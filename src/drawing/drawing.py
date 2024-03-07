import smtplib
from getpass import getpass
from email.message import EmailMessage
import pandas as pd

def get_smtp_settings(email_address):
    domain = email_address.split('@')[1].lower()

    if domain == '163.com':
        return 'smtp.163.com', 465
    elif domain == 'gmail.com':
        return 'smtp.gmail.com', 465
    elif domain == 'qq.com':
        return 'smtp.qq.com', 465
    else:
        raise ValueError(f"Unsupported email domain: {domain}")

def send_email(sender_email, sender_password, recipient_email, filename, recipient_name):
    smtp_host, smtp_port = get_smtp_settings(sender_email)
    smtp = smtplib.SMTP_SSL(smtp_host, smtp_port)

    subject = "Python邮件主题"
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    with open(filename, 'r', encoding='utf-8') as f:
        file_content = f.read()

    modified_content = f"{recipient_name}, {file_content}"

    msg.set_content(modified_content)

    smtp.login(sender_email, sender_password)
    smtp.send_message(msg)
    smtp.quit()

def main():
    sender_email = input('请输入你的邮箱地址: ')
    sender_password = getpass('请输入你的邮箱密码: ')

    file_path = 'src/send_message/index.xlsx'
    data = pd.read_excel(file_path)
    recipient_data = data.set_index('姓名')[['邮箱']].to_dict()['邮箱']

    for recipient_name, recipient_email in recipient_data.items():
        filename = r"src\send_message\test.txt"
        send_email(sender_email, sender_password, recipient_email, filename, recipient_name)

if __name__ == '__main__':
    main()
