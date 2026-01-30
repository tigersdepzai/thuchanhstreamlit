import random
contants = (("Số lượng câu hỏi",10),("số lượng bản cửu chương",5),("Điểm cho mỗi câu đúng",1))
leaderboard = []
def genarate_question():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    return(x , y, x * y)
def ask_question(question):
    x, y, answer = question
    print(f"{x} x {y} = ?")
    user_answer = input("Nhập câu trả lời của bạn: ")
    if user_answer.isdigit() and int(user_answer) == answer:
       print("Đúng rồi!") 
       return True
    else:
        print(f"Sai rồi! Đáp án đúng là:{answer}.")
        return False
def play_game():
    print("=====Game start=====")
    number_questions = contants[0][1]
    points_per_question = contants[2][1]
    questions = []
    for i in range(number_questions):
        q = genarate_question()
        questions.append(q)
    score = 0
    for q in questions:
        if ask_question(q):
            score += points_per_question
    print("==========================\n")
    print(f"Điểm của bạn là: {score}/{number_questions * points_per_question}")
    leaderboard.append((score,input("Nhập tên của bạn: ")))
    leaderboard.sort(reverse=True)
    print("=====Bảng xếp hạng=====")
    for i, score_entry in enumerate(leaderboard):
        print(f"{i + 1}. {score_entry[1]}: {score_entry[0]}")
    print("==========================\n")
while True:
    print("=====Menu=====")
    print("1. Chơi game")
    print("2. xem bảng xếp hạng")
    print("3. Thoát")
    print("==========================/n")
    choice = input("Nhập lựa chọn của bạn: ")
    if choice == "1":
        play_game()
    elif choice == "2":
        print("=====Bảng xếp hạng=====")
        for i, score_entry in enumerate(leaderboard):
            print(f"{i + 1}. {score_entry[1]}: {score_entry[0]}")
        print("==========================\n")
    elif choice == "3":
        print("Cảm ơn bạn đã chơi!")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")