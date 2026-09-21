import os
import sys
from datetime import datetime, timedelta
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

ROMAN_MONTHS = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
INDO_MONTHS = [
    '', 'Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni',
    'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'
]

def generate_spk_pdf(target_date=None):
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

    pdf_path = os.path.join(os.path.dirname(__file__), 'docs', 'SPK_2026_PLN_BALI_042_Kuta.pdf')
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    
    # 20mm margin
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=28,
        bottomMargin=28
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    style_kop_instansi = ParagraphStyle(
        'KopInstansi',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0f172a')
    )
    style_kop_sub = ParagraphStyle(
        'KopSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#334155')
    )
    style_title = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0f172a')
    )
    style_nomor = ParagraphStyle(
        'DocNomor',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2563eb')
    )
    style_body = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor('#1e293b')
    )
    style_table_label = ParagraphStyle(
        'TableLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#1e293b')
    )
    style_table_val = ParagraphStyle(
        'TableVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#1e293b')
    )
    style_sign_title = ParagraphStyle(
        'SignTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#1e293b')
    )
    style_sign_name = ParagraphStyle(
        'SignName',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0f172a')
    )
    style_sign_nip = ParagraphStyle(
        'SignNip',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#475569')
    )

    story = []

    # 1. KOP SURAT
    logo_unsri_path = os.path.join(os.path.dirname(__file__), 'images', 'Lambang_Universitas_Sriwijaya.png')
    logo_pln_path = os.path.join(os.path.dirname(__file__), 'images', 'Logo_PLN.png')

    logo_unsri = Image(logo_unsri_path, width=48, height=48)
    logo_pln = Image(logo_pln_path, width=42, height=42)

    kop_text = """
    <b>KEMENTERIAN PENDIDIKAN TINGGI, SAINS, DAN TEKNOLOGI</b><br/>
    <b>UNIVERSITAS SRIWIJAYA &mdash; FAKULTAS TEKNIK</b><br/>
    <b>LABORATORIUM SISTEM KOMPUTASI & IOT JURUSAN TEKNIK ELEKTRO</b><br/>
    <font size="7.5" color="#475569">Jalan Raya Palembang - Prabumulih Km. 32 Indralaya Ogan Ilir 30662</font><br/>
    <b>BERKOLABORASI DENGAN PT PLN (PERSERO) UNIT INDUK DISTRIBUSI BALI</b>
    """

    kop_table = Table(
        [[logo_unsri, Paragraph(kop_text, style_kop_instansi), logo_pln]],
        colWidths=[55, 410, 55]
    )
    kop_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (0, 0), 'LEFT'),
        ('ALIGN', (2, 0), (2, 0), 'RIGHT'),
    ]))
    story.append(kop_table)
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#0f172a'), spaceAfter=1))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#0f172a'), spaceAfter=12))

    # 2. JUDUL SURAT
    story.append(Paragraph("SURAT PERINTAH KERJA (SPK) &amp; SURAT PENUGASAN LAPANGAN", style_title))
    story.append(Spacer(1, 2))
    story.append(Paragraph(f"Nomor: SPK-042/PLN-UID-BALI/TE-UNSRI/{roman_month}/{year}", style_nomor))
    story.append(Spacer(1, 10))

    # 3. DASAR PENUGASAN
    dasar_text = f"""
    <b>MENIMBANG &amp; MEMPERHATIKAN:</b><br/>
    1. Laporan telemetri darurat SCADA Gateway Unsri-PLN tertanggal {formatted_date} Pukul 08:12:02 WITA mengenai hilangnya transmisi data (<i>Timeout &gt; 300 detik</i>) dan drop tegangan nol (0.0 Volt) pada <b>Node Sensor ESP32-KTA-03</b> di Gardu Trafo Distribusi Kuta Beach.<br/>
    2. Perjanjian Kerja Sama Riset Terapan Implementasi Smart Grid IoT antara PT PLN (Persero) Unit Induk Distribusi Bali dan Laboratorium Sistem Komputasi &amp; IoT Teknik Elektro Universitas Sriwijaya.<br/>
    3. Urgensi validasi perangkat fisik lapangan menjelang evaluasi dan audit keandalan sistem telemetri jaringan ketenagalistrikan nasional.
    """
    story.append(Paragraph(dasar_text, style_body))
    story.append(Spacer(1, 8))

    story.append(Paragraph("<b>DIPERINTAHKAN KEPADA:</b>", ParagraphStyle('SubHeader', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9, textColor=colors.HexColor('#0f172a'))))
    story.append(Spacer(1, 4))

    # 4. TABEL PERSONEL
    personel_data = [
        [Paragraph("Nama Lengkap", style_table_label), Paragraph(": <b>Luthfi Hibatullah</b>", style_table_val)],
        [Paragraph("Nomor Induk Mahasiswa (NIM)", style_table_label), Paragraph(": <b>03041182530001</b>", style_table_val)],
        [Paragraph("Program Studi / Jurusan", style_table_label), Paragraph(": Teknik Elektro &mdash; Konsentrasi Sistem Komputer &amp; IoT", style_table_val)],
        [Paragraph("Fakultas / Universitas", style_table_label), Paragraph(": Fakultas Teknik, Universitas Sriwijaya", style_table_val)],
        [Paragraph("Jabatan Penugasan", style_table_label), Paragraph(": <b>Peneliti Utama &amp; Lead Hardware IoT Engineer</b>", style_table_val)],
        [Paragraph("Didampingi Oleh", style_table_label), Paragraph(": Tim Reaksi Cepat Pemeliharaan Gardu PLN UP3 Bali Selatan (Denpasar)", style_table_val)],
    ]
    t_personel = Table(personel_data, colWidths=[160, 360])
    t_personel.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_personel)
    story.append(Spacer(1, 8))

    # 5. RINCIAN TUGAS (WAJIB KE KUTA)
    tugas_text = """
    <b>UNTUK MELAKSANAKAN TUGAS SEBAGAI BERIKUT:</b><br/>
    1. Melaksanakan kunjungan fisik langsung (<b>On-Site Field Visit</b>) ke titik instalasi <b>Gardu Trafo Distribusi Kuta Beach (Koordinat GPS: -8.7214, 115.1695)</b>.<br/>
    2. Melakukan manual hardware reset mikrokontroler ESP32-WROOM-32U, memeriksa relai proteksi beban lebih, sekring fasa sekunder 220V, dan catu daya cadangan baterai LiFePO4.<br/>
    3. Melakukan re-kalibrasi sensor arus CT Non-Invasive serta menguji ulang transmisi radio MQTT over TLS 1.3 ke Gateway Pusat Udayana.<br/>
    4. Menyusun Berita Acara Pemulihan Telemetri (BAPT) bersama teknisi PLN di lokasi Kuta Beach.<br/>
    <i>Catatan: Seluruh biaya transportasi, tiket dinas, akomodasi, dan operasional lapangan dibebankan pada Anggaran Kerja Sama Riset Terapan PLN &amp; Unsri TA 2026.</i>
    """
    story.append(Paragraph(tugas_text, style_body))
    story.append(Spacer(1, 16))

    # 6. TANDA TANGAN & PENGESAHAN (DUAL STAMP)
    tgl_text = f"Ditetapkan di : Denpasar &amp; Palembang<br/>Pada Tanggal : {formatted_date}"
    story.append(Paragraph(tgl_text, ParagraphStyle('Tgl', parent=styles['Normal'], fontName='Helvetica', fontSize=8, alignment=TA_RIGHT, textColor=colors.HexColor('#475569'))))
    story.append(Spacer(1, 10))

    ttd_data = [
        [
            Paragraph("Menyetujui &amp; Menugaskan,<br/>Kepala Lab Sistem Komputasi &amp; IoT Unsri", style_sign_title),
            Paragraph("Mengetahui Pihak BUMN,<br/>Senior Manager Distribusi PLN UID Bali", style_sign_title)
        ],
        [
            Spacer(1, 45),
            Spacer(1, 45)
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
    
    # 7. FOOTER KEAMANAN BSSN
    story.append(Spacer(1, 14))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cbd5e1'), spaceAfter=4))
    footer_doc = """
    <font size="7" color="#64748b"><i>Dokumen ini diterbitkan secara otomatis dan sah melalui Sistem Informasi Telemetri PLN x Unsri terenkripsi SHA-256 | Sertifikasi BSSN &amp; ISO 27001 | Security Token: SPK-PLN-BALI-042-LUTHFI-HIBATULLAH</i></font>
    """
    story.append(Paragraph(footer_doc, ParagraphStyle('Foot', alignment=TA_CENTER)))

    doc.build(story)
    print(f"PDF Generated successfully: {pdf_path}")

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else None
    generate_spk_pdf(target)

