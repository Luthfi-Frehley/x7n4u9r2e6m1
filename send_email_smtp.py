import smtplib
import argparse
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_dispatch_email(smtp_server, smtp_port, username, password, to_email, use_tls=True):
    html_path = os.path.join(os.path.dirname(__file__), 'docs', 'email-dispatch-bali.html')
    with open(html_path, 'r', encoding='utf-8') as f:
        html_body = f.read()

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "[URGENT DISPATCH] Perintah Penugasan Lapangan Darurat: Anomali Drop 0.0V Gardu Kuta Beach Bali (SPK-042 / SPPD-018)"
    msg['From'] = f"PT PLN (Persero) UID Bali <{username}>"
    msg['To'] = to_email
    msg['X-Priority'] = '1'
    msg['Importance'] = 'High'

    part = MIMEText(html_body, 'html', 'utf-8')
    msg.attach(part)

    print(f"Connecting to {smtp_server}:{smtp_port}...")
    server = smtplib.SMTP(smtp_server, smtp_port)
    if use_tls:
        server.starttls()
    server.login(username, password)
    server.sendmail(username, [to_email], msg.as_string())
    server.quit()
    print(f"Email successfully sent to {to_email}!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Send official PLN UID Bali dispatch email")
    parser.add_argument('--server', default="mail.scada-unsri.my.id", help="SMTP server host")
    parser.add_argument('--port', type=int, default=587, help="SMTP server port (default: 587)")
    parser.add_argument('--user', default="abubakar@scada-unsri.my.id", help="SMTP username")
    parser.add_argument('--pwd', required=False, help="SMTP password")
    parser.add_argument('--to', default="abubakar@scada-unsri.my.id", help="Recipient email")
    args = parser.parse_args()

    if not args.pwd:
        print("Note: To send actual email, run: python send_email_smtp.py --pwd 'YOUR_PASSWORD'")
    else:
        send_dispatch_email(args.server, args.port, args.user, args.pwd, args.to)
