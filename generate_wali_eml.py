import os

html_path = os.path.join(os.path.dirname(__file__), 'docs', 'email-pemberitahuan-wali.html')
eml_path = os.path.join(os.path.dirname(__file__), 'docs', 'Email_Pemberitahuan_Wali_Mahasiswa.eml')

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

eml_header = """From: "Sekretariat Tim Riset FT Unsri x PT PLN UID Bali" <distribusi.uidbali@pln.co.id>
To: "Orang Tua / Wali Sdr. Luthfi Hibatullah" <luthfiab80@gmail.com>
Cc: "Prof. Ir. Abu Bakar, M.T., Ph.D." <abubakar@unsri.ac.id>, "Ir. Nyoman Arya, M.Eng." <nyoman.arya@pln.co.id>, <luthfi@scada-unsri.my.id>
Subject: [PEMBERITAHUAN KEDINASAN] Penugasan Lapangan Wajib & Ketentuan Operasional Mandiri Riset Smart Grid Bali Sdr. Luthfi Hibatullah
Date: Fri, 25 Sep 2026 16:00:00 +0800
Message-ID: <PEMBERITAHUAN-WALI-20260925-048@pln.co.id>
MIME-Version: 1.0
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 8bit
X-Priority: 1 (Highest)
Importance: High
Priority: Urgent

"""

with open(eml_path, 'w', encoding='utf-8') as f:
    f.write(eml_header + html_content)

print(f"EML Wali created successfully: {eml_path}")
