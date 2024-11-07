words = ["donkey","kaddu","mote"]

with open("sample.txt") as f:
    content=f.read()
    for word in words:
     content = content.replace("words","@%^&*##")
    with open("sample.txt","w") as f:
         f.write(content)