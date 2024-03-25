import tkinter as tk
import random
import time
import keyboard
import pyttsx3
import threading

root = tk.Tk()
root.title("FakeStream")
root.geometry("800x400")

followCount = 0
aboCount = 1
money = 2
bits = 0
aboLength = {}
werbung = False
pause = False
sound = True
fSound = True
mvp = False
spectator = 1
antworten = []
start1 = False
shopWerbung60 = None
shopMVP = None
actionMessage = None

fMT = "        {randomName} followed"
nAMT = """          {randomName} abonniert! Dein Geld: {money} Euro! Abo Count: {aboCount}!"""
lAMT = """          {randomName} abonniert im {aboLength[randomName]}. Monat! Dein Geld: {money} Euro!"""
bMT = """           {randomName} spendet {bitsPlus} Bits! Bits Gesamt: {bits}!"""
dMT = """           {randomName} haut {moneyPlus}€ raus! Dein Geld: {money} Euro"""
sGMT = """          {randomName} giftet {giftSubs} Subs! Dein Geld: {money} Euro! Abo Count: {aboCount}!"""
sGlAMT = """        {randomName} abonniert im {aboLength[randomName]}. Monat!"""
rTM = """           {randomName} raidet mit {spectatorRaid} Zuschauern! +{newFollower} Follower!"""

def weights():
    global messageWeight
    global followWeight
    global subWeight
    global bitsWeight
    global donationWeight
    global subGiftWeight
    global raidWeight
    global weight

    if followCount < 20:
        messageWeight = 100
        followWeight = 25
        subWeight = 0
        bitsWeight = 0
        donationWeight = 0
        subGiftWeight = 0
        raidWeight = 0
    elif followCount >= 20 and followCount < 35:
        messageWeight = 105
        followWeight = 5
        subWeight = 2
        bitsWeight = 0
        donationWeight = 0
        subGiftWeight = 0
        raidWeight = 0
    elif followCount >= 35 and followCount < 50:
        messageWeight = 110
        followWeight = 4.75
        subWeight = 1.80
        bitsWeight = 0
        donationWeight = 0
        subGiftWeight = 0.40
        raidWeight = 0
    elif followCount >= 50 and followCount < 75:
        messageWeight = 115
        followWeight = 4.5
        subWeight = 1.7
        bitsWeight = 2
        donationWeight = 1.5
        subGiftWeight = 0.41
        raidWeight = 2.2
    elif followCount >= 75 and followCount < 120:
        messageWeight = 120
        followWeight = 4.25
        subWeight = 1.6
        bitsWeight = 1.975
        donationWeight = 1.475
        subGiftWeight = 0.42
        raidWeight = 2.175
    elif followCount >= 120 and followCount < 200:
        messageWeight = 130
        followWeight = 4
        subWeight = 1.55
        bitsWeight = 1.95
        donationWeight = 1.45
        subGiftWeight = 0.43
        raidWeight = 2.15
    elif followCount >= 200 and followCount < 300:
        messageWeight = 140
        followWeight = 4
        subWeight = 1.5
        bitsWeight = 1.925
        donationWeight = 1.425
        subGiftWeight = 0.44
        raidWeight = 2.125
    elif followCount >= 300:
        messageWeight = 500
        followWeight = 4 + (0.1 * (aboCount + 3 / 3))
        subWeight = 1.5 + (0.1 * (followCount / 1500))
        bitsWeight = 1.9 + (0.01 * (aboCount + 5 / 5))
        donationWeight = 1.4 + (0.01 * (aboCount + 2 / 2))
        subGiftWeight = 0.45 + (0.01 * (followCount / 1750))
        raidWeight = 2.1 + (0.01 * (followCount / 750))

    weight = (messageWeight, followWeight, subWeight, bitsWeight, donationWeight, subGiftWeight, raidWeight)

def tutorial1():
    global start1
    start1 = True
    print("""Willkommen! Ich bin das Tutorial!
          Hier siehst du Narichten von Bots.
          """)    
    time.sleep(3)
    print("""Oh! Hier kommen sogar schon die ersten Narichten!
          """)
    time.sleep(1)
    tMessage()
    tMessage()
    tMessage()
    print("""
          Huch! Dein erster Follow!
          """)
    time.sleep(2)
    tFollow()
    print("""
          Versuch jetzt mal die ersten 20 Follower zu erreichen!
          Übrigens: Du kannst mit der Tastenkombination 'alt + a', eine abstimmung Starten.
          Probier diese doch gerne mal aus!
          Viel Spaß dir jetzt noch und bis später!
          """)
    time.sleep(6)

