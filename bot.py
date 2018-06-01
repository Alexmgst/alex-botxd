import discord
import asyncio
import random
import time
from discord.ext import commands
from pytube import YouTube
import logging
import praw
import bs4 as bs
import urllib.request
import lxml
global url
global times_took
reddit = praw.Reddit(client_id="JC1EfGldDUnJyQ", client_secret="X0vAkLJHeXAt6Drkrw4AW7cs6AE",password="DeniaOliva2",user_agent="SKRIPT v. DiscordBot", username="al3xmg5t")
meme_subreddit = reddit.subreddit("memes")
times_took = 0
chars = ["q","w","e","r","t","z","u","i","o","p","a","s","d","f","g","h","j","k","l","y","x","c","v","b","n","m","Q","W","R","E","T","Z","U","I","O","P","A","S","D","F","G","H","J","K","L","Y","X","C","V","B","N","M"]

logging.basicConfig(level=logging.INFO)
client = discord.Client()


soup = urllib.request.urlopen("http://www.spiegel.de/schlagzeilen/").read()
soup_object = bs.BeautifulSoup(soup,"lxml")

    

global inChannel
global player



inChannel = False







bad_words = ["idiot","arsch", "opfer","arschloch","noob","wichser","muesslimaxxxe","blödian","kek","spast","fick dich", "du bist dumm","ficker","dummer","cock", "spasti","cunt","fuck","hure","hurensohn","ich hasse dich","fettsack","dickwanst","kys","suckt","scheisser","scheisshaufen","scheiße","scheisse","stfu","fett"]

jokes = ["Neulich im Kino Verkäuferin: Das Popcorn süß oder salzig? Er: So wie meine Freundin. Verkäuferin: Hässliche Popcorn haben wir nicht!", "Wenn ein Yogalehrer seine Beine senkrecht nach oben streckt und dabei furzt, welche Yoga Figur stellt er da? Eine Duftkerze.","Was ist der gefährliste Tag für ein Uboot ? -Tag der offen Tür","Wie nennt man einen übergewichtigen Vegetarier? Biotonne.", "Lehrer: So Tom du gehst jetzt vor die Tür dein Gelaber interessiert keinen! Schüler: Dann können sie ja gleich mitkommen!", "Warum freut sich eine Blondine so, wenn sie ein Puzzle nach 6 Monaten fertig hat? – Weil auf der Packung steht: 2-4 Jahre.", "Wie nennen Chinesen einen Oberschenkelbruch? Knacki Knacki nah bei Sacki","Warum macht die Blondiene ihren Jogurt schon im Supermarkt auf?Weil drauf steht hier öffnen","Was steht auf dem Grabstein eines Mathematikers? – Damit hat er nicht gerechnet.","Was sagt ein Hai, nachdem es einen Surfer gefressen hat?- Nett serviert, so mit Frühstücksbrettchen"," Deine Mudda heißt Dieter und ist der Haarigste im Zoo.","Deine Mutter ist so hässlich, dein Vater nimmt sie mit auf die Arbeit, damit er ihr kein Abschiedskuss geben muss.", "Deine Mutter ist so fett und hässlich. Sie kann einen ganzen Mob aufhalten.", "Wenn euer Familienhund deine Mudda beim essen zuschaut, bekommt er einen Würgreiz.", "Manche Personen hatten echt eine schwierige Kindheit. Bei anderen wurde die Schaukel einfach zu nah an der Hauswand gebaut.", "Manchmal trinke ich Wasser, um meine Leber zu überraschen.","Ich bin nicht gefallen. Ich habe den Boden attackiert.", "Wie war eigentlich die Stimmung in der DDR? Sie hielt sich so ziemlich in Grenzen.","Wir essen jetzt Tante Berta. Satzzeichen können Leben retten."]




token = "Mzg3OTg1Mzk0Mzg3NTE3NDQw.DQmdCQ.2C1TRBOjmu-in6wukZmew5G9-Sc"
changed = False
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Noobs boosten"))





commands = {
            "!news" : "Die aktuellsten News geliefert",
            "!coinflip" : "Ein virtueller Münzwurf",
            "!witz" : "Ein lustiger Witz",                        
            "!role : Rolle  ":"Verleiht sich eine Rolle (Ausser Admin!)",
            "!quickmaths : Aufgabe" : "Rechnet eine Matheaufgabe aus.",
            "!meme" : "Sendet ein meme"
            }
            



        
        
@client.event
async def on_message(message):
    global url
    global soup2
    global soup_object2
    global meme
    global hot_memes
    global channel
    global inChannel
    global voice
    global player
    global error_count
    global gamer
    sentence = message.content.lower().split()
    
    for word in sentence:
        if word in bad_words:
            if message.author.name != "alex-botxd":
               
                await client.send_message(message.channel, "Nicht beleidigen bzw. fluchen @" +  str(message.author) + "Wenn das so weiter geht, werden deine Nachrichten zensiert!")
    if message.content.startswith("!nicoistdumm"):
        await client.send_message(message.channel, "Das stimmt" + str(message.author))
    elif message.content.lower().startswith("!meme"):
        if message.channel.name == "memes":
            hot_memes = meme_subreddit.hot(limit = 1000)
            random_meme = random.randint(0,30)
            count = 0
            for submission in hot_memes:
                count += 1
                if count == random_meme:
                    meme = submission.url
                    hot_memes = meme_subreddit.hot(limit = 100)
                    await client.send_message(message.channel,meme)
                    break
    elif message.content.lower().startswith("!news"):
        for text in soup_object.find_all("div",class_="schlagzeilen-content schlagzeilen-overview"):
            info = (str(text.text)[:1900] + '...')
            new_info = info.replace("\n", "")
            await client.send_message(message.channel,str(new_info))
            
        

    elif message.content.lower().startswith("!witz"):
        await client.send_message(message.channel, "Witz des Tages: " + random.choice(jokes) + " <:yay:450746929702371328> <:yay:450746929702371328>")
    elif message.content.lower().startswith("!role"):
        if "moderator" in [y.name.lower() for y in message.author.roles]:

            command,role_name = message.content.split(" : ")
             
            for role in message.server.roles:
                if role.name == role_name:
                    role_id = role.id
                
                    try:
                    
                        await client.add_roles(message.author, role)
                        await client.send_message(message.channel," Dir wurde die Rolle " + role.name +" verliehen.")
                    except Exception as e:
                        await client.send_message(message.channel,"Ich kann dir diese Rolle nicht geben, da: " + str(e))
                    break  
        else:
            await client.send_message(message.channel," Du bist ein noob und daher zu dumm, um dir eine Rolle zu hacken")
                         
    elif message.content.lower().startswith("!quickmaths : "):
        try:
            maths = str(message.content).split(" : ")[1]
            result = eval(maths)
            await client.send_message(message.channel,"Das Ergebnis der Aufgabe: " + str(result))
        except:
            await client.send_message(message.channel,"Leider konnte ich diese Aufgabe nicht rechnen. :sob:  ")
    elif message.content.startswith("!coinflip"):
        zahl = random.randint(1,2)
        if zahl == 1:
            result = "kopf"
        else:
            result = "zahl"
        await client.send_message(message.channel,result)




    
    elif message.content.startswith("?commands"):
        await client.send_message(message.channel, str(commands))
  
        
         
        
        
client.run(token)
