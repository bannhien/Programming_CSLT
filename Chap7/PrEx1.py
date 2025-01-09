input_st=input()
char_indices={}
for index, char in enumerate(input_st):
    if char not in char_indices:
        char_indices[char]=[]
        
char_indices[char_indices].append(index)

for char in "abcdefghijklmnopqrstuvwxyz":
    if char in char_indices:
        print(f"{char_indices[char]}")
    else:
        print("None")