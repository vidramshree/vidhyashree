#!usr/bin/python3
import smtplib
s=smtplib.SMTP('Smtp.gmail.com',587)
s.starttls()
s.login("ramyareddy192001@gmail.com","ramyashree")
message="hi"
s.sendmail("ramyareddy192001@gmail.com","ramyareddy192001@gmail.com",message)
s.quit()




