# Đoạn văn bản ban đầu
text=''' Người đâu gặp gỡ làm chi ,
Trăm năm biết có , duyên gì hay không ,
Ngổn ngang trăm mối bên lòng ,
, Nên câu tuyệt diệu ngụ trong tính tình .'''

# cleaned_text=text.replace(", ","")
# print(cleaned_text)
# print()
# cleaned_text = cleaned_text.strip()
# print(cleaned_text)
# print()
def XLC(cau):
    cau=cau.replace(",","")
    L=cau.split()
    cau=" ".join(L)
    print(cau)
    cau=cau.replace(" ,",",")
    print(cau)