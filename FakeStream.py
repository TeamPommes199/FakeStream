import random
import time
import keyboard
import pyttsx3
import threading

followCount = 0
aboCount = 1
money = 2
bits = 0
aboLength = {}
statisticMonth = 1
werbung = False
pause = False
sound = True
fSound = True
mvp = False
spectator = 1
antworten = []
start1 = False
start2 = False
start3 = False
names = []
messages = []
subMessages = []
randomSpeakName = None
speakGiftSubs = None
statistic = False
on = False

shopWerbung60 = None
shopMVP = None

monthFollower = 0
monthMoney = 0
monthBits = 0
monthRaids = 0

month = 1
xp = 0
lvl = 1

testacc = False
tmW = 100
tfW = 12
tsW = 1.5
tbW = 1.62
tdW = 1.28
tsGW = 0.5
trW = 2
speed = 1

fMT = "        {randomName} followed"
nAMT = """          {randomName} abonniert! Dein Geld: {money} Euro! Abo Count: {aboCount}!"""
lAMT = """          {randomName} abonniert im {aboLength[randomName]}. Monat! Dein Geld: {money} Euro! {randomSubMessage}"""
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

    if testacc == True:
        messageWeight = float(tmW)
        followWeight = float(tfW)
        subWeight = float(tsW)
        bitsWeight = float(tbW)
        donationWeight = float(tdW)
        subGiftWeight = float(tsGW)
        raidWeight = float(trW)
    elif followCount < 20:
        messageWeight = 100
        followWeight = 25
        subWeight = 0
        bitsWeight = 0
        donationWeight = 0
        subGiftWeight = 0
        raidWeight = 0
    elif followCount >= 20 and followCount < 35:
        messageWeight = 125
        followWeight = 22
        subWeight = 2
        bitsWeight = 0
        donationWeight = 0
        subGiftWeight = 0
        raidWeight = 0
    elif followCount >= 35 and followCount < 50:
        messageWeight = 140
        followWeight = 19
        subWeight = 1.8
        bitsWeight = 0
        donationWeight = 0
        subGiftWeight = 0.40
        raidWeight = 0
    elif followCount >= 50 and followCount < 75:
        messageWeight = 150
        followWeight = 17
        subWeight = 1.7
        bitsWeight = 2
        donationWeight = 1.5
        subGiftWeight = 0.41
        raidWeight = 2.2
    elif followCount >= 75 and followCount < 120:
        messageWeight = 160
        followWeight = 15
        subWeight = 1.6
        bitsWeight = 1.975
        donationWeight = 1.475
        subGiftWeight = 0.42
        raidWeight = 2.175
    elif followCount >= 120 and followCount < 200:
        messageWeight = 175
        followWeight = 13
        subWeight = 1.55
        bitsWeight = 1.95
        donationWeight = 1.45
        subGiftWeight = 0.43
        raidWeight = 2.15
    elif followCount >= 200 and followCount < 300:
        messageWeight = 190
        followWeight = 11
        subWeight = 1.5
        bitsWeight = 1.925
        donationWeight = 1.425
        subGiftWeight = 0.44
        raidWeight = 2.125
    elif followCount >= 300:
        messageWeight = 500
        followWeight = 10 + (0.75 * (aboCount + 5 / 5))
        subWeight = 1.5 + (0.02 * (followCount + 250 / 1500))
        bitsWeight = 1.9 + (0.01 * (aboCount + 5 / 5))
        donationWeight = 1.4 + (0.01 * (aboCount + 2 / 2))
        subGiftWeight = 0.45 + (0.001 * (aboCount + 2 / 3))
        raidWeight = 2.1 + (0.002 * (followCount + 150 / 750))

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
            lvl = int(data[12].split('- ')[1])
            xp = int(data[13].split('- ')[1])
            month = int(data[14].split('- ')[1])
            aboLength = {}
            for line in data[50:]:
                name, length = line.strip().split(': ')
                aboLength[name] = int(length)
            return followCount, aboCount, money, bits, fMT, nAMT, lAMT, bMT, dMT, sGMT, rTM, aboLength, lvl, xp, month
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
        file.write(f'lvl- {lvl}\n')
        file.write(f'xp- {xp}\n')
        file.write(f'month- {month}\n')
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
        file.write(f'\n'.strip())
        for name, length in aboLength.items():
            file.write(f'{name}: {length}\n')

