import random
def format_chengyu(sentences):
    print("running")
    sentences = sentences.split("\n\n")
    ciyus = []
    hypys = []
    zaojus = []
    meanings = []
    for part in sentences:
        if part:
            ciyu = part[max(part.find("．")+1, part.find(".")+1):max(part.find("("),part.find("（"))].strip()
            ciyus.append(ciyu)
            hypy = part[max(part.find("("),part.find("（"))+1:max(part.find(")"),part.find("）"))]
            hypys.append(hypy)
            zaoju = part[part.find("例")+1:part[part.find("例")+1:].find("\n")]
            zaojus.append(zaoju[1:])
            meaning = part[part.find("解释"):part.find("\n例")]
            meanings.append(meaning)

    with open("hypy.txt", "a", encoding='utf-8') as f1:
        for line in hypys:
            f1.write(line + "\n")

ciyus, hypys, zaojus, meanings = [], [], [], []
chosenNums = []
wrongWords = {}
correctWords = []
correctTimes = 0
points = 0
exited = False
while not exited:
    points = 0
    answersLst = []
    wordLst = []
    zaojuWordLst = []
    zaojusLst = []
    chosenNums = []
    print("Welcome to the Chinese Revision chatbot :O")
    level = input("Pick a level of Chinese (Sec 1 to 4): ").strip()
    while level not in ["1", "2", "3", "4"]:
        level = input("Invalid! Try again. Pick a level of Chinese (Sec 1 to 4): ")
    with open(f"sec{level}/ciyu.txt", encoding='utf-8') as f : ciyus = f.read().split('\n')
    with open(f"sec{level}/hypy.txt", encoding='utf-8') as f : hypys = f.read().split('\n')
    with open(f"sec{level}/zaoju.txt", encoding='utf-8') as f : zaojus = f.read().split('\n')
    with open(f"sec{level}/meanings.txt", encoding='utf-8') as f : meanings = f.read().split('\n')
    print("""
This chatbot has various functions:
1) Generate 选词填空 
Desc: Set the words you want to test, how many you want to test and then a 选词填空 will be generated for you to try.
    
2) Dictionary
Desc: After selecting this function, you can ask for any word in any topic and find out the meaning and zaoju for it :D 
    
3) Flashcards 
Desc: Set the words you want to test and a random ciyu will be given. Spend some time formulating a paragraph of what it means and a zaoju for it. We will then show you a proper one afterwards.

4) Word List
Desc: After selecting this function, you can ask for any series of words and the list of ciyus will be printed.
          
5) 汉语拼音
Desc: Given a 汉语拼音, write out the word yourself (on a piece of paper), and check after
""")
    func = input("What function do you want to pick? (1/2/3/4/5): ")
    while len(func) != 1 or func not in "12345":
        print("Invalid. Try again!")
        func = input("What function do you want to pick? (1/2/3/4/5): ")

    limitText = {
        "1": """""",
        "2": """""",
        "3": """
A) Sec 3 单元一----林黛玉进贾府 (0-11)
B) Sec 3 单元二----吃茶喝茶品茶 (12-25)
C) Sec 3 单元二----喜怒衰乐与健康 (26-36)
D) Sec 3 单元三----远亲不如近邻 (37-48)
E) Sec 3 单元三----老吾老以及人之老 (49-59)
F) Sec 3 成语 part 1 (60-119)
G) Sec 3 单元四----沟通面面观 (120-131)
H) Sec 3 单元四----出言有尺 交往有度 (132-143)
I) Sec 3 单元五----学然后知不足 (144-156)
J) Sec 3 单元五----学然后知不足 (157-167)
K) Sec 3 成语 part 2 (168-197)               
""",
        "4": """
A) Sec 4 单元二---敬业乐业（0-9）
"""
    }
    if func == "1" or func == "3" or func == "4" or func == "5":
        limits = input("In one string together, with spaces, set the lower bound and upper bound\n" + limitText[level])
        lowBound = int(limits.split(" ")[0])
        highBound = int(limits.split(" ")[1])
        if func == "1" or func == "3":
            times = ""
            while type(times) == str:
                times = input(f"How many ciyus do you want to test? (limit:{highBound-lowBound}) You may type NA if you want to test all. ")
                if times == "NA":
                    times = highBound-lowBound
                elif times.isdigit():
                    times = int(times)

            wordLst = []
            zaojuWordLst = []
            zaojusLst = []
            for i in range(times):
                chosen = random.randint(lowBound, highBound)
                if len(chosenNums) == len(ciyus):
                    print('We appeared to have run out of ciyus!')
                    break
                while chosen in chosenNums:
                    chosen = random.randint(lowBound, highBound)
                chosenNums.append(chosen)
                wordLst.insert(random.randint(0, len(wordLst)), ciyus[chosen])
                zaojusLst.append(zaojus[chosen].replace(ciyus[chosen], "____"))

            if func == "1":
                for i in range(3):
                    while chosen in chosenNums:
                        chosen = random.randint(0, 197)
                    chosenNums.append(chosen)
                    wordLst.insert(random.randint(0, len(wordLst)), ciyus[chosen])

                print("These are your options.")
                print(wordLst)
                print()

                for i in range(0, len(zaojusLst)):
                    print(f"Q{i+1}. {zaojusLst[i]}\n")

                confirm = False
                answersLst = []
                while not confirm:
                    for i in range(0, len(zaojusLst)):
                        answersLst.append(str(i+1) + ": " + input(f"What is your answer for Q{i+1}?: "))
                    print("\nWould you like to lock in these answers?")
                    print("\n".join(answersLst))
                    check = input("Y to confirm.")
                    if check.upper() == "Y":
                        print("Alright!")
                        confirm = True
                    else:
                        print("Sure, let's go again!")
                        answersLst = []

                for i in range(len(answersLst)):
                    answersLst[i] = answersLst[i].split(": ")[1]
                    if answersLst[i].strip() == ciyus[chosenNums[i]]:
                        points += 1
                        print(f"You got Q{i+1} correct!")
                    else:
                        print(f"You got Q{i+1} wrong :C, the answer is {ciyus[chosenNums[i]]}")
                        print(f"The meaning of {ciyus[chosenNums[i]]} is {meanings[chosenNums[i]]}")
                    print(f'Original sentence is {zaojusLst[i].replace("____", "*" + ciyus[chosenNums[i]] + "*")}')
                    print()
                print("In conclusion..")
                print(f"You have gotten for some words, especially..")
                print(f"Overall, your score was {points}/{times}")
            else:
                for num in chosenNums:
                    print(f"词语：{ciyus[num]} {hypys[num]}")
                    input("What do you think is the 意思？")
                    input("Give a 造句：  ")
                    print()
                    print(f"The actual 意思：{meanings[num]}")
                    print(f"Proper example of a 造句：{zaojus[num]}")
                    print()
        elif func == "4": 
            for i in range(lowBound, highBound):
                print(f"词语：{ciyus[i]} {hypys[i]}")
                print(f"意思：{meanings[i]}")
                print(f"造句：{zaojus[i]}")
                input("")
        elif func == "5":
            chosenNums = []
            for i in range(lowBound, highBound):
                chosenNums.append(random.randint(lowBound, highBound-1))
                print(f"{hypys[chosenNums[-1]]}")
    else:
        exit2 = False
        while not exit2:
            chosenWord = input("Enter a valid 词语 to check the meaning of. Type 'X' to exit. ")
            while chosenWord not in ciyus:
                if chosenWord == "X":
                    exit2 = True
                    break
                print('Not in sec 3 syllabus.')
                chosenWord = input("Enter a valid 词语 to check the meaning of. Type 'X' to exit. ")
            print()
            if chosenWord == "X":
                break
            print(f"意思：{meanings[ciyus.find(chosenWord)]}")
            print(f"造句：{zaojus[ciyus.find(chosenWord)]}")
            exit2 = input("Would you like to continue using the dictionary? (Y/N) ").upper() == "N"