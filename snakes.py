followers = open("followers.txt").readlines()
following = open("following.txt").readlines()

for i in following:
    if not (i in followers):
        print(i.strip(),following.index(i))
