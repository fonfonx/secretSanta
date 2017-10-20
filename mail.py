# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(from_addr, to_addr_list, cc_addr_list, subject, message, login, password, smtpserver='smtp.gmail.com:587'):
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)

    msg = MIMEMultipart()

    msg['From'] = from_addr
    msg['To'] = ','.join(to_addr_list)
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'html'))

    server.send_message(msg)


def create_msg_html(dest, recv):
    html = """\
        <html>
        <head></head>
        <body>
            <p>Bonjour {:s},</p>
            <p>
                On organise un Secret Santa pour Noël cette année.
                Tu dois donc faire un cadeau à <b>{:s}</b>! Celui-ci doit être d'une valeur de moins de 20€.
            </p>
            <p>A bientôt en Bretagne!</p>
            <p>Le Père Noël</p>
        </body>
        </html>
        """
    return html.format(dest, recv)
