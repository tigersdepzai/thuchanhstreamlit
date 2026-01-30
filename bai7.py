dictionaryorder_status = ("menu gồm, tra_sua , matcha_lotte, cr7, messi, to_ngo_khong_xao_muoi_ot,...")
print("Danh sách các món trà sữa:")
print(dictionaryorder_status)  
print("Vui lòng nhập tên món trà sữa bạn muốn đặt hàng:")
order = input()
while check_order_status():
    if order.lower() in dictionaryorder_status.lower():
        print(f"Bạn đã đặt hàng thành công món: {order}")
    else:
        print("Xin lỗi, món này không có trong menu.")
    check_order_status = lambda: input("Bạn có muốn tiếp tục đặt hàng? (có/không): ").strip().lower() == "có"
    