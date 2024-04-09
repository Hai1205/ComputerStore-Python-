import re


def checkPhone(phone_number):
    pattern = r"^(0|\+84)[1-9]\d{8}$"
    if re.match(pattern, phone_number):
        return True
    else:
        return False
# phone_number = "0782748863"
# if checkPhone(phone_number):
#     print(f"Số điện thoại {phone_number} hợp lệ.")
# else:
#     print(f"Số điện thoại {phone_number} không hợp lệ.")


def checkPassword(password):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{6,}$"
        if re.match(pattern, password):
            return True
        else:
            return False
password = "0782748863Aa@"
if checkPassword(password):
    print(f"Mật khẩu hợp lệ.")
else:
    print(f"Mật khẩu không hợp lệ.")
