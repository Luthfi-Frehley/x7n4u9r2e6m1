import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.barcode import qr

def generate_surat_wali_pdf():
    pdf_path = os.path.join(os.path.dirname(__file__), 'docs', 'Surat_Pemberitahuan_Wali_Mahasiswa.pdf')
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
        fontSize=11.5,
        leading=14.5,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0f172a')
    )
    style_nomor = ParagraphStyle(
        'DocNomor',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
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

    # 1. KOP SURAT
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
    story.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor('#0f172a'), spaceAfter=7))

    # 2. JUDUL
    story.append(Paragraph("SURAT PEMBERITAHUAN RESMI KEPADA ORANG TUA / WALI MAHASISWA", style_title))
    story.append(Paragraph("Nomor: 048/UN9.1.3/PLN-BALI/WALI/IX/2026 &bull; Status: MANDATORY (WAJIB)", style_nomor))
    story.append(Spacer(1, 5))

    # 3. METADATA TUJUAN
    tujuan_text = """
    Kepada Yth.<br/>
    <b>Bapak / Ibu Orang Tua &amp; Wali Mahasiswa</b> dari Saudara: <b>Luthfi Hibatullah</b> (NIM: 03041182530001)<br/>
    <font color="#475569">Program Studi Teknik Elektro (Konsentrasi Sistem Komputer &amp; IoT) Fakultas Teknik Universitas Sriwijaya</font>
    """
    story.append(Paragraph(tujuan_text, style_body))
    story.append(Spacer(1, 4))

    # 4. ISI PEMBERITAHUAN
    pembuka_text = """
    Menindaklanjuti Surat Keputusan Bersama No: <b>SK-089/UN9.1.3/SK-PLN/IX/2026</b> serta Surat Perintah Kerja No: <b>SPK-042/PLN-UID-BALI/TE-UNSRI/IX/2026</b> perihal penugasan riset implementasi telemetri kelistrikan cerdas Smart Grid 20 kV di wilayah PT PLN (Persero) UID Bali, bersama ini disampaikan beberapa ketetapan resmi kepada Orang Tua / Wali Mahasiswa:
    """
    story.append(Paragraph(pembuka_text, style_body))
    story.append(Spacer(1, 4))

    # POIN 1: SIFAT PENUGASAN WAJIB
    poin1_box = """
    <b>1. STATUS PENUGASAN: BERSIFAT WAJIB &amp; TIDAK DAPAT DIWAKILKAN (MANDATORY)</b><br/>
    Saudara Luthfi Hibatullah bertindak sebagai <b>Peneliti Utama &amp; Lead Hardware IoT Engineer</b> yang merancang langsung arsitektur mikrokontroler sensor gardu transmisi. Berdasarkan evaluasi teknis darurat atas anomali drop 0.0V pada Gardu Kuta Beach yang tidak dapat diatasi melalui remote monitoring dari Palembang, kehadiran fisik di lokasi penugasan (Bali) bersifat <b>wajib mutlak</b> demi pemulihan sistem dan merupakan syarat penyelesaian luaran riset skripsi.
    """
    
    # POIN 2: BIAYA TRANSPORTASI MANDIRI & REIMBURSEMENT
    poin2_box = """
    <b>2. KETENTUAN ANGGARAN &amp; PEMBIAYAAN TRANSPORTASI MANDIRI (SWADANA)</b><br/>
    Sesuai ketentuan Diktum Ketiga SK-089 mengenai skema peneliti mandiri akademik: (a) Pengadaan tiket transportasi awal penerbangan rute Palembang (PLM) &harr; Denpasar (DPS) diselenggarakan secara <b>mandiri (swadana)</b> oleh mahasiswa pelaksana menggunakan tabungan proyek riset pribadi dan <b>tidak membebankan anggaran keluarga/wali</b>; (b) Seluruh biaya transportasi dinas tersebut diatur melalui mekanisme <b>100% Penggantian (Reimbursement) Resmi PT PLN UID Bali</b> sesuai dokumen SPPD-018 dan RAB-042 yang telah disahkan pihak keuangan BUMN.
    """

    # POIN 3: JAMINAN AKOMODASI & PROTOKOL KEAMANAN
    poin3_box = """
    <b>3. FASILITAS PENGINAPAN, MOBILITAS &amp; KESELAMATAN (K3) RESMI TERJAMIN</b><br/>
    Instansi memastikan keluarga tidak perlu mengkhawatirkan akomodasi mahasiswa di Bali: (a) Mahasiswa ditempatkan di <b>Wisma Tamu / Mess Resmi PT PLN (Persero) UID Bali</b> (Jl. Letda Tantular No. 1, Renon, Denpasar) bebas biaya sewa penginapan; (b) Seluruh mobilitas inspeksi gardu dikawal kendaraan dinas patroli Tim Reaksi Cepat (TRC) UP3 Bali Selatan; (c) Wajib mematuhi SOP K3 proteksi kelistrikan tegangan tinggi di bawah supervisi langsung Engineer PLN.
    """

    poin_table_data = [
        [Paragraph(poin1_box, style_body)],
        [Paragraph(poin2_box, style_body)],
        [Paragraph(poin3_box, style_body)]
    ]
    t_poin = Table(poin_table_data, colWidths=[530])
    t_poin.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BACKGROUND', (0,0), (0,0), colors.HexColor('#eff6ff')),
        ('BACKGROUND', (0,1), (0,1), colors.HexColor('#fffbeb')),
        ('BACKGROUND', (0,2), (0,2), colors.HexColor('#f0fdf4')),
        ('BOX', (0,0), (0,0), 0.6, colors.HexColor('#93c5fd')),
        ('BOX', (0,1), (0,1), 0.6, colors.HexColor('#fcd34d')),
        ('BOX', (0,2), (0,2), 0.6, colors.HexColor('#86efac')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_poin)
    story.append(Spacer(1, 4))

    penutup_text = """
    Demikian surat pemberitahuan kedinasan ini disampaikan. Kami memohon doa dan restu Bapak/Ibu demi kelancaran tugas serta keselamatan ananda selama menjalankan amanah strategis ini.
    """
    story.append(Paragraph(penutup_text, style_body))
    story.append(Spacer(1, 3))

    # TANGGAL
    tgl_text = "Ditetapkan di : Palembang &amp; Denpasar<br/>Pada Tanggal : <b>25 September 2026</b>"
    story.append(Paragraph(tgl_text, style_tgl))
    story.append(Spacer(1, 3))

    # PENGESAHAN DUA PIHAK
    sign_data = [
        [
            Paragraph("Menyetujui Pihak Perguruan Tinggi,<br/>Kepala Lab Sistem Komputasi &amp; IoT Unsri", style_sign_title),
            Paragraph("Mengesahkan Pihak BUMN,<br/>Senior Manager Distribusi PLN UID Bali", style_sign_title)
        ],
        [
            Spacer(1, 32),
            Spacer(1, 32)
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
    story.append(Spacer(1, 4))

    # QR CODE BSRÉ
    d_qr = Drawing(38, 38)
    q = qr.QrCodeWidget('https://scada-unsri.my.id/verify.html?doc=SK-089')
    q.barWidth = 38
    q.barHeight = 38
    d_qr.add(q)

    bsre_banner_text = """
    <b>SURAT PEMBERITAHUAN RESMI INI DILINDUNGI TTE TERDAFTAR BSRÉ - BSSN RI.</b><br/>
    Pindai QR Code di samping untuk memverifikasi keabsahan penugasan dan surat keputusan bersama di portal resmi: <b>https://scada-unsri.my.id/verify.html?doc=SK-089</b>
    """
    bsre_table = Table(
        [[d_qr, Paragraph(bsre_banner_text, style_bsre)]],
        colWidths=[42, 488]
    )
    bsre_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#eff6ff')),
        ('BOX', (0, 0), (-1, -1), 0.8, colors.HexColor('#3b82f6')),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(bsre_table)
    story.append(Spacer(1, 2))

    story.append(Paragraph("Dokumen Pemberitahuan Resmi Tim Satgas Riset Smart Grid FT Unsri & PT PLN (Persero) UID Bali | ISO 27001 Certified", style_sec))

    doc.build(story)
    print(f"Surat Wali PDF Generated successfully: {pdf_path}")

if __name__ == '__main__':
    generate_surat_wali_pdf()
