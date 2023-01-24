import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 참조: https://www.youtube.com/watch?v=R2PbRgZwY80

# 세션설정
s = smtplib.SMTP("smtp.gmail.com", 587)

# TLS 보안시작
s.starttls()

# 로그인 인증
s.login("y2gon2@gmail.com", "sgaadtpxjnzkpndm")

# 보낼 메세지 설정
msg = MIMEMultipart()
msg["Subject"] = "제목 : 메일 보내기 테스트입니다."
msg["From"] = "y2gon2@gmail.com"
msg["To"] = "y2gon2@gmail.com"

msg.attach(MIMEText("내용 : 본문내용 테스트입니다."))
file_path = "data\\sample.pdf"
file = open(file_path, "rb")
part = MIMEApplication(
    file.read(),
    Name=basename(file_path)
)
# after the file is closed
part["Content-Disposition"] = 'attachment; filename="%s"' % basename(file_path)
msg.attach(part)

# 메일보내기
s.sendmail("y2gon2@gmail.com", "y2gon2@gmail.com", msg.as_string())

# 세션 종료
s.quit()

# ===================================================================
# Sending email without an attached file.
# import smtplib
# from email.mime.text import MIMEText
#
# # 세션설정
# s = smtplib.SMTP("smtp.gmail.com", 587)
#
# # TLS 보안시작
# s.starttls()
#
# # 로그인 인증
# s.login("y2gon2@gmail.com", "sgaadtpxjnzkpndm")
#
# # 보낼 메세지 설정
# msg = MIMEText("내용 : 본문내용 테스트입니다.")
# msg["Subject"] = "제목 : 메일 보내기 테스트입니다."
# msg["From"] = "y2gon2@gmail.com"
# msg["To"] = "y2gon2@gmail.com"
#
# # 메일보내기
# s.sendmail("y2gon2@gmail.com", "y2gon2@gmail.com", msg.as_string())
#
# # 세션 종료
# s.quit()
# ===================================================================