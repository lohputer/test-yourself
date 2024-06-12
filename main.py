import random
def format_sentences(sentences):
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
            zaojus.append(zaoju)
            meaning = part[part.find("解释"):part.find("\n例")]
            meanings.append(meaning)

    with open("meanings.txt", "a", encoding='utf-8') as f1:
        for line in meanings:
            f1.write(line + "\n")

text = """

161．三思而行 (sàn sī ér xíng)
解释：做事经过反复思考，然后再去做。
例：我们做事要三思而行，不可以冲动。

162．杀鸡取卵 (shā jī qǔ luǎn)
解释：为了得到鸡蛋就把鸡杀了。比喻为了眼前一点好处而损害长远利益。
例：为了有更多时间准备考试而减少睡眠及放弃运动，这简直是杀鸡取卵。
例：一些商人为了赚钱，把货品的价格提高了好几倍，这种做法无疑是杀鸡取卵。

163．伤天害理 (shāng tiān hài lǐ)
解释：形容做事极端残忍，没有人性，不顾天理。
例：他做出了伤天害理的事，当然得受到法律的制裁。

164．舍己为人 (shě jǐ wèi rén)
解释：为了帮助别人而牺牲自己的利益。
例：他不顾个人安危，冲进火场救人，这种舍己为人的精神令人敬佩。

165．实事求是（shí shì qiú shì）
解释：完全从实际情况出发，正确地处理问题。指务必要有事实为根据，以求得正确的结论。
例：解决问题必须实事求是，否则就会过于主观。

166．事半功倍（shì bàn gōng bèi）
解释：形容费力小而收效大。
例：自从工厂自动化后，生产就取得事半功倍之效。
例：事前有周密的计划，做起事来就能达到事半功倍的效果。

167．视死如归（shì sǐ rú guī）
解释：形容为了正义的事业而勇于牺牲自己的生命。
例：战士们视死如归，为保家卫国而英勇作战的精神值得我们学习。

168．守望相助（shǒu wàng xiāng zhù）
解释：指邻近各处彼此照应，互相帮助。
例：邻居之间若能守望相助，便可杜绝窃案的发生。

169．守株待兔（shǒu zhū dài tù）
解释：比喻坐等意外收获的侥幸心理。也比喻死守狭隘经验。
例：要成功就要努力，守株待兔将一事无成。


170．熟能生巧（shú néng shēng qiǎo）
解释：熟练了就有高超的技巧。
例：经过了多次的练习，他终于熟能生巧，把复杂的舞步练成了。

171．水到渠成（shuǐ dào qú chéng）
解释：水流到的地方自然成渠。比喻条件成熟，事情自然成功。
例：要成功创业，除了要有经济实力，也要配合适当的时机，才能水到渠成。
例：这个问题目前虽然没办法解决，但将来科技进步时，自然会水到渠成。

172．水落石出（shuǐ luò shí chū）
解释：水落下去，石头就露出来。比喻真相大白。
例：针对这起盗窃伤人案，警方已展开调查工作，相信不久便能水落石出了。

173．司空见惯（sī kōng jiàn guàn）
解释：表示看惯了就不觉得奇怪。
例：对于他这种古怪的行径，我们已经是司空见惯，见怪不怪了。

174．四面楚歌（sì miàn chǔ gē）
解释：比喻处在孤立无援、四面受敌的困境中。
例：在我军的强大攻势下，敌人陷入四面楚歌的境地，最后只能投降。
例：他的骄傲自大的态度，让他陷入四面楚歌的境地。

175. 损人利己（sǔn rén lì jǐ）
解释：使别人受到损失而使自己得到好处。
例：他为了达到目的而不择手段，做出损人利己的事来。

176. 螳臂当车（táng bì dāng chē）
解释：螳螂举起臂膀，想把车挡住。比喻不自量力。
例：凭你现在的经济实力，想与那家大公司竞争，简直就是螳臂当车。

177. 桃李满天下（táo lǐ mǎn tiān xià）
解释：比喻所教的学生众多。
例：陈老师教学三十年，春风化雨，桃李满天下。

178. 天渊之别（tiān yuān zhī bié）
解释：上天和深渊之间的差别，比喻差别极大。
例：他们虽是兄弟，但性格上却有着天渊之别，一个外向，另一个则内向。
例：你丰衣足食，他却捉襟见肘，你和他的处境有着天渊之别。

179. 挑拨离间（tiǎo bō lí jiàn）
解释：引起是非争端，使别人不合。
例：为了坐收渔人之利，他在竞争对手面前极尽挑拨离间之能事。
例：朋友之间要互相信任，不要让有心人挑拨离间。

180.铤而走险（tǐng ér zǒu xiǎn)
解释：因无路可走而采取冒险行动。
例：为了偿还债务，他竟铤而走险去贩卖毒品。

181.同甘共苦（tóng gān gòng kǔ）
解释：指共同享受幸福，共同担当艰苦。
例：他俩同甘共苦几十年，彼此间的感情十分深厚。
例：为了完成目标，我们一定要同甘共苦，奋斗到底！

182.同流合污（tóng liú hé wū）
解释：指跟坏人一起做坏事。也指思想言行与恶劣的风气混同。
例：我们不可和坏人同流合污，干尽坏事，令父母失望。

183. 同心协力（tóng xīn xié lì）
解释：心思一致，共同努力。
例：为了建设美好的家园，我们应该同心协力。

184. 同舟共济（tóng zhōu gòng jì)
解释：比喻在困难的环境中，同心协力，共同渡过难关。
例：在艰苦的环境里，只要大家同舟共济，就能克服一切困难。

185.徒劳无功（tú láo wú gōng）
解释：白费力气而没有成效。
例：他费尽心思去巴结上司，但上司并不欣赏他，真是徒劳无功。
例：做事方法不对，一切努力就会徒劳无功了！

186. 退避三舍（tuì bì sān shè）
解释：主动退让，回避九十里(mile)。后用以比喻对人退让和尊敬。
例：李阿姨好搬弄是非，邻居们都对她退避三舍。

187. 万古流芳（wàn gǔ liú fāng）
解释：万古：时间很长。芳：香，指美名。好名声永远流传，用以称颂人的德行。
例：岳飞精忠报国的事迹万古流芳，世代受人景仰。

188. 万事具备，只欠东风（wàn shì jù bèi，zhǐ qiàn dōng fēng）
解释：已为完成某一计划作了种种准备，但还差最后的关键条件。
例：计划书已经写好了，就等老板许可，即可动工了，正是万事具备，只欠东风。

189. 望尘莫及（wàng chén mò jí）
解释：形容在后头追赶，只望见尘土，却远远地落在后头。
例：他在学业和课外活动方面的优越表现让许多同学望尘莫及。

190. 忘恩负义（wàng ēn fù yì）
解释：指忘记别人对自己的好处，做出对不起别人的事。
例：我们做人应该饮水思源，绝对不能忘恩负义。

191. 危言耸听（wēi yán sǒng tīng）
解释：故意说惊人的话，使听的人吃惊、震动。
例：网上的一些信息，根本就是危言耸听，没有任何的根据，我们不应该转发。

192. 为非作歹（wéi fēi zuò dǎi）
解释：任意干各种各样坏事。
例：这些为非作歹的流氓，如今被绳之以法，真是大快人心。

193. 为虎作伥（wèi hǔ zuò chāng）
解释：充当老虎的伥鬼，即引诱人来给老虎吃。比喻做恶人的帮凶。
例：他欺善怕恶，为虎作伥的行为，被大家所不齿。
例：我们不可帮助坏人做坏事，否则就是为虎作伥，迟早会被绳之以法。

194. 未雨绸缪（wèi yǔ chóu móu）
解释：趁天还没有下雨，先把门窗绑牢。比喻事先做好准备工作。
例：对于未来，我们应该未雨绸缪，早做好准备。

195. 温故知新（wēn gù zhī xīn）
解释：复习过去的知识，才可有新的体会。
例：为了温故知新，他总是把读过的书本拿出来再读一遍。

196. 温文尔雅（wēn wén ěr yǎ）
解释：举止文雅，态度温和。
例：老板是一个温文尔雅的人，对人总是彬彬有礼。
例：她是一个温文尔雅的孩子，大家都喜欢与她为友。

197. 闻鸡起舞（wén jī qǐ wǔ）
解释：听到鸡啼就起床舞剑练武，比喻有志者及时奋发。后来比喻把握时机，及时奋起行动；抓紧时间，不懈努力。
例：为了加强写作能力，他每天闻鸡起舞，阅读报章、书刊。
例：如果我们有闻鸡起舞的精神，学业成绩一定不会太差的。

198. 卧薪尝胆（wò xīn cháng dǎn）
解释：薪：柴草。睡觉睡在柴草上，吃饭睡觉都尝一尝苦胆。形容人刻苦自励，发奋图强。
例：卧薪尝胆的故事告诉我们，做事一定要有坚定的意志力，不可轻易放弃！

199. 乌合之众（wū hé zhī zhòng）
解释：像乌鸦那样暂时聚合的一群，比喻临时杂凑起来，毫无组织纪律的一群人。
例：所谓的乌合之众，是指没有组织的一群人，即使聚在一起也是成不了大事的。

200. 乌烟瘴气（wū yān zhàng qì）
解释：比喻环境嘈杂、秩序混乱，风气很坏或社会黑暗。
例：部分同事在公司里勾心斗角、搬弄是非，搞得公司乌烟瘴气，实在要不得!

201. 无可厚非（wú kě hòu fēi）
解释：指不可过分指责。
例：他为了表达孝心便买了礼物送给父母，虽然花费了不少金钱，但也无可厚非。
例：年轻人有自己的审美倾向是无可厚非的，他们只是需要引导。

202. 无微不至（wú wēi bù zhì）
解释：没有一个细微的地方不照顾到，形容关怀得非常细心周到。
例：我们要感恩父母对我们的关怀和照顾是无微不至的。

203. 五体投地（wǔ tǐ tóu dì）
解释：指两手、两膝和头一起着地。这是古印度佛教一种最恭敬的行礼仪式。比喻佩服到了极点。
例：李同学在写作上的出色表现，让我们佩服得五体投地！

204. 相辅相成（xiāng fǔ xiāng chéng）
解释：互相协助、配合而促成。
例：学习和复习，是用以掌握和巩固知识的两个方面，相辅相成，缺一不可。

205. 心猿意马（xīn yuán yì mǎ）
解释：形容心思不专，变化无常，好像马跑猿跳一样，控制不住。
例：妈妈要我专心做功课，不要心猿意马，老想着玩电脑游戏。

206. 幸灾乐祸（xìng zāi lè huò）
解释：别人遭到灾祸时自己心里高兴。
例：邻居家发生不幸，你不但不去帮忙，反而幸灾乐祸，真是太不应该了。

207. 胸有成竹（xiōng yǒu chéng zhú）
解释：画竹子之前，心里已经有了竹子的全貌。比喻事前已经做好了全面考虑和安排，因而显得镇静而有把握。
例：经过全面的复习后，我对这次的考试便胸有成竹了！

208. 袖手旁观（xiù shǒu páng guān）
解释：比喻置身事外，不加过问或者不予帮忙。
例：我们是好朋友，在你需要帮助的时候，我绝不会袖手旁观。

209. 虚怀若谷（xū huái ruò gǔ）
解释：胸怀像山谷那样深而宽广，形容十分谦虚。
例：虽然林教授学识渊博，但仍然虚怀若谷，诚恳地听取不同的意见。

210. 悬崖勒马（xuán yá lè mǎ）
解释：比喻到了危险的边缘及时醒悟回头。
例：大家都劝他悬崖勒马，赶快回头，不要一错再错了。

211. 削足适履（xuē zú shì lǚ）
解释：脚大鞋小，把脚削小以适合鞋子的尺码。比喻没有原则地迁就或不顾具体条件地生搬硬套。
例：由于国情有所不同，我们不应生搬硬套他国所推行的政策，否则就是削足适履。
例：为了迎合读者的口味而去虚构内容，脱离自己所熟悉的生活环境写文章，这种削足适履的做法是不可取的。

212. 雪中送炭（xuě zhōng sòng tàn）
解释：雪天给人送炭取暖。比喻在别人急需的时候给予帮助。
例：朋友遇到困难，我们应该雪中送炭，不可以不闻不问。

213. 循循善诱（xún xún shàn yòu）
解释：指善于有步骤地引导或教育人。
例：在老师的循循善诱之下，同学们的成绩有了很大的进步。
例：何老师对学生不仅和蔼可亲，而且循循善诱，深受同学们的敬重。

214. 掩耳盗铃（yǎn ěr dào líng）
解释：比喻不能欺骗别人，只能欺骗自己。
例：掩耳盗铃是一种自欺欺人的行为，不可取。
例：有些银行职员利用工作便利进行贪污，掩耳盗铃，真是不应该。

215．夜郎自大（yè láng zì dà）
解释：比喻妄自尊大。
例：在和他人交往时，我们既不能卑躬屈膝，也不要夜郎自大。
例：自从他在比赛中夺得冠军后，便变得夜郎自大，目中无人了。

216．一败涂地（yī bài tú dì）
解释：―旦失败就肝脑涂染遍地，形容惨败，不可收拾。
例：在球赛中，我队失误连连，结果输得一败涂地。

217．一帆风顺（yī fān fēng shùn）
解释：船挂满帆，一路顺风行驶。比喻非常顺利，毫无阻碍或挫折。
例：在生活中，我们难免会遇到些挫折，不可能是一帆风顺。
例：爸爸的事业一帆风顺，我们都很为他感到高兴。

218．一鼓作气（yī gǔ zuò qì）
解释：一鼓作气原意是作战擂响第一声战鼓时，士气最为高涨。
比喻趁劲头大的时候鼓起干劲，一口气把工作做完。
例：在连胜两局后，我校一鼓作气，把对方球员打败，夺得了冠军。

219．一见如故（yī jiàn rú gù）
解释：初次见面就像老朋友一样，形容彼此非常投合。
例：我们虽然是第一次见面，却是一见如故，谈得很投机。

220．一鸣惊人（yī míng jīng rén）
解释：原义是一叫就使人震惊。比喻平时没有突出的表现，一下子做出惊人的成绩。
例：他平时沉默寡言，谁知他第一次参加讲故事比赛却得到冠军，真是一鸣惊人啊!
"""
#format_sentences(text)
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
while i < 10:
    chosen = random.randint(0, len(ciyus))
    while chosen in chosenNums:
        chosen = random.randint(0, len(ciyus))
    chosenNums.append(chosen)
    ans = input(f"{i+1}. {hypys[chosen]}\nGive answer: ")
    if ans != ciyus[chosen]:
        correctTimes = 0
        points -= 1
        print(f'Wrong! The word was {ciyus[chosen]}. Restarting..')
        if ciyus[chosen] not in wrongWords:
            ciyus[chosen] = [1, 0]
        else:
            ciyus[chosen][0] += 1
        print(f"Do you at least know the meaning of the word?")
        input("Enter the meaning in your interpretation: ")
        print(meanings[chosen])
        match = input("Did it match with the above meaning? Y/N: ")
        if match == "N":
            print(f"Dang :(")
            ciyus[chosen][1] += 1
        else:
            print("Oh yay!")
        chosenNums.pop()
        i = 0
    else:
        print('Correct! Though, did you WRITE your word wrong?')
        print(ciyus[chosen])
        writeWrong = input("Y/N")
        if writeWrong == "Y":
            correctTimes = 0
            points -= 1
            print("Hm, okay. That's fine.")
            if ciyus[chosen] not in wrongWords:
                ciyus[chosen] = [1, 0]
            else:
                ciyus[chosen][0] += 1
            print(f"Do you at least know the meaning of the word?")
            input("Enter the meaning in your interpretation: ")
            print(meanings[chosen])
            match = input("Did it match with the above meaning? Y/N: ")
            if match == "N":
                print(f"Dang :(")
                ciyus[chosen][1] += 1
            else:
                print("Oh yay!")
            chosenNums.pop()
            i = 0
        else:
            points += 1
            print("Great!")
            print(f"Do YOU know the meaning of the word?")
            input("Enter the meaning in your interpretation: ")
            print(meanings[chosen])
            match = input("Did it match with the above meaning? Y/N: ")
            if match == "N":
                print(f"Dang :(. We forgive tho.")
            else:
                print("Oh yay!")
            correctWords.append(ans)
            correctTimes += 1
            i += 1
    correctStreak = max(correctStreak, correctTimes)
print("In conclusion..")
print(f"You have gotten for some words, especially..")
wrongWords.sort()
print(" Wrong Attempts | Word ")
for word in wrongWords:
    print(word)
print(f"You managed to maintain a streak of correct answers, at around {correctStreak} answers correct in a row.")
print(f"Overall, your score was {points}")
if points == 50:
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