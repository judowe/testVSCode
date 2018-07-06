import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 
fromaddr = "technik@uwnet.de"
toaddr = "it@ethnos360.de"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "!!!! WASSER im Serverraum !!!!"
 
body = "!!! Der Wassersensor im Serverraum meldet Wasser vorhanden !!!"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('mail.uwnet.de', 587)
server.starttls()
server.login(fromaddr, "WurstHans14")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()