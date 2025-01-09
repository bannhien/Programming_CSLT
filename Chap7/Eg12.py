# Đoạn văn bản ban đầu
text = """--Người---đâu-gặp---gỡ-làm-chi---
Trăm----năm-biết-có---duyên---gì--hay--không.
Ngổn-ngang---trăm-mối---bên---lòng----
----Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình."""

# Xử lý văn bản
def process_text(text):
    # Loại bỏ các dấu gạch ngang
    cleaned_text = text.replace("-", "")
    
    # Xóa các khoảng trắng dư thừa ở đầu và cuối đoạn văn
    cleaned_text = cleaned_text.strip()
    
    
    # Thêm khoảng trắng sau mỗi dấu chấm kết thúc câu
    cleaned_text = cleaned_text.replace(".", ". ")
    
    # Loại bỏ khoảng trắng dư thừa (nếu có) và thêm dòng mới sau mỗi dấu chấm
    lines = [line.strip() for line in cleaned_text.split(". ")]
    result = "\n".join(lines)
    
    return result

# Gọi hàm xử lý và in kết quả
processed_text = process_text(text)
print(processed_text)
