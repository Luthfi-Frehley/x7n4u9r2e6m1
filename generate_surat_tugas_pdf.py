import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.graphics.shapes import Drawing, Rect, String, Group
from reportlab.graphics.barcode import qr

def generate_surat_tugas_pdf(output_filename="Surat_Perintah_Tugas_Darurat_Bali_Luthfi.pdf"):
    pdf_path = os.path.join(os.path.dirname(__file__), 'docs', output_filename)
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    
    # Margin 10mm (tight for 1 page precision)
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=32,
        rightMargin=32,
        topMargin=22,
        bottomMargin=20
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    style_kop_instansi = ParagraphStyle(
        'KopInstansi',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0f172a')
    )
    style_title = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0f172a')
    )
    style_nomor = ParagraphStyle(
        'DocNomor',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#1d4ed8')
    )
    style_body = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11.5,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor('#1e293b')
    )
    style_table_label = ParagraphStyle(
        'TableLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor('#1e293b')
    )
    style_table_val = ParagraphStyle(
        'TableVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor('#1e293b')
    )
    style_tgl = ParagraphStyle(
        'TglRight',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=10,
        alignment=TA_RIGHT,
        textColor=colors.HexColor('#334155')
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
    style_bsre = ParagraphStyle(
        'BsreText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.5,
        leading=9,
        alignment=TA_LEFT,
        textColor=colors.HexColor('#1e3a8a')
    )
    style_sec = ParagraphStyle(
        'SecFooter',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6,
        leading=8,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#64748b')
    )

    story = []

    # 1. KOP SURAT BERSAMA
    logo_unsri_path = os.path.join(os.path.dirname(__file__), 'images', 'Lambang_Universitas_Sriwijaya.png')
    logo_pln_path = os.path.join(os.path.dirname(__file__), 'images', 'Logo_PLN.png')

    logo_unsri = Image(logo_unsri_path, width=44, height=44)
    logo_pln = Image(logo_pln_path, width=38, height=48)

    kop_text = """
    <b>KEMENTERIAN PENDIDIKAN TINGGI, SAINS, DAN TEKNOLOGI</b><br/>
    <b>UNIVERSITAS SRIWIJAYA &mdash; FAKULTAS TEKNIK</b><br/>
    <b>LABORATORIUM SISTEM KOMPUTASI & IOT JURUSAN TEKNIK ELEKTRO</b><br/>
    <font size="7" color="#475569">Jalan Raya Palembang - Prabumulih Km. 32 Indralaya Ogan Ilir 30662</font><br/>
    <b>BERKOLABORASI DENGAN PT PLN (PERSERO) UNIT INDUK DISTRIBUSI BALI</b>
    """

    kop_table = Table(
        [[logo_unsri, Paragraph(kop_text, style_kop_instansi), logo_pln]],
        colWidths=[50, 430, 50]
    )
    kop_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (0, 0), 'LEFT'),
        ('ALIGN', (2, 0), (2, 0), 'RIGHT'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(kop_table)
    story.append(Spacer(1, 3))
    story.append(HRFlowable(width="100%", thickness=1.8, color=colors.HexColor('#0f172a'), spaceAfter=1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor('#0f172a'), spaceAfter=8))

    # 2. JUDUL SURAT
    story.append(Paragraph("SURAT PERINTAH TUGAS LAPANGAN DARURAT (ON-SITE DISPATCH)", style_title))
    story.append(Paragraph("Nomor: ST-042/UN9.1.3/PLN-UID-BALI/IX/2026 &bull; SPK-042", style_nomor))
    story.append(Spacer(1, 6))

    # 3. DASAR PENUGASAN (MENIMBANG & MEMPERHATIKAN)
    dasar_text = """
    <b>MENIMBANG &amp; MEMPERHATIKAN:</b><br/>
    1. Surat Keputusan Bersama No: <b>SK-089/UN9.1.3/SK-PLN/IX/2026</b> tentang Pengangkatan Tenaga Ahli Riset Terapan &amp; Lead Hardware IoT Engineer Monitoring Grid 20 kV Bali.<br/>
    2. Hasil rapat koordinasi teknis via teleconference antara Kepala Lab Sistem Komputasi &amp; IoT FT Unsri (<b>Prof. Ir. Abu Bakar</b>) bersama Senior Manager Distribusi PT PLN UID Bali (<b>Ir. Nyoman Arya</b>) tertanggal 25 September 2026.<br/>
    3. Laporan darurat telemetri SCADA Central Gateway Udayana atas anomali drop tegangan nol (<b>0.00 Volt / Blackout</b>) pada <b>Node Sensor ESP32-KTA-03</b> di Gardu Distribusi Kuta Beach, di mana upaya perbaikan jarak jauh (<i>remote reset &amp; OTA</i>) mengalami timeout akibat indikasi kerusakan fisik hardware terpapar uap garam laut, sehingga mendesak dilakukan intervensi on-site oleh perancang sistem.
    """
    story.append(Paragraph(dasar_text, style_body))
    story.append(Spacer(1, 5))

    story.append(Paragraph("<b>MEMBERIKAN PERINTAH TUGAS KEPADA:</b>", ParagraphStyle('SubHeader', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, textColor=colors.HexColor('#0f172a'))))
    story.append(Spacer(1, 3))

    # 4. TABEL PERSONEL PENERIMA TUGAS
    personel_data = [
        [Paragraph("Nama Lengkap", style_table_label), Paragraph(": <b>Luthfi Hibatullah</b>", style_table_val)],
        [Paragraph("Nomor Induk Mahasiswa (NIM)", style_table_label), Paragraph(": <b>03041182530001</b>", style_table_val)],
        [Paragraph("Email Resmi / Kontak", style_table_label), Paragraph(": <b>luthfiab80@gmail.com</b> (Email Pribadi) &bull; luthfi@scada-unsri.my.id", style_table_val)],
        [Paragraph("Program Studi / Jurusan", style_table_label), Paragraph(": Teknik Elektro &mdash; Konsentrasi Sistem Komputer &amp; IoT (FT Unsri)", style_table_val)],
        [Paragraph("Jabatan Penugasan", style_table_label), Paragraph(": <font color='#1d4ed8'><b>Peneliti Utama &amp; Lead Hardware IoT Engineer</b></font>", style_table_val)],
        [Paragraph("Tim Pendamping Lapangan", style_table_label), Paragraph(": Tim Reaksi Cepat (TRC) Unit Pelaksana Pelayanan Pelanggan (UP3) Bali Selatan", style_table_val)],
    ]
    t_personel = Table(personel_data, colWidths=[150, 380])
    t_personel.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_personel)
    story.append(Spacer(1, 5))

    # 5. RINCIAN TUGAS DAN FASILITAS OPERASIONAL
    tugas_text = """
    <b>UNTUK MELAKSANAKAN TUGAS SEBAGAI BERIKUT:</b><br/>
    1. Melaksanakan kunjungan fisik darurat (<b>On-Site Field Visit</b>) ke titik instalasi <b>Gardu Trafo Distribusi Kuta Beach (Koordinat GPS: -8.7214, 115.1695)</b>;<br/>
    2. Melakukan intervensi teknis perangkat keras: inspeksi sekring kaca proteksi 500mA, manual hardware reset via pin strapping GPIO0-GND, dan flashing ulang bootloader ROM melalui port UART on-site;<br/>
    3. Memberikan perlakuan <i>conformal coating anti-saline</i> pada PCB sensor dan re-kalibrasi sensor arus CT Non-Invasive 100A:50mA;<br/>
    4. Menyusun dan menandatangani Berita Acara Pemulihan Telemetri (BAPT) bersama Tim Teknisi PLN UP3 Bali Selatan;<br/>
    5. <b>Fasilitas &amp; Akomodasi:</b> Mahasiswa pelaksana difasilitasi kamar dinas di <b>Wisma Tamu / Mess Diklat PT PLN (Persero) UID Bali (Jl. Letda Tantular No. 1, Renon, Denpasar)</b> secara gratis tanpa biaya penginapan pribadi, serta didampingi armada kendaraan patroli dinas Tim TRC PLN Bali Selatan;<br/>
    <i>Catatan Anggaran: Seluruh tiket penerbangan rute Palembang (PLM) &harr; Denpasar (DPS) PP serta operasional darurat dibebankan melalui mekanisme 100% Reimbursement Kuitansi Resmi PLN UID Bali sesuai SPPD-018 dan RAB-042.</i>
    """
    story.append(Paragraph(tugas_text, style_body))
    story.append(Spacer(1, 6))

    # 6. TANGGAL & PENGESAHAN DUA PIHAK
    tgl_text = "Ditetapkan di : Palembang &amp; Denpasar<br/>Pada Tanggal : <b>25 September 2026</b>"
    story.append(Paragraph(tgl_text, style_tgl))
    story.append(Spacer(1, 4))

    # PENGESAHAN DUA PIHAK
    sign_data = [
        [
            Paragraph("Menyetujui &amp; Menugaskan,<br/>Kepala Lab Sistem Komputasi &amp; IoT Unsri", style_sign_title),
            Paragraph("Mengesahkan Pihak BUMN,<br/>Senior Manager Distribusi PLN UID Bali", style_sign_title)
        ],
        [
            Spacer(1, 36),
            Spacer(1, 36)
        ],
        [
            Paragraph("<u>Prof. Ir. Abu Bakar, M.T., Ph.D.</u><br/><font size='7' color='#475569'>NIP. 19680315 199203 1 002</font>", style_sign_name),
            Paragraph("<u>Ir. Nyoman Arya, M.Eng.</u><br/><font size='7' color='#475569'>NIP. 19750821 200003 1 001</font>", style_sign_name)
        ]
    ]

    t_sign = Table(sign_data, colWidths=[265, 265])
    t_sign.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(t_sign)
    story.append(Spacer(1, 6))

    # 7. QR CODE & BSRE VERIFICATION BANNER
    d_qr = Drawing(42, 42)
    q = qr.QrCodeWidget('https://scada-unsri.my.id/verify.html?doc=SPK-042')
    q.barWidth = 42
    q.barHeight = 42
    d_qr.add(q)

    bsre_banner_text = """
    <b>SURAT TUGAS INI DITERBITKAN SECARA ELEKTRONIK (TTE) &amp; TERVERIFIKASI RESMI ROOT CA BSRÉ - BSSN.</b><br/>
    Sesuai ketentuan UU ITE No. 11/2008 &amp; PP No. 71/2019. Pindai QR Code di samping untuk memverifikasi keaslian penugasan lapangan atau kunjungi: <b>https://scada-unsri.my.id/verify.html?doc=SPK-042</b>
    """

    bsre_table = Table(
        [[d_qr, Paragraph(bsre_banner_text, style_bsre)]],
        colWidths=[46, 484]
    )
    bsre_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#eff6ff')),
        ('BOX', (0, 0), (-1, -1), 0.8, colors.HexColor('#3b82f6')),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(bsre_table)
    story.append(Spacer(1, 3))

    # 8. SECURITY FOOTER
    story.append(Paragraph("Dokumen Kedinasan Resmi Satgas Smart Grid PLN UID Bali & Universitas Sriwijaya | Sertifikasi Keamanan ISO 27001 | Token: ST-042-PLN-BALI-LUTHFI-HIBATULLAH-BSSN-SHA256", style_sec))

    doc.build(story)
    print(f"Surat Tugas PDF Generated successfully: {pdf_path}")

if __name__ == '__main__':
    generate_surat_tugas_pdf()
    # Also update SPK-042
    generate_surat_tugas_pdf("SPK_2026_PLN_BALI_042_Kuta.pdf")
