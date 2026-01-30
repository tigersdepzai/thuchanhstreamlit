class student:
    name = ""
    score = 0
    def display(self):
        print("name:", self.name)
        print("score:", self.score)
diemtrungbinh = ""
s1 = student()
s1.name = "trọng"   




class student:   
  def __init__(self, ten, diem):
     self.ten = ten     # thụt lề hơi lệch
     self.diem = diem

  def xuat(self):   # tên hàm đơn giản
    print("Ten:", self.ten)
    print("Diem:", self.diem)



hs1 = student("Trong", 9)
hs2 = student("tâm", 8)
hs3 = student("long", 7)

dslop = [hs1, hs2, hs3]   

tongdiem = 0
for h in dslop:
  tongdiem = tongdiem + h.diem

diemTb = tongdiem / len(dslop)

print("=== Danh sach hoc sinh ===")
for hocs in dslop:
  hocs.xuat()

print("Diem trung binh la:", diemTb)
