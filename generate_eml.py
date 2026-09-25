import os

html_path = os.path.join(os.path.dirname(__file__), 'docs', 'email-dispatch-bali.html')
eml_path = os.path.join(os.path.dirname(__file__), 'docs', 'Email_Perintah_Tugas_Bali_PLN.eml')

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

eml_header = """From: "PT PLN (Persero) UID Bali - Divisi Distribusi" <distribusi.uidbali@pln.co.id>
To: "Luthfi Hibatullah" <luthfi@scada-unsri.my.id>
Cc: "Prof. Ir. Abu Bakar, M.T., Ph.D." <abubakar@unsri.ac.id>, "Sekretariat Manajer Distribusi" <sekretariat.distribusi@pln.co.id>
Subject: [URGENT DISPATCH] Perintah Penugasan Lapangan Darurat: Anomali Drop 0.0V Gardu Kuta Beach Bali (SPK-042 / SPPD-018)
Date: Fri, 25 Sep 2026 15:45:12 +0800
Message-ID: <DISPATCH-20260925-042-KUTA@mail.pln.co.id>
MIME-Version: 1.0
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 8bit
X-Priority: 1 (Highest)
Importance: High
Priority: Urgent

"""

with open(eml_path, 'w', encoding='utf-8') as f:
    f.write(eml_header + html_content)

print(f"EML file created successfully: {eml_path}")
