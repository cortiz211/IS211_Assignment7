#Code referenced from http://www.cs.columbia.edu/~cannon/1006/lecture11.html

class Pig:
    def __init__(self, play1, play2):
        self.die = Die()
        self.p1 = Player('Player 1', play1)
        self.p2 = Player('Player 2', play2)

    def game(self):
        while (self.p1.score < 100 and self.p2.score < 100):
            self.p1.play1()
            if self.p1.score < 100:
                self.p2.play2()
        if (self.p1.score > self.p2.score):
            print('Player 1 has won! Good bye!')
            quit()
        else:
            print('Player 2 has won! Good bye!')
            quit()

class Die:
    def __init__(self,num=6):
        self.sides = num
        self.roll()

    def roll(self):
        self.face = int(random.random()*self.sides+1)

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.die = Die(6)

    def play1(self):
        round_score = 0
        roll = 'r'

        while roll == 'r':
            self.die.toss()
            toss = self.die.face
            if toss == 1:
                print(f'{self.name} rolled a 1')
                round_score = 0
                roll = 'h'
            else:
                print(f'{self.name} rolled a {toss}.')
                round_score = round_score+roll
                print(f"{self.name}'s round score is {round_score}.")
                roll = input('Roll or hold? (choose r/h)')
        self.score += round_score
        print(f"{self.name}'s turn is over.")
        print(f"{self.name}'s total score is {self.score}")

    def play2(self):
        round_score = 0
        roll = 'r'

        while roll == 'r':
            self.die.toss()
            toss = self.die.face
            if toss == 1:
                print(f'{self.name} rolled a 1')
                round_score = 0
                roll = 'h'
            else:
                print(f'{self.name} rolled a {toss}.')
                round_score = round_score + roll
                print(f"{self.p2}'s round score is {round_score}.")
                roll = input('Roll or hold? (choose r/h)')
        self.score += round_score
        print(f"{self.name}'s turn is over.")
        print(f"{self.name}'s total score is {self.score}")

def main():
    print("Starting up a game of Pig! Player1 goes first!")
    game = Pig()
    game.play()

if __name__ == "__main__":
    main()
