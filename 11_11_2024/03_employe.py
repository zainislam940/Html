class Employe:
    company = "Google"

harry  = Employe()
zain = Employe()
print(harry.company)
print(zain.company)
Employe.company = "youtube"
print(harry.company)
print(zain.company)