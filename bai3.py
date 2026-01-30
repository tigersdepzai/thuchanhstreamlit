print("sau đây là một số số điện thoại trong danh bạ của bạn")
phone_numbers = {
    "mẹ": "0914120353",                                                                   "bố":"0918132006"}
print(phone_numbers)
ask = input("bạn muốn gọi cho số điện thoại của ai? ")
if ask in phone_numbers:
    print(f"Số điện thoại của {ask} là: {phone_numbers[ask]}")
else:
    print("Số điện thoại không có trong danh bạ của bạn.")
