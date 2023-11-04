import yagmail
import os
import pandas

sender = os.getenv('email')

yag = yagmail.SMTP(user=sender, password=os.getenv('password')) # Set your own PASSWORD in Repl Secrets

df = pandas.read_csv('contacts.csv')

for index, row in df.iterrows():
    receiver_email = row['email']
    subject = "This is the subject!"
    contents = [f"""
    Hey, {row['name']} you have to pay {row['amount']}
    Bill is attached!""",
    row['filepath'], 
    ]
    yag.send(to=row['email'], subject=subject, contents=contents)
    print("Email Sent!")
