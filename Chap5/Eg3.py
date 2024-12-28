Names = []
while True:
    name1=input()
    if name1=="":
        break
    elif name1 not in Names:
        Names+=[name1]
print(Names)
    
