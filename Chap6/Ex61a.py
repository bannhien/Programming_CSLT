MH = {}
while True:
    mathang = input()
    if mathang == "":
        break
    sl = int(input())
    MH[mathang] = sl
max_sl_key = max(MH, key=MH.get)
min_sl_key = min(MH, key=MH.get)
max_sl_value = MH[max_sl_key]
min_sl_value = MH[min_sl_key]
print(min_sl_value)
print(max_sl_value)
