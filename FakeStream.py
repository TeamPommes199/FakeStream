import random
import time
import keyboard
import pyttsx3

followCount = 0
aboCount = 0
money = 0
bits = 0
aboLength = {}
werbung = False
pause = False
sound = True
spectator = 1

fMT = "        {randomName} followed"
nAMT = """          {randomName} abonniert! Dein Geld: {money} Euro! Abo Count: {aboCount}!"""
lAMT = """          {randomName} abonniert im {aboLength[randomName]}. Monat! Dein Geld: {money} Euro!"""
bMT = """           {randomName} spendet {bitsPlus} Bits! Bits Gesamt: {bits}!"""
dMT = """           {randomName} haut {moneyPlus}€ raus! Dein Geld: {money} Euro"""
sGMT = """          {randomName} giftet {giftSubs} Subs! Dein Geld: {money} Euro! Abo Count: {aboCount}!"""
sGlAMT = """        {randomName} abonniert im {aboLength[randomName]}. Monat!"""
rTM = """           {randomName} raidet mit {spectatorRaid} Zuschauern! +{newFollower} Follower!"""

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
            for line in data[11:]:
                name, length = line.strip().split(': ')
                aboLength[name] = int(length)
            return followCount, aboCount, money, bits, fMT, nAMT, lAMT, bMT, dMT, sGMT, rTM, aboLength
    except FileNotFoundError:
        print("Datei nicht gefunden!")
        return None

def save_data_to_file(filename):
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
        for name, length in aboLength.items():
            file.write(f'Abos for {name}: {length}\n')

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
        
        time.sleep(3)
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

    messageType = [1, 2, 3, 4, 5, 6, 7]

    randomMessageType = random.choices(messageType, weights=(100 * ((followCount + 1) / 50), 12 * ((followCount + 1) / 47.5), 0.25 * (followCount + 1) / 25, 0.1 * (followCount + 1) / 30, 0.12 * (followCount + 1) / 50, 0.15 * (followCount + 1) / 75, 0.08 * (followCount + 1) / 18), k=1)

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

def configuration():
    global pause
    global sound
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
                    (1) Ja
                    (2) Nein
                       """)
        
        if cSound == "1":
            sound = True
        
        elif cSound == "2":
            sound = False

    pause = False

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

keyboard.add_hotkey("w + 3", werbung30)
keyboard.add_hotkey("w + 6", werbung60)
keyboard.add_hotkey("alt + shift", configuration)

choiceName()

while True:
    if pause == False:
        if followCount >= 0 and followCount < 99:
            timer = random.uniform(7.5, 10) / (aboCount + 1) * 25
        
        elif followCount >= 100 and followCount < 299:
            timer = random.uniform(5.8, 6.4) / (aboCount + 1) * 25

        elif followCount >= 300 and followCount < 499:
            timer = random.uniform(4.5, 5) / (aboCount + 1) * 25
        
        elif followCount >= 500 and followCount < 999:
            timer = random.uniform(3.25, 3.8) / (aboCount + 1) * 25

        elif followCount >= 1000 and followCount < 1999:
            timer = random.uniform(2.1, 2.8) / (aboCount + 1) * 25
            
        elif followCount >= 2000:
            timer = random.uniform(1.4, 2) / (aboCount + 1) * 25


        time.sleep(timer)

        choiceType()

        if randomMessageType == [1]:
            choiceName()
            choiceMessage()

            print(randomName + ": " + randomMessage)

        if randomMessageType == [2]:
            choiceName()

            followMessage = fMT.replace("{randomName}", randomName)

            followCount += 1
            
            print(f"""{followMessage}
                Follow Count: {followCount}""")
            if sound == True:
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
                aboCount -= 1

                longAboMessage = lAMT.replace("{randomName}", randomName).replace("{money}", str(money)).replace("{aboLenght[randomName]}", str(aboLength[randomName]))

                print(longAboMessage)

                if sound == True:
                    pyttsx3.speak(f"{randomName}, Abonniert im {aboLength[randomName]}. Monat!")
            
        if randomMessageType == [4] and followCount >= 20:
            choiceName()
            bitsValue = [50, 200, 500, 1200, 2500, 4000, 7500, 12000, 25000]
            bitsPlus = random.choices(bitsValue, weights=(75, 15, 6, 2, 1.2, 0.6, 0.1, 0.07, 0.03), k=1)
            bits += bitsPlus[0]

            bitsMessage = bMT.replace("{randomName}", randomName).replace("{bits}", str(bits)).replace("{bitsPlus}", str(bitsPlus))

            print(bitsMessage)
            if sound == True:
                pyttsx3.speak(f"{randomName} spendet {bitsPlus[0]} Bits!")

        if randomMessageType == [5] and followCount >= 20:
            choiceName()
            moneyValue = [1, 2, 3, 5, 10, 20, 30, 50, 100]
            moneyPlus = random.choices(moneyValue, weights=(75, 15, 6, 2, 1.2, 0.6, 0.1, 0.07, 0.03), k=1)
            money += moneyPlus[0]

            donationMessage = dMT.replace("{randomName}", randomName).replace("{money}", str(money)).replace("{moneyPlus}", str(moneyPlus))

            print(donationMessage)

            if sound == True:
                pyttsx3.speak(f"{randomName} spendet {moneyPlus[0]} €")
        
        if randomMessageType == [6] and followCount >= 20:
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
        
        if randomMessageType == [7]:
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
            else:
                spectatorRaid = random.randint(1, 25)
            
            newFollower = random.randint(1, spectatorRaid)

            followCount += newFollower

            raidMessage = rTM.replace("{randomName}", randomName).replace("{spectatorRaid}", str(spectatorRaid)).replace("{newFollower}", str(newFollower))

            print(raidMessage)

            if sound == True:
                pyttsx3.speak(f"{randomName} raidet mit {spectatorRaid} Zuschauern!")
    
    if saveDataQ == "Ja" or loadDataQ == "Ja":
        if saveDataQ == "Ja":
            save_data_to_file(saveDataFile)
        else:
            save_data_to_file(loadDataFile)
