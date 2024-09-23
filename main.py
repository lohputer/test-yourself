import random
def format_sentences(sentences):
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
    
text = """
221. 一暴十寒（yī pù shí hán）
解释：比喻学 习工作没有恒心，努力的时候少，懒惰的时候多。
例：成功靠的是毅力和恒心，像你这样一暴 十寒，怎么会有成就呢？ 

222．一视同仁（yī shì tóng rén）
解释：一样看待，仁爱。指平等对待，不加区别。
例：这个公司的老板对员工一视同仁，勤奋的职员都有机会获得升职。

223．一意孤行（yī yì gū xíng）
解释：固执地按照自己的心意做事，不听别人的意见，独断独行。
例：你应该认真考虑大家的意见，不应再这样一意孤行，蛮干下去。

224．一针见血（yī zhēn jiàn xuè）
解释：比喻说话简要，一下子就说中要害。
例：他的批评一针见血，切中小王的要害，令假公济私的小王很不安。

225．以卵击石（yǐ luǎn jī shí）
解释：拿蛋去打石头。比喻以弱敌强，自取灭亡。
例：他是我国羽毛球单打冠军，林教练派你去和他对阵，岂不是以卵击石？

226．以身作则（yǐ shēn zuò zé）
解释：用自己的实际行动做榜样。
例：他不但教育子女要养成看书的好习惯，而且以身作则，每天陪子女阅读书报。

227．以牙还牙（yǐ yá huán yá）
解释：别人用牙齿咬我，我也用牙齿咬他。比喻用对方使用的手段回击对方。
例：每次我做错事，他就得理不饶人；这次他做错了事，我决定以牙还牙，让他尝尝被欺负的滋味。

228．因材施教（yīn cái shī jiào）
解释：根据不同的对象或智力的高低而采取不同的教育方法。
例：校长要求每位老师能因材施教，使不同程度的学生都能发展他们最大的潜能。

229．饮水思源（yǐn shuǐ sī yuán）
解释：喝水时想到水源。比喻不忘本。
例：你能有今天的成就，应该饮水思源，感谢王老师的指导与帮助。

230．迎刃而解（yíng rèn ér jiě）
解释：比喻主要问题解决了，其他问题就容易办。也比喻问题顺利解决。
例：这个关键的难题一解决，其他问题也就迎刃而解了。

231．应接不暇（yìng jiē bù xiá）
解释：形容事情繁多，忙得不可开交，无法应付。
例：学校假期中，每天前来借书的学生很多，图书馆的工作人员忙得不可开交，应付不过来。

232．与虎谋皮（yǔ hǔ móu pí）
解释：比喻商量的事危害对方切身利益，绝对办不成。
例：这间店的生意越来越好，你想要店主转让，这简直是与虎谋皮！

233．与日俱增（yǔ rì jù zēng）
解释：形容随着时间不断增长。
例：随着服务质量的改善，那间餐馆的生意蒸蒸日上，营业额与日俱增。

234．缘木求鱼（yuán mù qiú yú）
解释：比喻方向或方法不对，不可能达到目的。
例：这孩子根本没有音乐天分，家长硬要他学音乐，简直是缘木求鱼，白费心机。

235．约法三章（yuē fǎ sān zhāng）
解释：指订立为大家所遵守的规章条款。
例：考试期间爸爸和我约法三章，不许我看电视连续剧。

236．再接再厉（zài jiē zài lì）
解释：比喻继续努力，毫不放松。
例：在进入半决赛后，陈教练鼓励全体球员再接再厉，争取进入大决赛。

237．真知灼见（zhēn zhī zhuó jiàn）
解释：正确而透彻的见解。
例：黄教授所发表的言论确实是真知灼见，深受学术界的赞誉。

238．蒸蒸日上（zhēng zhēng rì shàng）
解释：形容事业一天天向上发展。
例：我们伟大的祖国生机勃勃，蒸蒸日上。

239．执迷不悟（zhí mí bù wù）
解释：坚持错误而不觉悟。
例：尽管老师苦口婆心地劝他改过自新，但他仍执迷不悟。

240．纸上谈兵（zhǐ shàng tán bīng）
解释：比喻空谈理论，不能解决实际问题。
例：理论不能联系实际，只会纸上谈兵，是不可能成功的。

241．志同道合（zhì tóng dào hé）
解释：志向相同，意见一致。形容有共同的理想和目标。
例：我和小华自小相识，兴趣爱好一致，是志同道合的好朋友。

242．志在四方（zhì zài sì fāng）
解释：形容有远大的志向和抱负。
例：男儿志在四方，将来有机会我要到国外去发展事业。

243．州官放火（zhōu guān fàng huǒ）
解释：比喻在上的人可以胡作非为，而普通人却受到限制。
例：经理不许职员把任何过期的旧报纸带回家，自己却每天把当天的报纸带走，真是只许州官放火，不许百姓点灯。

244．装聋作哑（zhuāng lóng zuò yǎ）
解释：指故意不理睬，只当不知道。
例：对社会上的不良风气，不能装聋作哑，不闻不问。

245．自暴自弃（zì bào zì qì）
解释：自己瞧不起自己，甘于落后或堕落。
例：虽然这次比赛失败了，但我们不能自暴自弃，要继续努力，争取下次赢回来。

246．自食其力（zì shí qí lì）
解释：依靠自己的劳动所得来生活。
例：年轻人要自食其力，总想着依靠父母是不会有出息的。

247．自投罗网（zì tóu luó wǎng）
解释：自己主动钻入对方布下的陷阱，也指自取祸害。
例：这名毒犯有眼无珠，竟然向警方兜售毒品，真是自投罗网。

248．自相矛盾（zì xiāng máo dùn）
解释：比喻语言、行动前后不一致或互相抵触。
例：将军原本主张抵抗到底，现在却又主张同敌人讲和，真是自相矛盾。

249．作壁上观（zuò bì shàng guān）
解释：比喻站在一旁看着，不动手帮助。
例：他看到别人有困难，总是作壁上观，从来也不会伸出援手。

250．坐享其成（zuò xiǎng qí chéng）
解释：自己不出力而享受别人取得的成果。
例：李经理从没出过力，计划完成后他却坐享其成，将功劳归于自己，大家都感到愤愤不平。
"""
format_sentences(text)
with open("ciyu.txt", encoding='utf-8') as f : ciyus = f.read().split('\n')
with open("hypy.txt", encoding='utf-8') as f : hypys = f.read().split('\n')
with open("zaoju.txt", encoding='utf-8') as f : zaojus = f.read().split('\n')
with open("meanings.txt", encoding='utf-8') as f : meanings = f.read().split('\n')
chosenNums = []
wrongWords = {}
correctWords = []
correctStreak = 0
correctTimes = 0
points = 0
i = 0
print("Before we start, let's set some limits..")
limits = input("""
In one string together, with spaces, set the lower bound and upper bound
A) 单元一----林黛玉进贾府 (0-11)
B) 单元二----吃茶喝茶品茶 (12-25)
C) 单元二----喜怒衰乐与健康 (26-36)
D) 单元三----远亲不如近邻 (37-48)
E) 单元三----老吾老以及人之老 (49-59)
F) 成语 part 1 (60-119)
G) 单元四----沟通面面观 (120-131)
H) 单元四----出言有尺 交往有度 (132-143)
I) 单元五----学然后知不足 (144-156)
J) 单元五----学然后知不足 (157-167)
K) 成语 part 2 (168-197)
""")
lowBound = int(limits.split(" ")[0])
highBound = int(limits.split(" ")[1])
print(lowBound, highBound)
while i < 50:
    if len(chosenNums) >= highBound-lowBound:
        print("OOPS RAN OUT")
        break
    chosen = random.randint(lowBound, highBound)
    while chosen in chosenNums:
        chosen = random.randint(lowBound, highBound)
    chosenNums.append(chosen)
    ans = input(f"{i+1}. {ciyus[chosen]}\nGive answer: ")
    if ans != ciyus[chosen]:
        correctTimes = 0
        points -= 1
        print(f'Wrong!')
        if ciyus[chosen] not in wrongWords:
            wrongWords[ciyus[chosen]] = 0
        else:
            wrongWords[ciyus[chosen]] += 1
        print(f"Do you at least know the meaning of the word?")
        input("Enter the meaning in your interpretation: ")
        print(meanings[chosen])
        match = input("Did it match with the above meaning? Y/N: ")
        if match == "N":
            print(f"Dang :(")
            points -= 1
        else:
            print("Oh yay!")
        chosenNums.pop()
        input("Okay how bout try come up with a SENTENCE with it? ")
        print(zaojus[chosen])
        match = input("Is the sentence good AND proper? ")
        if match == "N":
            print(f"Dang :(")
            points -= 1
        else:
            print("Oh yay!")
        if i >= 5:
            i -= 5
        else:
            i = 0
    else:
        points += 3
        print("Great!")
        print(f"Do YOU know the meaning of the word?")
        input("Enter the meaning in your interpretation: ")
        print(meanings[chosen])
        match = input("Did it match with the above meaning? Y/N: ")
        if match == "N":
            print(f"Dang :(.")
            points -= 1
        else:
            print("Oh yay!")
        correctWords.append(ans)
        correctTimes += 1
        input("Okay how bout try come up with a SENTENCE with it? ")
        print(zaojus[chosen])
        match = input("Is the sentence good AND proper? ")
        if match == "N":
            print(f"Dang :(")
            points -= 1
        else:
            print("Oh yay!")
        i += 1
    correctStreak = max(correctStreak, correctTimes)
print("In conclusion..")
print(f"You have gotten for some words, especially..")
print(" Wrong Attempts | Word ")
for word in wrongWords:
    print(f" {wrongWords[word]} | {word}")
print(f"You managed to maintain a streak of correct answers, at around {correctStreak} answers correct in a row.")
print(f"Overall, your score was {points}")
if points >= 50:
    print("This is A+ grade")
elif points >= 40:
    print("This is A grade")
elif points >= 30:
    print("This is B grade")
elif points >= 15:
    print("This is C grade")
elif points >= 0:
    print("This is D grade")
else:
    print("This is F grade")