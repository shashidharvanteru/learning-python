import smtplib
host = "smtp.gmail.com"
port= 587
username="hungrybird319@gmail.com"
password="Shashi@@2"
email_conn=smtplib.SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()
