import smtplib
from email.message import EmailMessage
import ssl
import os
import imghdr

password2 = os.environ.get("PYTHON_GMAIL_PASSWORD")
print(password2)

from_addr= "henryclymerdev@gmail.com"
to_addr = "henryclymerdev@gmail.com"


subject = "New email (with attachement)"
body = """ Here is the test for my new email, this is just a test to see how it goes. Image attached
"""

em = EmailMessage()

em["From"] = from_addr
em['To'] = to_addr
em["Subject"] = subject
em.set_content(body)



###for sending images##

files = ["Catphoto.jpg","Catphoto2.jpg", "Catphoto3.jpg" ]

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    em.add_attachment(file_data, maintype="image", subtype= file_type, filename=file_name)
  
##for sending pdf###    
files = ["resume.pdf" ]

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    em.add_attachment(file_data, maintype="application", subtype= 'octet-stream', filename=file_name)

# context = ssl.create_default_context()

#to send to local host paste "python -m smtpd -c DebuggingServer -n localhost:1025" into command prompt


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
# with smtplib.SMTP('localhost', 1025) as smtp:
    smtp.login(from_addr, password2)
    smtp.send_message(em)
    

    