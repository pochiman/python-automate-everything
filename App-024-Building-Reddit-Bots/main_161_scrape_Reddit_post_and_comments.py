import praw

reddit = praw.Reddit(user_agent=True, 
                     client_id="Bh58UAQxDFFqyXNYxgDsRw", 
                     client_secret="eu8i1-bBszBEVkTb8m8T3vruuWP4Ug", 
                     username='automate-with-python', 
                     password='Tardam-socnid-nanzu3')

url = "https://www.reddit.com/r/cats/comments/qz201u/declawing_hurts_your_cat/"

post = reddit.submission(url=url)
print(post.title)
print(post.selftext)

print(len(post.comments))
for comment in post.comments:
    print(comment.body)
