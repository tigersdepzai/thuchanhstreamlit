def generate
    y = 0
    if x <=0:
        print("BYE")
        return False
    for i in range(x):
        y += i
    return y
print(generate(5))