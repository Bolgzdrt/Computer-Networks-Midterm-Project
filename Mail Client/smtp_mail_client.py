import smtplib
import ssl

port = 465      # gmail's SSL port for their SMTP server

# sender email credentials
from_email = "compnettest345@gmail.com"
password = "f#%$7bx%1RLd"

to_email = "robbob345@gmail.com"
email_body = """\
Subject: This was sent using python

Hello,

This is the first assignment option on Computer Networks Midterm 2.

-Robert"""

# returns object with settings for server authentication using SSl, necessary
# for gmail SMTP connection
context = ssl.create_default_context()

# with statement ensures socket is destroyed after completion of internal statements
# SMTP_SSL encapsulates an SMTP connection, which uses TCP, with the settings necessary for SSL
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(from_email, password)      # uses sender credentials to establish connection to SMTP server
    server.sendmail(from_email, to_email, email_body)       # sends the email