import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send(email, date, keyword):
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login('y2gon2@gmail.com', 'sgaadtpxjnzkpndm')

    msg = MIMEMultipart()
    msg["Subject"] = '[' + keyword + '] ' + date + '일자 크롤링 자료 송부'
    msg['From'] = 'y2gon2@gmail.com'
    msg['To'] = email

    msg.attach(MIMEText('유첨파일 (' + keyword + '.txt) 참조'))
    file_path = './data/' + email + '/' + date + '/' + keyword + '.txt'
    with open(file_path, 'rb') as f:
        part = MIMEApplication(
            f.read(),
            Name=basename(file_path)
        )

    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file_path)
    msg.attach(part)

    session.sendmail('y2gon2@gmail.com', email, msg.as_string())
    session.quit()