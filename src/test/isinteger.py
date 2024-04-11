def is_integer(s):
    try:
        int(s)  # Chuyển đổi chuỗi thành số nguyên
        return True
    except ValueError:
        return False

# Sử dụng hàm kiểm tra
print(is_integer(123))   # Output: True
print(is_integer("1abc"))   # Output: False
print(is_integer("12.3"))  # Output: False
