ngAm="AEIOUaeiou"

input_str=input().strip()

ngam_list=[]
phuam_list=[]

for char in input_str:
    if char.isalpha():
        if char in ngAm:
            ngam_list.append(char)
        else:
            phuam_list.append(char)
            
ngam_str=" ".join(ngam_list)
phuam_str=" ".join(phuam_list)
print(ngam_str)
print(phuam_str)