class GameEntry:
    total_player = 0

    def __init__(self, name, score, timeq):
        self.name = name
        self.score = score
        self.time = timeq
        
        GameEntry.total_player += 1
    
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setScore(self, score):
        self.score = score
    
    def getScore(self):
        return self.score

    def setTime(self, timeq):
        self.time = timeq

    def getTime(self):
        return self.time

    def getTotal():
        return GameEntry.total_player

class ScoreBoard:

    def __init__(self, capacity):
        self.capacity = capacity
        self.board = [None] * self.capacity
        self.n = 0 
    
    def getCapacity(self):
        return self.capacity

    def sumEntries(self):
        return self.n

    def addItem(self, entry):
        score = entry.getScore()

        condition = len(self.board) > self.n or score > self.board[self.capacity - 1].getScore()
   

        if condition:
            if self.n < self.capacity:
                self.n += 1

            j = self.n - 1

            while j > 0 and self.board[j-1].getScore() < score:
                self.board[j] = self.board[j-1]
                j -= 1
            self.board[j] = entry
            print(f"Entri {score} ditambahkan!")

    def listEntries(self):
        for i in range (0, self.n):
            print(i+1,":", getattr(self.board[i], 'name'), getattr(self.board[i], 'score'))

# player1 = GameEntry("Farid", 89, 5)
# player2 = GameEntry("Alika", 96, 5)
# player3 = GameEntry("Tono", 86, 5)

board = ScoreBoard(10)
# board.addItem(player1)
# board.addItem(player2)
# board.addItem(player3)

active = True

while active:
    print("")
    start = input("Opsi: \n 1 = Tambahkan Entry Baru \n 2 = Tampilkan List ScoreBoard \n 3 = Keluar \n")
    print("")
    if start == '2':
        board.listEntries()
    elif start == '1':
        name = input("input nama pemain ")
        skor = int(input("input skor "))
        waktu = int(input("input waktu "))

        in_score = GameEntry(name, skor, waktu)
        set_board = board.addItem(in_score)

        print(f"Entri baru ditambahkan: {in_score.getName()} {in_score.getScore()} {in_score.getTime()}")
    else:
        break
