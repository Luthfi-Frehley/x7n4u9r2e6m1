import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

def generate_sppd_pdf():
    pdf_path = os.path.join(os.path.dirname(__file__), 'docs', 'SPPD_2026_PLN_BALI_Luthfi.pdf')
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=26,
        bottomMargin=26
    )

    styles = getSampleStyleSheet()

    style_kop = ParagraphStyle(
        'KopText',
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
        textColor=colors.HexColor('#2563eb')
    )
    style_tbl_no = ParagraphStyle(
        'TblNo',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#1e293b')
    )
    style_tbl_field = ParagraphStyle(
        'TblField',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor('#1e293b')
    )
    style_tbl_val = ParagraphStyle(
        'TblVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor('#0f172a')
    )
    style_sign_title = ParagraphStyle(
        'SignTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
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

    story = []

    # 1. KOP SURAT
    logo_unsri_path = os.path.join(os.path.dirname(__file__), 'images', 'Lambang_Universitas_Sriwijaya.png')
    logo_pln_path = os.path.join(os.path.dirname(__file__), 'images', 'Logo_PLN.png')

    logo_unsri = Image(logo_unsri_path, width=44, height=44)
    logo_pln = Image(logo_pln_path, width=38, height=38)

    kop_text = """
    <b>KEMENTERIAN PENDIDIKAN TINGGI, SAINS, DAN TEKNOLOGI</b><br/>
    <b>UNIVERSITAS SRIWIJAYA &mdash; FAKULTAS TEKNIK</b><br/>
    <b>LABORATORIUM SISTEM KOMPUTASI & IOT TEKNIK ELEKTRO</b><br/>
    <font size="7" color="#475569">Jl. Raya Palembang - Prabumulih Km. 32 Indralaya 30662</font><br/>
    <b>KERJASAMA OPERASIONAL DENGAN PT PLN (PERSERO) UID BALI</b>
    """

    kop_table = Table(
        [[logo_unsri, Paragraph(kop_text, style_kop), logo_pln]],
        colWidths=[50, 422, 50]
    )
    kop_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (0, 0), 'LEFT'),
        ('ALIGN', (2, 0), (2, 0), 'RIGHT'),
    ]))
    story.append(kop_table)
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.8, color=colors.HexColor('#0f172a'), spaceAfter=1))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#0f172a'), spaceAfter=8))

    # 2. TITLE
    story.append(Paragraph("SURAT PERINTAH PERJALANAN DINAS (SPPD)", style_title))
    story.append(Spacer(1, 2))
    story.append(Paragraph("Nomor: SPPD-018/PLN-UID-BALI/TE-UNSRI/IX/2026", style_nomor))
    story.append(Spacer(1, 8))

    # 3. TABEL FORMAT SPPD STANDAR KEDINASAN / BUMN
    table_data = [
        [
            Paragraph("1.", style_tbl_no),
            Paragraph("Pejabat Pembuat Komitmen / Pemberi Perintah", style_tbl_field),
            Paragraph("Prof. Ir. Abu Bakar, M.T., Ph.D. (Kepala Lab IoT Unsri)<br/>Ir. Nyoman Arya, M.Eng. (Senior Manager Distribusi PLN UID Bali)", style_tbl_val)
        ],
        [
            Paragraph("2.", style_tbl_no),
            Paragraph("Nama Peneliti / Pegawai yang Diperintahkan", style_tbl_field),
            Paragraph("<b>Luthfi Hibatullah</b> (NIM: 03041182530001)", style_tbl_val)
        ],
        [
            Paragraph("3.", style_tbl_no),
            Paragraph("a. Pangkat / Golongan<br/>b. Jabatan / Instansi<br/>c. Tingkat Biaya Perjalanan Dinas", style_tbl_field),
            Paragraph("a. Mahasiswa Peneliti Khusus Skripsi / SKPI<br/>b. Lead Hardware &amp; Firmware Engineer / Lab IoT Unsri<br/>c. Tingkat Dinas BUMN &mdash; Riset Terapan", style_tbl_val)
        ],
        [
            Paragraph("4.", style_tbl_no),
            Paragraph("Maksud Perjalanan Dinas", style_tbl_field),
            Paragraph("<b>Investigasi Darurat &amp; Pemulihan Fisik On-Site:</b><br/>Manual reset hardware, pengujian relai pengaman, dan kalibrasi sensor daya pada <b>Gardu Trafo Distribusi Kuta Beach (ESP32-KTA-03)</b> menyusul anomali tegangan drop 0.0 Volt.", style_tbl_val)
        ],
        [
            Paragraph("5.", style_tbl_no),
            Paragraph("Alat Angkutan yang Dipergunakan", style_tbl_field),
            Paragraph("<b>Pesawat Udara (Penerbangan Komersial)</b><br/>Rute: Bandara Sultan Mahmud Badaruddin II (PLM) &rarr; I Gusti Ngurah Rai (DPS) PP", style_tbl_val)
        ],
        [
            Paragraph("6.", style_tbl_no),
            Paragraph("a. Tempat Berangkat<br/>b. Tempat Tujuan", style_tbl_field),
            Paragraph("a. Palembang, Sumatera Selatan<br/>b. <b>Kuta Beach &amp; Denpasar, Provinsi Bali</b>", style_tbl_val)
        ],
        [
            Paragraph("7.", style_tbl_no),
            Paragraph("a. Lamanya Perjalanan Dinas<br/>b. Tanggal Berangkat<br/>c. Tanggal Harus Kembali", style_tbl_field),
            Paragraph("a. 4 (Empat) Hari Kalender<br/>b. 21 September 2026<br/>c. 24 September 2026", style_tbl_val)
        ],
        [
            Paragraph("8.", style_tbl_no),
            Paragraph("Pembebanan Anggaran<br/>a. Instansi / Sumber Dana<br/>b. Akun / Mata Anggaran", style_tbl_field),
            Paragraph("a. DIPA Riset Terapan PT PLN (Persero) UID Bali TA 2026<br/>b. Kerjasama Implementasi Smart Grid Unsri - PLN (Sub-Pos: Tiket &amp; Akomodasi)", style_tbl_val)
        ],
        [
            Paragraph("9.", style_tbl_no),
            Paragraph("Keterangan Lain-lain", style_tbl_field),
            Paragraph("Kehadiran fisik peneliti di lokasi gardu bersifat <b>MANDATORY / WAJIB</b> karena sistem interlock pengaman menolak remote reboot.", style_tbl_val)
        ]
    ]

    sppd_table = Table(table_data, colWidths=[24, 188, 310])
    sppd_table.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#0f172a')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f8fafc')),
    ]))
    story.append(sppd_table)
    story.append(Spacer(1, 12))

    # 4. TANDA TANGAN KEDINASAN DUA PIHAK
    tgl_par = Paragraph("Dikeluarkan di : Palembang &amp; Denpasar<br/>Pada tanggal  : 18 September 2026", ParagraphStyle('TglDinas', parent=styles['Normal'], fontName='Helvetica', fontSize=7.5, alignment=TA_RIGHT, textColor=colors.HexColor('#475569')))
    story.append(tgl_par)
    story.append(Spacer(1, 6))

    ttd_data = [
        [
            Paragraph("Menyetujui &amp; Menugaskan,<br/><b>Kepala Lab Sistem Komputasi &amp; IoT Unsri</b>", style_sign_title),
            Paragraph("Mengetahui &amp; Memfasilitasi Akomodasi,<br/><b>Senior Manager Distribusi PLN UID Bali</b>", style_sign_title)
        ],
        [
            Paragraph("<font color='#2563eb'><b>[ STAMPEL &amp; TANDA TANGAN ELEKTRONIK ]</b></font><br/><font size='6.5' color='#64748b'>Ref: BSSN-UNSRI-2026-SPPD</font><br/><br/>", ParagraphStyle('St1', fontName='Helvetica-Oblique', fontSize=7, alignment=TA_CENTER, textColor=colors.HexColor('#2563eb'))),
            Paragraph("<font color='#dc2626'><b>[ TERVERIFIKASI ANGGARAN DINAS PLN ]</b></font><br/><font size='6.5' color='#64748b'>DIPA/PLN-BALI/DCC/2026/042</font><br/><br/>", ParagraphStyle('St2', fontName='Helvetica-Oblique', fontSize=7, alignment=TA_CENTER, textColor=colors.HexColor('#dc2626')))
        ],
        [
            Paragraph("<b><u>Prof. Ir. Abu Bakar, M.T., Ph.D.</u></b>", style_sign_name),
            Paragraph("<b><u>Ir. Nyoman Arya, M.Eng.</u></b>", style_sign_name)
        ],
        [
            Paragraph("NIP. 19680315 199203 1 002", style_sign_nip),
            Paragraph("NIP. 19750821 200003 1 001", style_sign_nip)
        ]
    ]

    t_ttd = Table(ttd_data, colWidths=[260, 260])
    t_ttd.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t_ttd)

    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cbd5e1'), spaceAfter=3))
    footer_text = """
    <font size="6.5" color="#64748b"><i>Perhatian: SPPD ini merupakan dokumen penugasan negara sah. Segala bentuk perintangan atas pelaksanaan tugas pemulihan infrastruktur kelistrikan terancam sanksi perundang-undangan. | ISO 27001 Certified</i></font>
    """
    story.append(Paragraph(footer_text, ParagraphStyle('FootSppd', alignment=TA_CENTER)))

    doc.build(story)
    print(f"SPPD PDF generated successfully: {pdf_path}")

if __name__ == '__main__':
    generate_sppd_pdf()

