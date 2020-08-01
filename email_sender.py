import smtplib
from email.message import EmailMessage
from string import Template # Substituting text
from pathlib import Path # Allows you to access HTML file


html = Template(Path('index.html').read_text()) # read_text method to connect html
email = EmailMessage()
email['from'] = 'Huzaifah'
email['to'] = ['hm.196x@gmail.com']
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp: #Server
	smtp.ehlo()
	smtp.starttls() # TLS is an encryption mechanism - to connect securly to the server
	smtp.login('hm.196x@gmail.com', 'Python.7861')
	smtp.send_message(email)
	print('all good boss!')