def nameslist():
    with open("C:\\Users\\User\\Documents\\funtests\\FakeStream\\names.txt", 'r', encoding='utf-8') as file:
        data = file.readlines()
        data = [line.strip() for line in data]
        return data

def messageslist():
    with open("C:\\Users\\User\\Documents\\funtests\\FakeStream\\messages.txt", 'r', encoding='utf-8') as file:
        data = file.readlines()
        data = [line.strip() for line in data]
        return data

def submessageslist():
    with open("C:\\Users\\User\\Documents\\funtests\\FakeStream\\subMessages.txt", 'r', encoding='utf-8') as file:
        data = file.readlines()
        data = [line.strip() for line in data]
        return data

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

    names = nameslist()

    if isinstance(names, list):
        randomName = random.choice(names)
    else:
        randomName = "Ein Fehler ist aufgetreten: " + names

def choiceMessage():
    global randomMessage
    global messages

    messages = messageslist()

    if isinstance(messages, list):
        randomMessage = random.choice(messages)
    else:
        randomMessage = "Ein Fehler ist aufgetreten: " + messages

def choiceSubMessage():
    global randomSubMessage
    global subMessages

    subMessages = submessageslist()

    if isinstance(subMessages, list):
        randomSubMessage = random.choice(subMessages)
    else:
        randomSubMessage = "Ein Fehler ist aufgetreten: " + subMessages

def addAbo():
    global aboLength
    global randomName

    if randomName in aboLength:
        aboLength[randomName] += 1
    else:
        aboLength[randomName] = 1

    threading.Timer(300, removeAbo).start()

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
    global fMT, nAMT, lAMT, bMT, dMT, sGMT, rTM
    global tmW, tfW, tsW, tbW, tdW, tsGW, trW, speed
    pause = True

    print("""Kategorie auswählen:
                     (1) Messages
                     (2) Sound""")
    if testacc == True:
        print("""                     (3) Test-Account
              """)
    else:
        print("")

    category = input("")

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

    if category == "3" and testacc == True:
        print(f"""
              Gewichte:
              (1) Message: {tmW}
              (2) Follow: {tfW}
              (3) Sub: {tsW}
              (4) Bits: {tbW}
              (5) Donations: {tdW}
              (6) SubGifts: {tsGW}
              (7) Raid: {trW}
              (8) Speed: {speed}
              """)
        wInput = input("")

        if wInput == "1":
            print("Neues Gewicht eingeben:")
            tmW = input("")
        elif wInput == "2":
            print("Neues Gewicht eingeben:")
            tfW = input("")
        elif wInput == "3":
            print("Neues Gewicht eingeben:")
            tsW = input("")
        elif wInput == "4":
            print("Neues Gewicht eingeben:")
            tbW = input("")
        elif wInput == "5":
            print("Neues Gewicht eingeben:")
            tdW = input("")
        elif wInput == "6":
            print("Neues Gewicht eingeben:")
            tsGW = input("")
        elif wInput == "7":
            print("Neues Gewicht eingeben:")
            trW = input("")
        elif wInput == "8":
            print("Neuen Speed eingeben:")
            speed = input("")

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
    global aboCount
    global sGlAMT

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
            (3) GiftSubs
