import yagmail
import os

sender = os.getenv('email')
receiver = 'lebenjelostravels@gmail.com'

subject = "This is the subject!"


contents = """
Here is the content of the email! 
Hi!
"""

yag = yagmail.SMTP(user=sender, password=os.getenv('password'))
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent!")
