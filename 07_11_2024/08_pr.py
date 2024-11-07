f = open('poems.txt')
t = f.read()
if 'little' in t:
    print("little is present")
else:
        print("little is not present")