import random as r
class Game:
    def __init__(self):
        self.wins=0
        self.losses=0
        self.ties=0
        self.options={'rock':0,'paper':1,'scissor':2}

    def choices(self):
        return r.choice(list(self.options.keys()))
    def print(self):
        print(f"yo have {self.wins} wins, {self.losses} loses and {self.ties} ties")

    def winner(self,player,oponent):
        result= (player-oponent)%3
        if result ==0:
            self.ties+=1
            print("you guys are tie")
        elif result==1:
            self.wins +=1
            print("you win")
        elif result==2:
            self.losses +=1
            print("you loss")


    def on_game(self):
        while True:

            player_input = input("You have 3 options rock paper or scissor enter one among it\n")
            if player_input not in self.options.keys():
                print("invalid input try again")
            else:
                break

        oponent_choice = self.choices()

        print(f"you have entered {player_input} and oponeent entered {oponent_choice}")
        self.winner(self.options[player_input],self.options[oponent_choice])



if __name__ == "__main__":
    while True:
        game= Game()
        game.on_game()
        game.print()

        while True:
            cont =input("do you want to continue(y/n)?")
            if cont == 'y':
                break
            elif cont ==  'n':
                print("thank you")
                exit()
            else:
                print("invalid")
                continue