def tutorial2():
    global start2

    start2 = True
    print("""Herzlichen Glückwunsch zu 20 Followern!
          Du hast nun Abonnements freigeschaltet!""")
    time.sleep(2)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("""Oh! Da ist ja sogar schon ein Sub!
          """)
    time.sleep(2)
    tSub()
    print("""Außerdem bekommst du pro Sub 2€,
          die du bald im Shop einlösen kannst!
          """)
    time.sleep(3)
    print("""Übrigens kannst du ab sofort die Tastenkombination
          'w + 3' freigeschaltet,
          mit der du nun Werbung für ein wenig Geld aktievieren kannst!
          (Du wirst selber die Werbung nicht sehen)
          Probier es doch mal gerne aus! Wir werden uns später nochmal sehen!
          """)
    time.sleep(6)

def tutorial3():
    global start3

    start3 = True

    print("""Hey! Du hast 35 Follower erreicht!
          Nun können bots auch mit geringer Chance
          Subs giften!
          """)
    time.sleep(3)
    print("""Außerdem kannst du den Sound nun an und aus stellen,
          oder aber auch selbst Follow Messages,
          Abo Messages, ... configuieren!
          Probier es doch mal gerne mit ' alt + shift' aus!
          Viel Spaß dir noch und villeicht ja bis später!
          """)
    time.sleep(2)

def load_data_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.readlines()
            followCount = int(data[0].split('- ')[1])
            aboCount = int(data[1].split('- ')[1])
            money = float(data[2].split('- ')[1])
            bits = float(data[3].split('- ')[1])
            fMT = str(data[4].split('- ')[1])
            nAMT = str(data[5].split('- ')[1])
            lAMT = str(data[6].split('- ')[1])
            bMT = str(data[7].split('- ')[1])
            dMT = str(data[8].split('- ')[1])
            sGMT = str(data[9].split('- ')[1])
            rTM = str(data[10].split('- ')[1])
            aboLength = {}
            for line in data[50:]:
                name, length = line.strip().split(': ')
                aboLength[name] = int(length)
            return followCount, aboCount, money, bits, fMT, nAMT, lAMT, bMT, dMT, sGMT, rTM, aboLength
    except FileNotFoundError:
        print("Datei nicht gefunden!")
        return None

