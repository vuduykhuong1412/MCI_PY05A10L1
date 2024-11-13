principal = 400
monthly_payment = 10
interest_rate = 0.1
months_in_year = 12

for month in range(1,months_in_year + 1):
    principal -= monthly_payment
    if principal <= 0:
        break
if principal > 0:
    while principal >0:
        monthly_interest = (principal * interest_rate) / months_in_year
        principal += monthly_interest
        principal -= monthly_payment
print(f"Người vay sẽ trả hết khoản nợ sau {month} tháng")   # Cú pháp chung của f-string là: f"chuỗi văn bản {biểu thức} chuỗi văn bản"
        