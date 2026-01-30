f = open("tracnghiem.txt", encoding="utf-8")
print(f.read())
f.close()
print("theo bạn,tay to là gì ")
tay_to = input("")
if tay_to == "manh_me": # type: ignore
    print("bạn đã đoán đúng")
else:
    print("bạn đã đoán sai")

print("theo bạn,tay nhỏ là gì ")
tay_nho = input("")
if tay_nho == "kheo_leo": # type: ignore
    print("bạn đã đoán đúng")
else:
    print("bạn đã đoán sai")

print("theo bạn,chân_dài là gì ")
chan_dai = input("")
if chan_dai == "nhanh_nhen": # type: ignore
    print("bạn đã đoán đúng")
else:
    print("bạn đã đoán sai")

print("theo bạn,chân_ngắn là gì ")
chan_ngan = input("")
if chan_ngan == "kien_tri": # type: ignore
    print("bạn đã đoán đúng")
else:
    print("bạn đã đoán sai")

    

