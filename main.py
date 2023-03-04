# Kurbağa sınıfı oluşturun
class Kurbaga:
    def __init__(self):
        self.konum = [0, 0]  # kurbağanın başlangıç konumu
        self.yemek = [7, 7]  # yemeğin konumu

    def yemek_ye(self):
        if self.konum == self.yemek:
            print("Yemek yeyildi!")
        else:
            print("Yemek hele tapılmayıb.")

    def hareket_et(self, x, y):
        self.konum[0] += x
        self.konum[1] += y
        if self.konum[0] < 0:
            self.konum[0] = 0
        elif self.konum[0] > 7:
            self.konum[0] = 7
        if self.konum[1] < 0:
            self.konum[1] = 0
        elif self.konum[1] > 7:
            self.konum[1] = 7


# Kurbağa ve tahta oluşturun
qurbaga = Kurbaga()
tahta = [[0 for i in range(8)] for j in range(8)]

# Yemek ve kurbağanın konumunu tahtada işaretleyin
tahta[qurbaga.yemek[0]][qurbaga.yemek[1]] = "Y"
tahta[qurbaga.konum[0]][qurbaga.konum[1]] = "K"

# Tahtayı yazdırın
for i in range(8):
    for j in range(8):
        print(tahta[i][j], end=" ")
    print()

# Kurbağanın yemeğe gitmesi
while qurbaga.konum != qurbaga.yemek:
    x_hareketi = int(input("X koordinatında neçə xana ilərləmək istəyirsiniz? "))
    y_hareketi = int(input("Y koordinatında neçə xana ilərləmək istəyirsiniz? "))
    qurbaga.hareket_et(x_hareketi, y_hareketi)
    tahta = [[0 for i in range(8)] for j in range(8)]
    tahta[qurbaga.yemek[0]][qurbaga.yemek[1]] = "Y"
    tahta[qurbaga.konum[0]][qurbaga.konum[1]] = "K"
    for i in range(8):
        for j in range(8):
            print(tahta[i][j], end=" ")
        print()

# Yemek yendi mesajı yazdırın
qurbaga.yemek_ye()
