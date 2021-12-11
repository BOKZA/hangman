import string
import random

class Player:
    def __init__(self, name, hp, damage, correct_alp):
        self.name = name
        self.hp = hp 
        self.damage = damage
        self.correct_alp = 0


class Game:

    def __init__(self):
        self.player = []
        self.user_character = ""
        self.remain_alp = list(string.ascii_uppercase) 
        self.cur_string = ["_"] * 10
        self.answer_string = ""

    def start_game(self):
        self.player.append(Player("김건웅", 50, 20, 0))
        self.player.append(Player("김현주", 70, 25, 0))
        self.player.append(Player("박진혁", 80, 30, 0))
        self.player.append(Player("유송경", 90, 35, 0))
        
        
        n = int(input("당신의 캐릭터 번호를 선택해주세요 (1,2,3,4) "))
        global user_character
        user_character = self.player[n-1]
        print("당신의 캐릭터는", user_character.name,"입니다.\n")
        
        
        global answer_string
        answer_string=""
        for i in range(10):
            answer_string += str(random.choice(string.ascii_uppercase))
        print("컴퓨터가 랜덤으로 만든 답입니다. 플레이어에게는 보이지 않습니다.", answer_string,"\n")
        
    def sort_data(self, i):        
       
        if i==1:
            self.player.sort(key = lambda x: x.name)             
        else:
            self.player.sort(key = lambda x: -x.hp)
      
    def play_game(self):
        print(
            f"게임은 {self.player[0].name},{self.player[1].name},{self.player[2].name},{self.player[3].name} 순으로 진행됩니다.\n")

        for i in range(3):

            if self.player[i] == self.user_character:
                print("***** 내 캐릭터 *****")
            else:
                print(f"\n***** {i+1} 캐릭터 *****")

            print(f"이름: {self.player[i].name} (HP: {self.player[i].name})")
            choice = input("선택알파벳: ")
            
            if choice not in self.cur_string:
                self.cur_string+=choice
            
            if(choice in answer_string):
                self.player[i].correct_alp += 1
                print("***** 맞았습니다 ᵔεᵔ  *****")
                for w in answer_string: 
                    if w in self.cur_string:
                        print(w, end=" ")
                    else:
                        print("_", end=" ")
                        succeed = False
                print("\n")
                
            else:
                print("***** 틀렸습니다 (ﾟ⊿ﾟ)  ******")
                self.player[i].hp -= self.player[i].damage
                print(self.player[i].name,"님은 틀렸기 떄문에 HP가 ", self.player[i].hp, "남았습니다.\n")
                
    def game_result(self):
        
        print("******************* 게임이 끝났습니다 *******************")
        print("=============================")
        print("     게임 순위 - 생명력")
        print("=============================")
        self.player.sort(key=lambda x:-x.hp )
        for i in range (4):
            if (self.player[i].hp>=0):
                print(i+1,"등: ", self.player[i].name," (HP:", self.player[i].hp,")")
            else:
                print(i+1,"등: ", self.player[i].name," (사망)")
                
        print("=============================")
        print(" 게임 순위 - 알파벳 맞춘 횟수")
        print("=============================")
        self.player.sort(key= lambda x:-x.correct_alp)
        for i in range (4):
            print(i+1,"등: ", self.player[i].name, self.player[i].correct_alp,"회")

        
    def game(self):

        self.start_game()

        print("******************* 게임 시작 *******************\n")

        for i in range(1, 4):
            print("===========================")
            print(f"     ROUND {i} - START")
            print("===========================")

            self.sort_data(i)
            self.play_game()

            print(f"===========================")
            print(f"     ROUND {i} - END")
            print("===========================")

        self.game_result()


if __name__ == '__main__':
    game = Game()
    game.game()