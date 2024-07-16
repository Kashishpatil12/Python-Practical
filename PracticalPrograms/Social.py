fb = {"kashish","siddhi","rani","krisha","foram","hetvi","hetal","jigisha","himani","bharti"}
insta = {"krisha","nitina","bharti","kashish","hetal","megha","riya","priya","hetakshi","shruti"}
snap = {"khushi","devu","rani","gopi","kashish","nikita","hetvi","urvi","krisha","sonakshi"}

s1 = fb.intersection(insta)
s2 = s1.intersection(snap)

s3 = s1.difference(snap)
print(s3)

s4 = fb.intersection(snap)
s5 = s4.difference(insta)
print(s5)


s6 = fb.difference(insta)
s7 = s6.difference(snap)
print(s7)

print(s2)

s8 = insta.issubset(fb)
print(s8)