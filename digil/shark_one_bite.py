import os,random

class Shark:
    
    def __init__(self):
        self.patience = random.randint(8,15) * 10
        self.dot_damage = False

    def touch(self):
        cur = self.patience
        ran = random.randint(1,3)
        self.patience = cur + ran
        print(f"[+] 쓰다듬으로 인해 +{ran}이 됩니다.")

    def hug(self):
        # 10 이하 -2 /20이하 -1 / 나머지 +2
        cur = self.patience
        if cur <= 20:
            self.patience = cur -2
            print(f"[-] 많이 안좋은 상태여서 -2가 됩니다.")
        elif cur <= 10:
            self.patience = cur -1
            print(f"[-] 안좋은 상태여서 -1이 됩니다.")
        else:
            self.patience = cur +2
            print(f"[+] 기분 좋은 상태여서 +2이 됩니다.")

    def punch(self):
        cur = self.patience
        self.patience = cur -3
        print(f"[-] 상습적인 펀치로 인해 -3됩니다.")

    def flight(self):
        cur = self.patience
        print(f"[*] 상어가 꿈을 이루고자 용기를 냈습니다.")
        print(f"[*] 다치거나 경험하거나 확률은 50%입니다.")
        
        ran = random.randint(1,100)
        if ran > 50:
            # 51 - 100
            print("[+] 고난 끝에 날아올랐습니다. 기분이 좋아져 +10됩니다.")
            self.patience = cur +10
        else:
            # 1 - 50
            print("[-] 도전하다가 자빠져서 다쳤습니다. -8됩니다.")
            self.patience = cur-8
    
    def Neko_sleep(self):
        cur = self.patience

        if self.dot_damage == False:
            self.dot_damage = True
            print(f"[-] Neko가 안고 있습니다, 도트뎀이 들어옵니다.")
            return

        if self.dot_damage:
            print(f"[!] 계속 Neko가 껴안고 있습니다. -1됩니다.")
            self.patience = cur - 1

    def eye_spear(self):
        cur = self.patience
        self.patience = cur -5
        print(f"[-] 주변사람에 습관적 눈찌르기로 -5됩니다.")


    def cook_shark(self):
        cur = self.patience
        self.patience = cur -20
        print(f"[-] 요리 당할뻔 하여 기분 나빠져 -20이 됩니다.")

    def rest(self):
        cur = self.patience
        self.patience = cur + 10
        self.dot_damage = False
        print(f"[+] 휴식을 취하여 +10, 상태이상 회복되었습니다.")

    
    # 인내심이 0 이하일떄 물는 이벤트
    def kwaang(self):
        with open("./mad_shark.txt") as g:
            lines = g.readlines()
            for line in lines:
                print(line)
        #print("형 뒤1질래요?")
        line_dijil()

def shark_title():
    title = '''
      _____ __ __   ____  ____   __  _  __ __  __ __  ___ ___ 
 / ___/|  |  | /    ||    \ |  |/ ]|  |  ||  |  ||   |   |
(   \_ |  |  ||  o  ||  D  )|  ' / |  |  ||  |  || _   _ |
 \__  ||  _  ||     ||    / |    \ |  ~  ||  |  ||  \_/  |
 /  \ ||  |  ||  _  ||    \ |     \|___, ||  :  ||   |   |
 \    ||  |  ||  |  ||  .  \|  .  ||     ||     ||   |   |
  \___||__|__||__|__||__|\_||__|\_||____/  \__,_||___|___|
                                                          
    '''
    print(title)

def line_draw():
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

def line_dijil():
    digil = '''
     ` `     `        `              `                `            ` `     ` `          ```     `  ``                  `                                    `      `                              
    `````````       ##`               `             ``###        ````     ```            `    ##```               `##`  `##                               ` ``   `                               
  ` ######### ``    ##`             `############`   `##`    ``  `###`     `#############     ##` `` `########`  ``##`` `##           `#######`    `     ``########` `               ``#``   `#`#
 ##############`    ##`             `##``        ``  `##`    ``###`##`     ``    `##          ##` ` ```   ` ##`` ``## ` `##``    ``####` `   `###``    ``##```` ``###`                ## `  `##  
````````````````    ##`             `##```           `##`      `  `##`         ``###          ##` `         ##`  ``##   `##       ##`          `###`    ` ``     ` ###`         ```   ##`  ``#`` 
 ````#######````######`             `##` `       ` ` `##`          ##`    ``   ###``## `  ``  ##` ` ``    ` ##`  ``##`  `##      `##          ` `##`            ` `##``         ` ###############
 ``##` ` ` `##`     ##`             `############# ` `##`          ##`     ``###     `###`    ##` ` ``########`  ``########     ``##``          `##              ###`           `    ##  `` ## ` 
` `##`   ```## `######`                      `     `` ##`          ##`     ``` `     ```     `##`    `##  ``` `  ``##   `##     ` `###`    `  `###``         ` ###`               ` ##```` ##``  
    `#######`  `   `##`         `  `################``##`          ##`       ` `################     `##``       ``##   `##         ``#########```           `##`                ############### 
    ```    ``````` ```          ` `       ##```````  `##`          ##`          ````````````` ##     `##``        `##   `##         ##  `  ` ` ##`           ```                 ` `##`   ##  `  
       ####``````##### `                  ##`        `##`          ##`          ````````````` ##    ``###############   `##         ##         ##`           `    ``              `##   ` ##     
     `##  ` ` `    `###`                  ##`        `##`          ##`       ` `################       ` `     `  `##   `##         ##         ##`           `##`                 `#`    `#`     
    ` ##`   `      `##` `                 ##`        `##`        `   ``        `##`             ` `              ``##   `##   ########################`      `##` `                `       ``    
        ############`                     ##`         ##`                    `  ################`` `            `````  ``## `                                                                    
'''
    print(digil)

# file open으로 구성
def shark_art():
    with open('./shark_body.txt') as f:
        lines = f.readlines()
        for line in lines:
            print(line)

def banner():
    shark_title()
    shark_art()

def print_memu():
    print("1. 상어 쓰다듬기") # +1-+3
    print("2. 상어 껴앉기") # -2 - +2
    print("3. 상어 펀치") # -1
    print("4. 상어 눈 찌르기")
    print("5. 상어 날다") # 확률 20% - +5 나머지 -3
    print("6. 네코sleep에 찌부됨") # 휴식 전까지 -1 누적
    print("7. 상어 Cook") # -10
    print("8. 휴식") # +10

# Main
Nek = Shark()

banner()
line_draw()
print("\n> 상어의 인내심을 시험해보세요. <\n")

round = 0
while(1):
    if Nek.patience < 0:
        print("< Shark is mad >")
        Nek.kwaang()
        break

    print("==== Action Memu ====")
    print_memu()
    print("=====================")
    print(f"Status : {Nek.patience}\n")
    print("=====================")
    enter = int(input("> "))

    if round != 0 and Nek.dot_damage==True:
        Nek.Neko_sleep()

    if enter == 1:
        Nek.touch()
    elif enter == 2:
        Nek.hug()
    elif enter == 3:
        Nek.punch()
    elif enter == 4:
        Nek.eye_spear()
    elif enter == 5:
        Nek.flight()
    elif enter == 6:
        Nek.Neko_sleep()
    elif enter == 7:
        Nek.cook_shark()
    elif enter == 8:
        Nek.rest()
    else:
        print(f"[!] 잘못된 선택지 입니다.")
    round += 1

    #os.system('cls') # 화면 정리

