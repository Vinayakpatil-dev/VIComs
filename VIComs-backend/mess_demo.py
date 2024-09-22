import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("abijith0707@gmail.com","kgth rtlx wqhy dtsm")
message="hello team "
s.sendmail("abijith0707@gmail.com","abijith0707@gmail.com",message)
s.quit()
