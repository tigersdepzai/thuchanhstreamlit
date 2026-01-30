number_of_player =  int(input("nhập số lượng người chơi người chơi:"))
arr = []
for i in range(number_of_player):
    name = input("nhập tên người chơi: ")
    score = int(input("nhập điểm của người chơi: "))
    arr.append((name, score))
for name ,score in arr:
    print(f"Tên người chơi: {name}, Điểm: {score}")
def buble_sort_dict(data , key , accending=True):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            a = data[j][key]
            b = data[i][key]
            if (a > b and accending) or (a < b and not accending):
                data[i], data[j] = data[j], data[i]
    return data
    
            

    

