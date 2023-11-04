import yagmail
import os

sender = os.getenv('email')
receiver = 'app7flask@gmail.com'

subject = """
This is the subject!
"""
contents = ["""
Here is the content of the email! 
Hi!
""", 'text.txt']

yag = yagmail.SMTP(user=sender, password=os.getenv('password')) # Set your own PASSWORD in Repl Secrets
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent!")