def save_data_to_file(filename):
    global money
    money = round(money, 2)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f'Follow Count- {followCount}\n')
        file.write(f'Abo Count- {aboCount}\n')
        file.write(f'Money- {money}\n')
        file.write(f'Bits- {bits}\n')
        file.write(f'follow-Message-Template- {fMT.strip()}\n')
        file.write(f'new-Abo-Message-Template- {nAMT.strip()}\n')
        file.write(f'long-Abo-Message-Template- {lAMT.strip()}\n')
        file.write(f'bits-Message-Template- {bMT.strip()}\n')
        file.write(f'donations-Message-Template- {dMT.strip()}\n')
        file.write(f'sub-Gift-Message-Template- {sGMT.strip()}\n')
        file.write(f'raid-Template-Message- {rTM.strip()}\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        file.write(f'\n')
        for name, length in aboLength.items():
            file.write(f'{name}: {length}\n')

def werbung30():
    global money
    global werbung
    global spectator
    if werbung == False:
        spectator = random.randint(1, 50)
        plusMoney = spectator * 0.07
        money += plusMoney
        werbung = True
        plusMoney = round(plusMoney, 2)

        print("""30 Sekunden Werbung Aktiviert für:
            """, spectator, """Zuschauer
            Geld für diese Werbung:""", plusMoney, "€")
        
        time.sleep(30)
        werbung = False
        spectator = 1

def werbung60():
    global money
    global werbung
    global spectator
    if werbung == False:
        spectator = random.randint(5, 75)
        plusMoney = spectator * 0.06
        money += plusMoney
        werbung = True
        plusMoney = round(plusMoney, 2)

        print("""60 Sekunden Werbung Aktiviert für:
            """, spectator, """Zuschauer
            Geld für diese Werbung:""", plusMoney, "€")
        
        time.sleep(60)
        werbung = False
        spectator = 1

def choiceType():
    global randomMessageType

    weights()

    messageType = [1, 2, 3, 4, 5, 6, 7]

    randomMessageType = random.choices(messageType, weights=weight, k=1)

def choiceName():
    global randomName
    global names

    names = [
        "TeamPommes ✅",
        "BastiGHG 🔴",
        "JoJonas 🔴",
        "Neverseen 🔴",
        "DiamondCat 👑",
        "TheRealFinn 👑",
        "Tomato 👑",
        "AlphaGamer3000",
        "AngelWings",
        "ArcaneMage",
        "AquaMarine",
        "AtomicBlaster",
        "BattleMage",
        "BlazingComet",
        "BossBabe",
        "CosmicFallenAngel",
        "CosmicLion",
        "CosmicSamurai",
        "CyberCelestial",
        "CyberHacker",
        "CyberPunk",
        "CyberQueen",
        "CyberSamurai",
        "DeathWish",
        "DiamondDog",
        "DigitalWarrior",
        "DoomBringer",
        "EagleEye",
        "ElectricDreams",
        "EpicGamer",
        "EternalGamer",
        "FieryDragon",
        "Fireball",
        "FlamingPhoenix",
        "Frostbyte",
        "GameMaster",
        "GamerGod",
        "GoldenKnight",
        "IceDragon",
        "IronFist",
        "JellyBean",
        "JungleWarrior",
        "LaserCat",
        "LuckyCharm",
        "LuckyShot",
        "LunaTheCat",
        "MadScientist",
        "MasterBuilder",
        "MysticWizard",
        "MysticalEnigma",
        "NeonGoddess",
        "Nightshade",
        "NovaStorm",
        "PandaPilot",
        "PixelWarrior",
        "PlatinumPlaya",
        "Pommes_XD",
        "ProSniper",
        "PsychedelicPrincess",
        "RapidFire",
        "ShadowHunter",
        "ShadowNinja",
        "SilentShadow",
        "SavageBeast",
        "SneakyNinja",
        "SnowQueen",
        "SpeedDemon",
        "SpeedyGonzales",
        "StarStriker",
        "StealthyAssassin",
        "Sunflower",
        "TheGuru",
        "TheRealDeal",
        "TheWizard",
        "TigerTamer",
        "VirtualReality",
        "WickedWitch",
        "XenonX",
        "XtremeGaming",
        "ZombieSlayer"
    ]

    randomName = random.choice(names)

def choiceMessage():
    global randomMessage

    messages = [
    "Willkommen im Stream! 🎮",
    "Lasst uns gemeinsam zocken! 🕹️",
    "Hallo, liebe Community! 👋",
    "Ab ins Battle Royale! 💥",
    "Chat, was haltet ihr von diesem Spiel? 🤔",
    "Gibt es hier Rocket League-Fans? 🚗⚽",
    "Time for some speedruns! ⏱️",
    "Habt ihr Tipps für meinen Build? 🔧",
    "Chat, was ist euer Lieblingsspiel? 🎮",
    "Ich liebe die Community hier! ❤️",
    "Auf geht's, wir rocken das! 🤘",
    "Wer hat Lust auf ein 1v1? 👊",
    "Chat, wie war euer Tag? 😊",
    "Lasst uns zusammen lachen! 😂",
    "Ich bin so hyped für das neue Update! 🚀",
    "Gibt es hier Animal Crossing-Fans? 🌴🐶",
    "Chat, was ist euer Lieblings-Emote? 😎",
    "Time for some chill beats! 🎵",
    "Ich liebe eure Unterstützung! 🙌",
    "Wer ist bereit für den nächsten Bosskampf? 👹",
    "Chat, was ist euer Gaming-Snack? 🍿",
    "Lasst uns über die neuesten Gaming-News quatschen! 🗞️",
    "Ich bin so dankbar für diese Community! 🙏",
    "Gibt es hier Speedrunner? 🏃‍♂️",
    "Time for some PogChamp moments! 😮",
    "Ich freue mich auf die nächste Stream-Session! 🎥",
    "Chat, was sind eure Pläne fürs Wochenende? 🌟",
    "Bereit für eine epische Gaming-Nacht? 🌙🎮",
    "Wer ist heute der MVP im Chat? 🏆",
    "Können wir heute den Highscore knacken? 📈",
    "Welches Spiel soll ich als Nächstes streamen? 🎲",
    "Chat, zeigt mir eure besten Memes! 😆",
    "Wer freut sich auch schon auf das nächste Turnier? 🏆",
    "Chat, habt ihr schon das Easter Egg gefunden? 🥚",
    "Welcher Streamer inspiriert euch am meisten? 🌟",
    "Chat, seid ihr Team Controller oder Team Keyboard? ⌨️🎮",
    "Lasst uns heute die Community-Challenge meistern! 💪",
    "Wer ist euer Lieblingscharakter in diesem Spiel? 🎭",
    "Chat, lasst uns eine Runde Q&A starten! ❓",
    "Welches Retro-Spiel liebt ihr am meisten? 🕹️",
    "Chat, wer ist euer Lieblingsgegner? 😈",
    "Lasst uns heute einen neuen Strategieplan ausarbeiten! 🗺️",
    "Wer ist bereit für eine Überraschung im Stream? 🎁",
    "Chat, welches ist das unterschätzteste Spiel? 🤷‍♂️",
    "Heute ist ein guter Tag, um zu siegen! 🏆",
    "Chat, welche Mods könnt ihr empfehlen? 🛠️",
    "Lasst uns heute die Welt retten! 🌍🎮",
    "Chat, wer macht heute Nacht den Endboss platt? 🎯",
    "Zeit für eine kleine Pause mit Snacks und Getränken! 🥤🍪",
    "Chat, teilt eure lustigsten Gaming-Momente! 😄",
    "Wer ist heute Abend der Glückspilz im Spiel? 🍀",
    "Chat, lasst uns über die besten Gaming-Headsets diskutieren! 🎧",
    "Heute fühlen wir die Power des Gaming! 💪🎮",
    "Chat, wer ist euer Lieblingsstreamer und warum? 📺"
]

    randomMessage = random.choice(messages)

def addAbo():
    global aboLength
    global randomName

    if randomName in aboLength:
        aboLength[randomName] += 1
    else:
        aboLength[randomName] = 1

    threading.Timer(180, removeAbo).start()

def removeAbo():
    global aboCount
    aboCount -= 1

def giveMVP():
    global pause
    global mvpName
    global mvp

    pause = True

    print("Wer soll heute MVP bekommen?")
    mvpName = input("")

    mvp = True
    pause = False

def reply():
    global replyName

    time.sleep(timer)

    if randomMessage == "Wer ist heute der MVP im Chat? 🏆":
        if mvp == True:
            replyName = randomName

            choiceName()

            print(f"{randomName}: @{replyName}, {mvpName} hat heute MVP bekommen.")
        
        else:
            replyName = randomName

            choiceName()

            print(f"{randomName}: @{replyName}, bisher noch niemand.")
    
    time.sleep(timer)    

def configuration():
    global pause
    global sound
    global fSound
    global fMT
    global nAMT
    global lAMT
    global bMT
    global dMT
    global sGMT
    global rTM
    pause = True

    category = input("""Kategorie auswählen:
                     (1) Messages
                     (2) Sound
                     """)
    
    if category == "1":
        cMessage = input("""Messages:
                         (1) Follow Message
                         (2) Neuer-Abo Message
                         (3) Re-Abo Message
                         (4) Bits-Spenden Message
                         (5) Donations Message
                         (6) Gift-Subs Message
                         (7) Raid Message
                         """)
        
        if cMessage == "1":
            print("""Placeholders:
                  {randomName} - für den Namen, der gefollowed hat
                    """)
            print("Aktuelle Message:", fMT)
            newMessage = input("""Neue Message: """)
            
            fMT = newMessage
        
        elif cMessage == "2":
            print("""Placeholders:
                  {randomName} - für den Namen, der gefollowed hat
                  {money} - zeigt deinen aktuellen Geld-Stand an
                  {aboCount} - zeigt deinen aktuellen Abo-Stand an""")
            print("Aktuelle Message:", nAMT)
            newMessage = input("""Neue Message: """)
        
            nAMT = newMessage
        
        elif cMessage == "3":
            print("""Placeholders:
                  {randomName} - für den Namen, der gefollowed hat
                  {money} - zeigt deinen aktuellen Geld-Stand an
                  {aboLength[randomName]} - zeigt die Abo Anzahl des Namens""")
            print("Aktuelle Message:", lAMT)
            newMessage = input("""Neue Message: """)

            lAMT = newMessage

        elif cMessage == "4":
            print("""Placeholders:
                  {randomName} - für den Namen, der gefollowed hat
                  {bits} - zeigt deinen aktuellen Bit-Stand an
                  {bitsPlus} - Anzahl der gespendeten Bits""")
            print("Aktuelle Message:", bMT)
            newMessage = input("""Neue Message: """)

            bMT = newMessage
        
        elif cMessage == "5":
            print("""Placeholders:
                  {randomName} - für den Namen, der gefollowed hat
                  {money} - zeigt deinen aktuellen Geld-Stand an
                  {moneyPlus} - Anzahl des gespendeten Geldes""")
            print("Aktuelle Message:", dMT)
            newMessage = input("""Neue Message: """)

            dMT = newMessage
        
        elif cMessage == "6":
            print("""Placeholders:
                  {randomName} - für den Namen, der gefollowed hat
                  {money} - zeigt deinen aktuellen Geld-Stand an
                  {aboCount} - zeigt deinen aktuellen Abo-Stand an
                  {giftSubs} - Anzahl der gegifteten Subs""")
            print("Aktuelle Message:", sGMT)
            newMessage = input("""Neue Message: """)

            sGMT = newMessage
        
        elif cMessage == "7":
            print("""Placeholders:
                  {randomName} - für den Namen, der gefollowed hat
                  {spectatorRaid} - anzahl der Zuschauer, mit dem der namen geraidet hat
                  {newFollower} - anzahl der neuen Follower""")
            print("Aktuelle Message:", rTM)
            newMessage = input("""Neue Message: """)

            rTM = newMessage
    
    if category == "2":
        cSound = input("""Sound:
                    (1) Follower
                    (2) Rest
                       """)
        
        if cSound == "1":
            sFollwer = input("""Follower:
                            (1) Ja
                            (2) Nein
                             """)
            if sFollwer == "1":
                fSound = True
            elif sFollwer == "2":
                fSound = False
        elif cSound == "2":
            sRest = input("""Rest:
                            (1) Ja
                            (2) Nein
                             """)
            if sRest == "1":
                sound = True
            elif sRest == "2":
                sound = False

    pause = False

def abstimmung():
    global pause
    global antworten

    pause = True

    print("Wie lautet der Titel der Umfrage?")

    titel = input("")

    print("Wie viele Antwort möglich keiten soll es geben?")

    time.sleep(0.1)

    aAnzahl = input("")

    while int(aAnzahl) > 0:
        rAntwort = 1
        votes = 0

        antwort = input(f"Antwort, dann Enter drücken: ")

        antworten.insert(rAntwort - 1, (antwort, votes))

        rAntwort += 2
        aAnzahl = int(aAnzahl) - 1
    
    rAntwort = 1

    tAbstimmung = 10

    while tAbstimmung > 0:
        for i in range(len(antworten)):
            nVotes = random.randint(1, 20)
            antwort, aVotes = antworten[i]
            aVotes += nVotes
            antworten[i] = (antwort, aVotes)
            print(f"{antwort}: {aVotes} Votes")

        tAbstimmung -= 1

        time.sleep(3)
    
    print("")
    print(f"Ergebnisse: {titel}")
    for antwort, aVotes in antworten:
        print(f"{antwort}: {aVotes} Votes")
    print("")

    antworten.clear()

    time.sleep(3)

    pause = False

def tMessage():
    choiceName()
    choiceMessage()

    print(randomName + ": " + randomMessage)
    
    time.sleep(3)

def tFollow():
    choiceName()

    followMessage = fMT.replace("{randomName}", randomName)
    
    print(f"{followMessage}")

    if sound == True:
        pyttsx3.speak(f"{randomName} folgt nun!")
    
    time.sleep(3)

def tSub():
    newAboMessage = nAMT.replace("{randomName}", randomName).replace("{money}", str(money)).replace("{aboCount}", str(aboCount))

    print(newAboMessage)

    if sound == True:
        pyttsx3.speak(f"{randomName} subt!")
    
    time.sleep(2)

def shop():
    global pause
    global money
    global shopWerbung60
    global shopMVP

    pause = True

    if not shopWerbung60 == "freigeschaltet":
        shopWerbung60 = "200 €"

    if not shopMVP == "freigeschaltet":
        shopMVP = "250 €"

    time.sleep(1)

    print(f"""
Willkommen hier im Shop!
Hier kannst du coole Features freischalten!
            (1) 60 Sekunden Werbung - {shopWerbung60}
            (2) MVP vergeben - {shopMVP}
Du hast: {money} €""")
    
    time.sleep(2)
    
    shopinput = input("")

    if shopinput == "1":
        if shopWerbung60 == "freigeschaltet":
            print("Du hast dieses Feature bereits freigeschaltet!")
        elif money < 200:
            print("Du hast nicht genug Geld!")
        else:
            keyboard.add_hotkey("w + 6", werbung60)
            money = money - 200
            shopWerbung60 = "freigeschaltet"
            print("""Du hast nun die 60 Sekunden Werbung freigeschaltet!
Du kannst diese nun nutzen mit:
                  'w + 6'""")
    
    if shopinput == "2":
        if shopMVP == "freigeschaltet":
            print("Du hast dieses Feature bereits freigeschaltet!")
        elif money < 250:
            print("Du hast nicht genug Geld!")
        else:
            keyboard.add_hotkey("alt + m", werbung60)
            money = money - 250
            shopMVP = "freigeschaltet"
            print("""Du kannst nun einer Person MVP geben!
Vergeben machst du es, mit:
                  'alt + m'""")
            
    pause = False

def action():
    global timer
    global actionMessage

    while True:
        if pause == False:
            if start1 == True:
                timer = 1

            elif followCount >= 0 and followCount < 50:
                timer = random.uniform(1, 1.5) / (aboCount + 1) * 5
                if timer > 1.5:
                    timer = 1.5

            elif followCount >= 50 and followCount < 500:
                timer = random.uniform(1.5, 3) / (aboCount + 1) * 15
                if timer > 3:
                    timer = 3
            
            elif followCount >= 500 and followCount < 1000:
                timer = random.uniform(1.6, 2.6) / (aboCount + 1) * 19
                if timer > 2.6:
                    timer = 2.6

            elif followCount >= 1000 and followCount < 2500:
                timer = random.uniform(1.4, 2.3) / (aboCount + 1) * 22
                if timer > 2.3:
                    timer = 2.3
            
            elif followCount >= 2500 and followCount < 5000:
                timer = random.uniform(1.3, 2.1) / (aboCount + 1) * 27
                if timer > 2.1:
                    timer = 2.1

            elif followCount >= 5000 and followCount < 10000:
                timer = random.uniform(1.2, 1.9) / (aboCount + 1) * 33
                if timer > 1.9:
                    timer = 1.9
                
            elif followCount >= 10000:
                timer = random.uniform(1.1, 1.75) / (aboCount + 1) * 40
                if timer > 1.75:
                    timer = 1.75

            if spectator < 5:
                sspectator = 5

            else:
                sspectator = spectator

            time.sleep(timer * (sspectator / 5))

            choiceType()

            if randomMessageType == [1]:
                choiceName()
                choiceMessage()

                print(randomName + ": " + randomMessage)

                actionMessage = tk.StringVar
                actionMessage.set(randomName + ": " + randomMessage)

                reply()

            if randomMessageType == [2]:
                choiceName()

                followMessage = fMT.replace("{randomName}", randomName)

                followCount += 1
                
                print(f"""{followMessage}
                    Follow Count: {followCount}""")
                if fSound == True:
                    pyttsx3.speak(f"{randomName} folgt nun!")
            
            if randomMessageType == [3] and followCount >= 20:
                choiceName()

                aboCount += 1
                money += 2

                addAbo()

                if aboLength[randomName] == 1:
                    
                    newAboMessage = nAMT.replace("{randomName}", randomName).replace("{money}", str(money)).replace("{aboCount}", str(aboCount))

                    print(newAboMessage)

                    if sound == True:
                        pyttsx3.speak(f"{randomName} subt!")

                elif aboLength[randomName] >= 2:

                    longAboMessage = lAMT.replace("{randomName}", randomName).replace("{money}", str(money)).replace("{aboLenght[randomName]}", str(aboLength[randomName]))

                    print(longAboMessage)

                    if sound == True:
                        pyttsx3.speak(f"{randomName}, Abonniert im {aboLength[randomName]}. Monat!")

            if randomMessageType == [4] and followCount >= 50:
                choiceName()
                bitsValue = [50, 200, 500, 1200, 2500, 4000, 7500, 12000, 25000]
                bitsPlus = random.choices(bitsValue, weights=(75, 15, 6, 2, 1.2, 0.6, 0.1, 0.07, 0.03), k=1)
                bits += bitsPlus[0]

                bitsMessage = bMT.replace("{randomName}", randomName).replace("{bits}", str(bits)).replace("{bitsPlus}", str(bitsPlus))

                print(bitsMessage)
                if sound == True:
                    pyttsx3.speak(f"{randomName} spendet {bitsPlus[0]} Bits!")

            if randomMessageType == [5] and followCount >= 50:
                choiceName()
                moneyValue = [1, 2, 3, 5, 10, 20, 30, 50, 100]
                moneyPlus = random.choices(moneyValue, weights=(75, 15, 6, 2, 1.2, 0.6, 0.1, 0.07, 0.03), k=1)
                money += moneyPlus[0]

                donationMessage = dMT.replace("{randomName}", randomName).replace("{money}", str(money)).replace("{moneyPlus}", str(moneyPlus))

                print(donationMessage)

                if sound == True:
                    pyttsx3.speak(f"{randomName} spendet {moneyPlus[0]} €")
            
            if randomMessageType == [6] and followCount >= 35:
                choiceName()

                giftSubs = random.randint(1, 10)

                subGiftMessage = sGMT.replace("{randomName}", randomName).replace("{giftSubs}", str(giftSubs))

                if sound == True:
                    pyttsx3.speak(f"{randomName} giftet {giftSubs} Subs!")

                while giftSubs > 0:
                    choiceName()

                    aboCount += 1
                    money += 2

                    addAbo()

                    subGiftLongAboMessage = sGlAMT.replace("{randomName}", randomName).replace("{aboLenght[randomName]}", str(aboLength[randomName]))

                    print(subGiftLongAboMessage)

                    giftSubs -= 1
                
                subGiftMessage = subGiftMessage.replace("{money}", str(money)).replace("{aboCount}", str(aboCount))

                print(subGiftMessage)
            
            if randomMessageType == [7] and followCount >= 50:
                choiceName()

                if followCount >= 50:
                    spectatorRaid = random.randint(2, 50)
                elif followCount >= 100:
                    spectatorRaid = random.randint(4, 75)
                elif followCount >= 175:
                    spectatorRaid = random.randint(7, 125)
                elif followCount >= 275:
                    spectatorRaid = random.randint(11, 200)
                elif followCount >= 400:
                    spectatorRaid = random.randint(16, 300)
                
                newFollower = random.randint(1, spectatorRaid)

                followCount += newFollower

                raidMessage = rTM.replace("{randomName}", randomName).replace("{spectatorRaid}", str(spectatorRaid)).replace("{newFollower}", str(newFollower))

                print(raidMessage)

                if sound == True:
                    pyttsx3.speak(f"{randomName} raidet mit {spectatorRaid} Zuschauern!")
        
        if followCount == 20 and start1 == True:
            start1 = False
            tutorial2()

        if followCount == 35 and start2 == True:
            start2 = False
            tutorial3()

        if saveDataQ == "Ja" or loadDataQ == "Ja":
            if saveDataQ == "Ja":
                save_data_to_file(saveDataFile)
            else:
                save_data_to_file(loadDataFile)

loadDataQ = input("Data Laden? (Ja/Nein): ")
saveDataQ = input("Data Saven? (Ja/Nein): ")

if saveDataQ == "Ja":
    saveDataFile = input("Datei-Namen: ") # C:\Users\User\Documents\funtests\FakeStreamTest\test1.txt oder dein pfad wo du speichern willst

if loadDataQ == "Ja":
    loadDataFile = input("Datei-Namen: ") # C:\Users\User\Documents\funtests\FakeStreamTest\test1.txt oder dein pfad wo du speichern willst
    followCount, aboCount, money, bits, fMT, nAMT, lAMT, bMT, dMT, sGMT, rTM, aboLength = load_data_from_file(loadDataFile)

    print("Follow Count:", followCount)
    print("Abo Count:", aboCount)
    print("Money:", money)
    print("Bits:", bits)
    print("fMT:", fMT)
    print("nAMT:", nAMT)
    print("lAMT:", lAMT)
    print("bMT:", bMT)
    print("dMT:", dMT)
    print("sGMT:", sGMT)
    print("rTM:", rTM)

else:
    tutorial1()

keyboard.add_hotkey("w + 3", werbung30)
keyboard.add_hotkey("alt + shift", configuration)
keyboard.add_hotkey("alt + a", abstimmung)
keyboard.add_hotkey("alt + s", shop)

choiceName()

label1 = tk.Label(root, text="actionMessage")
label1.pack()

for item in label1.keys():
    print(item, ": ", label1[item])

root.mainloop()