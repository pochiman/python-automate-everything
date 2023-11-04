import yagmail
import os
import time

sender = os.getenv('email')
receiver = '2jjnkjca@10mail.tk'

subject = """
This is the subject!
"""
contents = """
Here is the content of the email! 
Hi!
"""
while True:
    yag = yagmail.SMTP(user=sender, password=os.getenv('password'))
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")
    time.sleep(60)
