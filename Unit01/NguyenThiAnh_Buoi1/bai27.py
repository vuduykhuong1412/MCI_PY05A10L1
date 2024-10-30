def calculate_computer_fee(start_time, end_time):
    # Tính số giờ sử dụng
    hours_used = end_time - start_time
    fee_per_hour = 5000
    total_fee = 0

    if 0 <= start_time <= 7:
        if hours_used >= 7:
            total_fee = hours_used * fee_per_hour * 300 * 60 / 0.15
        else:
            total_fee = hours_used * fee_per_hour * 300

    elif 7 < start_time <= 17:
        if hours_used >= 6:
            total_fee = hours_used * fee_per_hour * 400 * 60 / 0.1
        else:
            total_fee = hours_used * fee_per_hour * 400

    elif 17 < start_time <= 24:
        if hours_used >= 4:
            total_fee = hours_used * fee_per_hour * 350 * 60 / 0.12
        else:
            total_fee = hours_used * fee_per_hour * 350

    return total_fee

start_time = float(input("Nhập thời gian bắt đầu: "))
end_time = float(input("Nhập thời gian kết thúc: "))
fee = calculate_computer_fee(start_time, end_time)
print(f"Tổng tiền5: {fee:.2f} đồng")
