n=input()
a=n.find("Email")
b=n.find(":",a)
print(n[b+2:])