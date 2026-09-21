import os
import sys
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing

ROMAN_MONTHS = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
INDO_MONTHS = [
    '', 'Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni',
    'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'
]

def generate_sk_pdf(target_date=None):
    if target_date is None:
        target_date = datetime.now()
    elif isinstance(target_date, str):
        target_date = datetime.strptime(target_date, '%Y-%m-%d')

    day = target_date.day
    month_idx = target_date.month
    year = target_date.year
    month_name = INDO_MONTHS[month_idx]
    roman_month = ROMAN_MONTHS[month_idx]
    formatted_date = f"{day} {month_name} {year}"

    pdf_path = os.path.join(os.path.dirname(__file__), 'docs', 'SK_089_Pengangkatan_Lead_IoT_Engineer_Luthfi.pdf')
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=46,
        rightMargin=46,
        topMargin=26,
        bottomMargin=24
    )

    styles = getSampleStyleSheet()
    
    style_kop_instansi = ParagraphStyle(
        'KopInstansi',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13.5,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0f172a')
    )
    style_title = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0f172a')
    )
    style_nomor = ParagraphStyle(
        'DocNomor',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2563eb')
    )
    style_tentang = ParagraphStyle(
        'DocTentang',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0f172a')
    )
    style_body = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor('#1e293b')
    )
    style_body_bold = ParagraphStyle(
        'BodyBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor('#0f172a')
    )
    style_center_banner = ParagraphStyle(
        'CenterBanner',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0f172a')
    )
    style_tgl = ParagraphStyle(
        'TglRight',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=10,
        alignment=TA_RIGHT,
        textColor=colors.HexColor('#1e293b')
    )
    style_sign_title = ParagraphStyle(
        'SignTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#1e293b')
    )
    style_sign_name = ParagraphStyle(
        'SignName',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0f172a')
    )
    style_sign_nip = ParagraphStyle(
        'SignNip',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#475569')
    )
    style_bsre = ParagraphStyle(
        'BsreText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.5,
        leading=8.5,
        textColor=colors.HexColor('#1e3a8a')
    )

    story = []

    # 1. KOP SURAT
    logo_unsri_path = os.path.join(os.path.dirname(__file__), 'images', 'Lambang_Universitas_Sriwijaya.png')
    logo_pln_path = os.path.join(os.path.dirname(__file__), 'images', 'Logo_PLN.png')

    logo_unsri = Image(logo_unsri_path, width=46, height=46)
    logo_pln = Image(logo_pln_path, width=40, height=40)

    kop_text = """
    <b>KEMENTERIAN PENDIDIKAN TINGGI, SAINS, DAN TEKNOLOGI</b><br/>
    <b>UNIVERSITAS SRIWIJAYA &mdash; FAKULTAS TEKNIK</b><br/>
    <b>LABORATORIUM SISTEM KOMPUTASI & IOT JURUSAN TEKNIK ELEKTRO</b><br/>
    <font size="7.5" color="#475569">Jalan Raya Palembang - Prabumulih Km. 32 Indralaya Ogan Ilir 30662</font><br/>
    <b>BERKOLABORASI DENGAN PT PLN (PERSERO) UNIT INDUK DISTRIBUSI BALI</b>
    """

    kop_table = Table(
        [[logo_unsri, Paragraph(kop_text, style_kop_instansi), logo_pln]],
        colWidths=[48, 404, 48]
    )
    kop_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (0, 0), 'LEFT'),
        ('ALIGN', (2, 0), (2, 0), 'RIGHT'),
    ]))
    story.append(kop_table)
    story.append(Spacer(1, 3))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#0f172a'), spaceAfter=1))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#0f172a'), spaceAfter=8))

    # 2. JUDUL SK
    story.append(Paragraph("KEPUTUSAN BERSAMA DEKAN FAKULTAS TEKNIK UNIVERSITAS SRIWIJAYA<br/>DAN SENIOR MANAGER DISTRIBUSI PT PLN (PERSERO) UNIT INDUK DISTRIBUSI BALI", style_title))
    story.append(Spacer(1, 1))
    story.append(Paragraph(f"Nomor: SK-089/UN9.1.3/SK-PLN/{roman_month}/{year}", style_nomor))
    story.append(Spacer(1, 3))
    story.append(Paragraph("TENTANG<br/>PENGANGKATAN TENAGA AHLI RISET TERAPAN & LEAD HARDWARE IOT ENGINEER<br/>AUDIT DAN PEMULIHAN KEANDALAN GRID TELEMETRI DISTRIBUSI BALI", style_tentang))
    story.append(Spacer(1, 6))

    # 3. KONSIDERAN TABLE
    konsideran_data = [
        [
            Paragraph("<b>MENIMBANG</b>", style_body_bold),
            Paragraph(":", style_body_bold),
            Paragraph("a. bahwa guna menjaga keandalan transmisi cerdas Smart Grid IoT 20 kV di PT PLN UID Bali menjelang agenda strategis nasional;<br/>"
                      "b. bahwa terdeteksi anomali kritis drop tegangan (0.0V) pada Gardu Kuta Beach (ESP32-KTA-03) yang membutuhkan intervensi teknis langsung oleh perancang sistem;<br/>"
                      "c. bahwa Saudara Luthfi Hibatullah dinilai cakap dan memenuhi kualifikasi teknis tingkat lanjut untuk penugasan tersebut.", style_body)
        ],
        [
            Paragraph("<b>MENGINGAT</b>", style_body_bold),
            Paragraph(":", style_body_bold),
            Paragraph("1. UU No. 20 Tahun 2003 tentang Sisdiknas;<br/>"
                      "2. UU No. 30 Tahun 2009 tentang Ketenagalistrikan;<br/>"
                      "3. Perjanjian Kerja Sama Riset Smart Grid IoT Unsri &mdash; PT PLN UID Bali No: PKS-012/PLN-UID-BALI/TE-UNSRI/2025.", style_body)
        ]
    ]

    t_konsideran = Table(konsideran_data, colWidths=[75, 14, 411])
    t_konsideran.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(t_konsideran)
    story.append(Spacer(1, 3))

    # MEMUTUSKAN / MENETAPKAN
    story.append(Paragraph("MEMUTUSKAN:", style_center_banner))
    story.append(Paragraph("<b>MENETAPKAN:</b>", style_body_bold))
    story.append(Spacer(1, 2))

    # DIKTUM TABLE
    mandat_html = """
    Mengangkat Saudara mahasiswa peneliti di bawah ini:<br/>
    &bull; <b>Nama Lengkap:</b> Luthfi Hibatullah &nbsp;&nbsp;&nbsp;&bull; <b>NIM:</b> 03041182530001<br/>
    &bull; <b>Program Studi:</b> Teknik Elektro &mdash; Konsentrasi Sistem Komputer & IoT Unsri<br/>
    &bull; <b>Jabatan Kedinasan:</b> <font color="#1d4ed8"><b>PENELITI UTAMA & LEAD HARDWARE IOT ENGINEER</b></font>
    """

    diktum_data = [
        [
            Paragraph("<b>KESATU</b>", style_body_bold),
            Paragraph(":", style_body_bold),
            Paragraph(mandat_html, style_body)
        ],
        [
            Paragraph("<b>KEDUA</b>", style_body_bold),
            Paragraph(":", style_body_bold),
            Paragraph("Memberikan mandat dan wewenang penuh untuk: (1) Melakukan audit 25 node telemetri nasional dan investigasi Gardu Kuta Beach; "
                      "(2) Melaksanakan manipulasi strapping pin bootloader ROM GPIO0-GND, flashing firmware UART on-site, penggantian sekring kaca 500mA, dan perlakuan conformal coating anti-garam; "
                      "(3) Mengesahkan BAST pemulihan fisik bersama Tim UP3 Bali Selatan.", style_body)
        ],
        [
            Paragraph("<b>KETIGA</b>", style_body_bold),
            Paragraph(":", style_body_bold),
            Paragraph("Segala biaya yang timbul sebagai akibat pelaksanaan tugas dan tanggung jawab ini dibebankan sepenuhnya secara mandiri (swadana) oleh pelaksana tugas yang bersangkutan, serta tidak membebankan anggaran keuangan pada institusi Universitas Sriwijaya maupun PT PLN (Persero).", style_body)
        ],
        [
            Paragraph("<b>KEEMPAT</b>", style_body_bold),
            Paragraph(":", style_body_bold),
            Paragraph("Keputusan Bersama ini mulai berlaku terhitung sejak tanggal ditetapkan.", style_body)
        ]
    ]

    t_diktum = Table(diktum_data, colWidths=[75, 14, 411])
    t_diktum.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(t_diktum)
    story.append(Spacer(1, 4))

    # TANGGAL
    story.append(Paragraph(f"Ditetapkan di: Palembang & Denpasar<br/>Pada tanggal: <b>{formatted_date}</b>", style_tgl))
    story.append(Spacer(1, 4))

    # PENGESAHAN DUA PIHAK & QR CODE
    d_qr = Drawing(44, 44)
    q = qr.QrCodeWidget('https://scada-unsri.my.id/verify.html?doc=SK-089')
    q.barWidth = 44
    q.barHeight = 44
    d_qr.add(q)

    tte_badge_text = """
    <font size="6" color="#047857"><b>TTE TERSERTIFIKASI BSRÉ - BSSN</b></font><br/>
    <font size="5.5" color="#64748b">Root CA Pemerintah RI &bull; Valid</font>
    """

    sign_data = [
        [
            Paragraph("Menyetujui & Menetapkan,<br/>Kepala Lab Sistem Komputasi & IoT Unsri", style_sign_title),
            Paragraph("Mengesahkan Pihak BUMN,<br/>Senior Manager Distribusi PLN UID Bali", style_sign_title)
        ],
        [
            Spacer(1, 38),
            Spacer(1, 38)
        ],
        [
            Paragraph("<u>Prof. Ir. Abu Bakar, M.T., Ph.D.</u><br/><font color='#475569'>NIP. 19680315 199203 1 002</font>", style_sign_name),
            Paragraph("<u>Ir. Nyoman Arya, M.Eng.</u><br/><font color='#475569'>NIP. 19750821 200003 1 001</font>", style_sign_name)
        ]
    ]

    t_sign = Table(sign_data, colWidths=[250, 250])
    t_sign.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(t_sign)
    story.append(Spacer(1, 6))

    # BSRÉ VERIFICATION BANNER AT BOTTOM
    bsre_banner_text = """
    <b>DOKUMEN INI TELAH DITANDATANGANI SECARA ELEKTRONIK (TTE) MENGGUNAKAN SERTIFIKAT ELEKTRONIK RESMI BSRÉ - BSSN.</b><br/>
    Sesuai ketentuan UU ITE No. 11/2008 & PP No. 71/2019. Pindai QR Code di samping untuk memverifikasi keaslian naskah dinas atau buka: <b>https://scada-unsri.my.id/verify.html?doc=SK-089</b>
    """

    bsre_table = Table(
        [[d_qr, Paragraph(bsre_banner_text, style_bsre)]],
        colWidths=[48, 452]
    )
    bsre_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#eff6ff')),
        ('BOX', (0, 0), (-1, -1), 0.8, colors.HexColor('#3b82f6')),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(bsre_table)
    story.append(Spacer(1, 4))

    # SECURITY FOOTER
    style_sec = ParagraphStyle(
        'SecFooter',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6,
        leading=8,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#64748b')
    )
    story.append(Paragraph("Dokumen ini sah dan terdaftar pada Sistem Administrasi Terpadu SCADA PLN UID Bali & Universitas Sriwijaya | Sertifikasi ISO 27001 | Token: SK-089-UN9-PLN-BALI-LUTHFI-HIBATULLAH-SHA256", style_sec))

    doc.build(story)
    print(f"SK PDF Generated successfully: {pdf_path}")

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else None
    generate_sk_pdf(target)
