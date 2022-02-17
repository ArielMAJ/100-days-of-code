mySocialMedia_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for n,post in enumerate(mySocialMedia_posts):
    try:
        # This is just a test. It would probably be better to use "post.get('Likes', 0)"
        print(n, end='--')
        total_likes = total_likes + post['Likes']
    except KeyError as msg:
        print(f"The post {post} doesn't have {msg}.", end='--')
        continue
    else:
        continue
    finally:
        # Checking if finally really is executed before continuing.
        print(n)



print("\n", total_likes, sep='')