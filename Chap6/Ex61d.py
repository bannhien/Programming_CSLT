MH = {}
while True:
    mathang = input()
    if mathang == "":
        break
    sl = int(input())
    MH[mathang] = sl
    
keys_to_delete = [key for key, value in MH.items() if value <= 10]
for key in keys_to_delete:
    del MH[key]
print(MH)