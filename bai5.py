def count_words(file_name):
    word_counts = {}
    f = open(file_name, 'r')
    text = f.read()
    words = text.split()
    for word in words:
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1
    return word_counts
file_name = input("Nhap ten file can kiem tra: ")
file_name = file_name(file_name)
for word, count in count_words(file_name).items():
    print(f"{word}: {count}")