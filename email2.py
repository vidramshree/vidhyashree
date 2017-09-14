#!/usr/bin/python3
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("ramyareddy192001@gmail.com","ramyashree19")
message="hi"
s.sendmail("ramyareddy192001@gmail.com","ramyashree",message)
s.quit()