Du hast: {money} €""")
    
    time.sleep(1.5)
    
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
    
    if shopinput == "3":
        print("""Wie viele GiftSubs sollen es sein?
              (1) 1 - 10€
              (2) 3 - 27€
              (3) 5 - 40€
              (4) 10 - 75€
              (5) 20 - 125€
              (6) Custom (max. 50 - 500€)""")

        subGiftInput = input("")
        
        if subGiftInput == "1":
            if money < 10:
                print("Du hast nicht genug Geld!")
            else:
                choiceName()
                money = money - 10
                aboCount += 1
                money += 2
                addAbo()
                subGiftLongAboMessage = sGlAMT.replace("{randomName}", randomName).replace("{aboLenght[randomName]}", str(aboLength[randomName]))
                print(subGiftLongAboMessage)
                print("Du giftest 1 Sub!")
                pyttsx3.speak("Du giftest 1 Sub!")
        elif subGiftInput == "2":
            if money < 27:
                print("Du hast nicht genug Geld!")
            else:
                money = money - 27
                shopSubGifts = 3
                while shopSubGifts > 0:
                    choiceName()
                    shopSubGifts -= 1
                    aboCount += 1
                    addAbo()
                    subGiftLongAboMessage = sGlAMT.replace("{randomName}", randomName).replace("{aboLenght[randomName]}", str(aboLength[randomName]))
                    print(subGiftLongAboMessage)
                    money += 2
                    time.sleep(0.08)
                print("Du giftest 3 Subs!")
                pyttsx3.speak("Du giftest 3 Subs!")
        elif subGiftInput == "3":
            if money < 40:
                print("Du hast nicht genug Geld!")
            else:
                money = money - 40
                shopSubGifts = 5
                while shopSubGifts > 0:
                    choiceName()
                    shopSubGifts -= 1
                    aboCount += 1
                    addAbo()
                    subGiftLongAboMessage = sGlAMT.replace("{randomName}", randomName).replace("{aboLenght[randomName]}", str(aboLength[randomName]))
                    print(subGiftLongAboMessage)
                    money += 2
                    time.sleep(0.08)
                print("Du giftest 5 Subs!")
                pyttsx3.speak("Du giftest 5 Subs!")
        elif subGiftInput == "4":
            subGiftLongAboMessage = sGlAMT.replace("{randomName}", randomName).replace("{aboLenght[randomName]}", str(aboLength[randomName]))
            if money < 75:
                print("Du hast nicht genug Geld!")
            else:
                money = money - 75
                shopSubGifts = 10
                while shopSubGifts > 0:
                    choiceName()
                    shopSubGifts -= 1
                    aboCount += 1
                    addAbo()
                    subGiftLongAboMessage = sGlAMT.replace("{randomName}", randomName).replace("{aboLenght[randomName]}", str(aboLength[randomName]))
                    print(subGiftLongAboMessage)
                    money += 2
                    time.sleep(0.08)
                print("Du giftest 10 Subs!")
                pyttsx3.speak("Du giftest 10 Subs!")
        elif subGiftInput == "5":
            if money < 125:
                print("Du hast nicht genug Geld!")
            else:
                money = money - 125
                shopSubGifts = 20
                while shopSubGifts > 0:
                    choiceName()
                    shopSubGifts -= 1
                    aboCount += 1
                    addAbo()
                    subGiftLongAboMessage = sGlAMT.replace("{randomName}", randomName).replace("{aboLenght[randomName]}", str(aboLength[randomName]))
                    print(subGiftLongAboMessage)
                    money += 2
                    time.sleep(0.08)
                print("Du giftest 20 Subs!")
                pyttsx3.speak("Du giftest 20 Subs!")
        elif subGiftInput == "6":
            customSubInput = input("Wie viele sollen es sein?: ")
            customSubMoney = int(customSubInput) * 10
            if money < int(customSubMoney):
                print("Du hast nicht genug Geld!")
            else:
                money = money - customSubMoney
                shopSubGifts = int(customSubInput)
                while int(shopSubGifts) > 0:
                    choiceName()
                    shopSubGifts -= 1
                    aboCount += 1
                    addAbo()
                    subGiftLongAboMessage = sGlAMT.replace("{randomName}", randomName).replace("{aboLenght[randomName]}", str(aboLength[randomName]))
                    print(subGiftLongAboMessage)
                    money += 2
                    time.sleep(0.08)
                print(f"Du giftest {customSubInput} Subs!")
                pyttsx3.speak(f"Du giftest {customSubInput} Subs!")

    pause = False

def streamMonth():
    global statisticMonth, on, statistic
    global monthFollower, monthMoney, monthBits, monthRaids, month
    global xp, lvl

    on = True

    oldlvl = lvl
    newXp = monthFollower * 2 + monthMoney * 3 + (monthBits / 33.333333) + (monthRaids * 10)
    newXp = round(newXp, 0)
    xp = int(xp)
    xp += int(newXp)
    # Level 2 = 30 XP / Level 3 = 160 XP / Level 5 = 960 XP / Level 7 = 2880 XP
    # Level 10 = 8910 XP / Level 15 = 31360 XP / Level 20 = 75810 XP / Level 25 = 149760 XP
    # Level 30 = 260710 XP / Level 40 = 623610 XP / Level 50 = 1224510 XP / Level 100 = 9899010 XP
    needXp = lvl * lvl * (2 + lvl) * 10
    
    if xp > needXp:
        lvl += 1

    print(f"""
          Du hast den {month}. Monat abgeschlossen!
          in diesem Monat hast du:
          {monthFollower} neue Follower bekommen!
          {monthMoney} € bekommen!
          {monthBits} Bits bekommen!
          Außerdem wurdest du {monthRaids}x geraidet!""")
    
    time.sleep(3)

    if oldlvl < lvl:
        needXp = lvl * lvl * (2 + lvl) * 10
        print(f"""
              Dafür bekommst du {newXp} XP und
              steigst in Level {lvl} auf!
              Für das nächste Level benötigst du
              nun {needXp} XP.
              """)
    
    elif oldlvl == lvl:
        print(f"""
              Dafür bekommst du {newXp} XP und
              bleibst in Level {lvl}!
              Du hast nun {xp}/{needXp} XP für
              das nächste Level.
              """)

    statisticMonth += 1

    time.sleep(2)

    monthMoney = 0
    monthBits = 0
    monthFollower = 0
    monthRaids = 0
    newXp = 0
    month += 1

    statistic = False
    on = False

def bitsInMoney():
    global bits
    global money
    global pause
    pause = True
    
    print(f"Du hast {bits} Bits, wie viele möchtest du in € umwandeln?")
    
    bitsInput = input("Bitte eine Zahl eingeben: ")

    if int(bitsInput) > bits:
        print("Du hast leider nicht genug Bits!")
    else:
        bMoney = int(bitsInput) / 100 * 0.81
        bMoney = round(bMoney, 2)
        money += bMoney
        bits -= int(bitsInput)
        print(f"""Vielen Dank für die Umwandlung!
              Du hast nun für {bitsInput} Bits,
              {bMoney}€ bekommen!""")

    pause = False

loadDataQ = input("Data Laden? (Ja/Nein): ")
saveDataQ = input("Data Saven? (Ja/Nein): ")

if saveDataQ == "Ja":
    saveDataFile = input("Datei-Namen: ") # C:\Users\User\Documents\funtests\FakeStream\FakeStreamTest\test1.txt oder dein pfad wo du speichern willst

if loadDataQ == "Ja":
    loadDataFile = input("Datei-Namen: ") # C:\Users\User\Documents\funtests\FakeStream\FakeStreamTest\test1.txt oder dein pfad wo du speichern willst
    followCount, aboCount, money, bits, fMT, nAMT, lAMT, bMT, dMT, sGMT, rTM, aboLength, lvl, xp, month = load_data_from_file(loadDataFile)

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

if loadDataQ == "Nein":
    tutorialQ = input("Brauchst du ein Tutorial? (Ja/Nein): ")

    if tutorialQ == "Ja":
        tutorial1()

    elif tutorialQ == "Nein":
        followCount = 50

keyboard.add_hotkey("w + 3", werbung30)
keyboard.add_hotkey("alt + shift", configuration)
keyboard.add_hotkey("alt + a", abstimmung)
keyboard.add_hotkey("alt + s", shop)
keyboard.add_hotkey("alt + b", bitsInMoney)

choiceName()

while True:
    global timer

    if statistic == False:
        statistic = True
        threading.Timer(300, streamMonth).start()

    if pause == False and on == False:
        if start1 == True:
            timer = 1

        elif followCount >= 0 and followCount < 50:
            timer = random.uniform(1, 1.5) / (aboCount + 1) * 5
            if timer > 1.5:
                timer = 1.5

        elif followCount >= 50 and followCount < 500:
            timer = random.uniform(1.5, 2.4) / (aboCount + 1) * 15
            if timer > 2.4:
                timer = 2.4
        
        elif followCount >= 500 and followCount < 1000:
            timer = random.uniform(1.6, 2) / (aboCount + 1) * 30
            if timer > 2:
                timer = 2

        elif followCount >= 1000 and followCount < 2500:
            timer = random.uniform(1.4, 1.8) / (aboCount + 1) * 60
            if timer > 1.8:
                timer = 1.8
        
        elif followCount >= 2500 and followCount < 5000:
            timer = random.uniform(1.3, 1.6) / (aboCount + 1) * 100
            if timer > 1.6:
                timer = 1.6

        elif followCount >= 5000 and followCount < 10000:
            timer = random.uniform(1.2, 1.5) / (aboCount + 1) * 175
            if timer > 1.5:
                timer = 1.5
            
        elif followCount >= 10000:
            timer = random.uniform(1.1, 1.35) / (aboCount + 1) * 300
            if timer > 1.35:
                timer = 1.35

        if spectator < 3:
            sspectator = 3

        else:
            sspectator = spectator

        time.sleep(timer * (sspectator / 5))

        choiceType()

        if randomMessageType == [1]:
            choiceName()
            choiceMessage()

            print(randomName + ": " + randomMessage)

            reply()

        if randomMessageType == [2]:
            choiceName()

            followMessage = fMT.replace("{randomName}", randomName)

            followCount += 1
            monthFollower += 1
            
            print(f"""{followMessage}
                Follow Count: {followCount}""")
            if fSound == True:
                pyttsx3.speak(f"{randomName} folgt!")
        
        if randomMessageType == [3] and followCount >= 20:
            choiceName()

            aboCount += 1
            money += 2
            monthMoney += 2

            addAbo()

            if aboLength[randomName] == 1:
                
                newAboMessage = nAMT.replace("{randomName}", randomName).replace("{money}", str(money)).replace("{aboCount}", str(aboCount))

                print(newAboMessage)

                if sound == True:
                    pyttsx3.speak(f"{randomName} subt!")

            elif aboLength[randomName] >= 2:
                choiceSubMessage()

                longAboMessage = lAMT.replace("{randomName}", randomName).replace("{money}", str(money)).replace("{aboLenght[randomName]}", str(aboLength[randomName])).replace("{randomSubMessage}", str(randomSubMessage))

                print(longAboMessage)

                if sound == True:
                    pyttsx3.speak(f"{randomName}, Abonniert im {aboLength[randomName]}. Monat! {randomSubMessage}")
                
                time.sleep(timer * 3)

        if randomMessageType == [4] and followCount >= 50:
            choiceName()
            bitsValue = [50, 200, 500, 1200, 2500, 4000, 7500, 12000, 25000]
            bitsPlus = random.choices(bitsValue, weights=(75, 15, 6, 2, 1.2, 0.6, 0.1, 0.07, 0.03), k=1)
            bits += bitsPlus[0]
            monthBits += bitsPlus[0]

            bitsMessage = bMT.replace("{randomName}", randomName).replace("{bits}", str(bits)).replace("{bitsPlus}", str(bitsPlus))

            print(bitsMessage)
            if sound == True:
                pyttsx3.speak(f"{randomName} spendet {bitsPlus[0]} Bits!")

        if randomMessageType == [5] and followCount >= 50:
            choiceName()
            moneyValue = [1, 2, 3, 5, 10, 20, 30, 50, 100]
            moneyPlus = random.choices(moneyValue, weights=(75, 15, 6, 2, 1.2, 0.6, 0.1, 0.07, 0.03), k=1)
            money += moneyPlus[0]
            monthMoney += moneyPlus[0]

            donationMessage = dMT.replace("{randomName}", randomName).replace("{money}", str(money)).replace("{moneyPlus}", str(moneyPlus))

            print(donationMessage)

            if sound == True:
                pyttsx3.speak(f"{randomName} spendet {moneyPlus[0]} €")
        
        if randomMessageType == [6] and followCount >= 35:
            choiceName()

            giftSubsList = [1, 3, 5, 10, 20]
            giftSubsWeight = [25, 50, 30, 10, 3]

            giftSubs = random.choices(giftSubsList, giftSubsWeight, k=1)

            subGiftMessage = sGMT.replace("{randomName}", randomName).replace("{giftSubs}", str(giftSubs))

            randomSpeakName = randomName
            speakGiftSubs = giftSubs
            giftSubs = giftSubs[0]

            if sound == True:
                pyttsx3.speak(f"{randomSpeakName} giftet {speakGiftSubs} Subs!")

            while giftSubs > 0:
                choiceName()

                aboCount += 1
                money += 2
                monthMoney += 2

                addAbo()

                subGiftLongAboMessage = sGlAMT.replace("{randomName}", randomName).replace("{aboLenght[randomName]}", str(aboLength[randomName]))

                print(subGiftLongAboMessage)

                giftSubs -= 1

                time.sleep(0.05)
            
            subGiftMessage = subGiftMessage.replace("{money}", str(money)).replace("{aboCount}", str(aboCount))

            print(subGiftMessage)

            time.sleep(timer * 3)
        
        if randomMessageType == [7] and followCount >= 50:
            choiceName()

            monthRaids += 1

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
            monthFollower += newFollower

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
