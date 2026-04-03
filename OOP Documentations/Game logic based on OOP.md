import random
# User input and Usage of Py.library
battle = random.choice(["Ponyta","Nidoran","Tododile"])
crit = random.choice(["Critical Hit!","no Crits"])
name = input("Enter Trainer name:")
# OOP logic-
class Pokemon:
    def __init__(self,pokemon,trainer,move,moves):
        self.pokemon = pokemon
        self.trainer = trainer
        self.move = move
        self.moves = moves
        self.hp = 30
        self.trainer_hp = 40
        self.battle = random.choice(["Ponyta","Nidoran","Tododile"])
        
    def Display_stats(self):
        print(f"A wild {battle} appeared")
        while True:
            ask = int(input(f"{self.trainer} what are going to do with your {self.pokemon} 1){self.move} 2){self.moves}?:"))
            if ask == 1:
                print("Super Effective!")
                self.hp -= 15
            else:
                print("Its Not very effective")
                self.hp -= 5
            print("The wild nidoran is going Rogue it attacked you")
            self.hp -= 10
            print(self.hp)
            print(self.trainer_hp)
            if self.hp <= 0:
                print(f"{battle} fainted {self.trainer} WINS")
                break
            else:
                continue

            
            
p1 = Pokemon("Mightyena",name,"Earthquake","Psychic")
p1.Display_stats()

            
            
        
