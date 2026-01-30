tiền = int(input("Nhập số tiền bạn có: "))
if tiền <= 0:
    print("Số tiền không hợp lệ, vui lòng nhập lại.")
    exit()  


while True:
    print("1. show menu")
    print("2. mua trái cây")
    print("3. thoát")
    choice = int(input("Nhập lựa chọn của bạn: "))
    if choice == 1:
        print("Menu:")
        print("1. Mua táo")
        print("2. Mua chuối")
        print("3. Mua cam")
        print("4. Mua dưa hấu")
        print("5. Mua nho")
        print("                                                               ")
    elif choice == 2:
        trai_cay = input("Nhập tên trái cây bạn muốn mua: ")
        print(f"Bạn đã mua {trai_cay}.")
        print("                                                              )")
    elif choice == 3:
        print("Cảm ơn bạn đã sử dụng chương trình!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng thử lại.")
        print("                           (❁´◡`❁)                                  )")
