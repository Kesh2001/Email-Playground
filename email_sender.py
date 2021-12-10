# server problem occurred
import smtplib  # allows us to create a server for this; 
# Simple Mail Transfer Protocol
from email.message import EmailMessage
from string import Template
from pathlib import Path # os.path is same
html = Template(Path('index.html').read_text())
email =  EmailMessage()
email['from'] = 'Keshav Anand'
email['to'] = 'roli.m75@gmail.com'
email['subject'] = 'Python Test'


email.set_content(html.substitute(name='TinTin'), 'html')
with smtplib.SMTP(host='smtp.gamil.com', port=587) as smtp:
	smtp.ehlo() # this is a server, m awake msg
	smtp.starttls() # connect to server securely
	smtp.login('anandkushagara@gmail.com', 'kesh@2001')
	smtp.send_message(email)
	print('All good!')