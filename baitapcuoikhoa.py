# Bài tập cuối khóa Python
# câu 1
number_of_player = int(input("Nhập số lượng học sinh: "))
import random
for n in range(number_of_player):
    ten = input("Nhập tên học sinh: ")
    diem_ne = random.randint(0, 10)
    print(f"Tên học sinh: {ten}, Điểm: {diem_ne}")
# câu 2
open_file = open("baitapcuoikhoa.py", "w")
open('diem.txt', 'r'encodeing='utf-8')
for n in range(number_of_player):
    ten = input("Nhập tên học sinh: ")
    diem_ne = random.randint(0, 10)
    open_file.write(f"Tên học sinh: {ten}, Điểm: {diem_ne}\n")
open_file.close()
# câu 3

# câu 4
def buble_sort_dict(data, key, accending=True):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            a = data[j][key]
            b = data[i][key]
            if (a > b and accending) or (a < b and not accending):
                data[i], data[j] = data[j], data[i]
    return data
# câu 5
def main():
    arr = []
    for i in range(number_of_player):
        name = input("Nhập tên người chơi: ")
        score = int(input("Nhập điểm của người chơi: "))
        arr.append((name, score))
    
    for name, score in arr:
        print(f"Tên người chơi: {name}, Điểm: {score}")
    
    sorted_arr = buble_sort_dict(arr, 1, accending=False)
    print("Danh sách người chơi sau khi sắp xếp theo điểm:")
    for name, score in sorted_arr:
        print(f"Tên người chơi: {name}, Điểm: {score}")







