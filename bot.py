import discord
import asyncio
import random
import time
from discord.ext import commands
import mutagen
from mutagen.mp3 import MP3
import subprocess
import logging
import praw
import bs4 as bs
import urllib.request
import lxml

reddit = praw.Reddit(client_id="JC1EfGldDUnJyQ", client_secret="X0vAkLJHeXAt6Drkrw4AW7cs6AE",password="DeniaOliva2",user_agent="SKRIPT v. DiscordBot", username="al3xmg5t")
meme_subreddit = reddit.subreddit("memes")
hot_memes = meme_subreddit.hot(limit = 1000)


logging.basicConfig(level=logging.INFO)
client = discord.Client()


soup = urllib.request.urlopen("http://www.spiegel.de/schlagzeilen/").read()
soup_object = bs.BeautifulSoup(soup,"lxml")

    

global inChannel
global player



inChannel = False







bad_words = ["idiot","arsch", "opfer","arschloch","noob","wichser","muesslimaxxxe","blödian","kek","spast","fick dich", "du bist dumm","ficker","dummer","cock", "spasti","cunt","fuck","hure","hurensohn","ich hasse dich","fettsack","dickwanst","kys","suckt","scheisser","scheisshaufen","scheiße","scheisse"]




changed = False
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Noobs boosten"))



if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')



commands = {"!summon" : "Joint dem voice channel",
            "!news" : "Die aktuellsten News geliefert",
            "!coinflip" : "Ein virtueller Münzwurf",
            "!nicoistdumm" : "...",
            "!krabbelante" : "Schickt ein Foto von Krabbelante",
            "!schweinepriester" : "Sendet ein Bild des obersten schweinepriesters",            
            "!role : Rolle  ":"Verleiht sich eine Rolle (Ausser Admin!)",
            "!quickmaths : Aufgabe" : "Rechnet eine Matheaufgabe aus.",
            "!meme" : "Sendet ein meme"
            }
            

    
@client.event
async def on_message(message):
    global meme
    global hot_memes    
    global inChannel
    global voice
    global player
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
            
        

                                  
    elif message.content.startswith("!role"):
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
    elif message.content.startswith("!summon"):
        try:
            channel = message.author.voice_channel
            voice = await client.join_voice_channel(channel)
            inChannel = True
        except discord.InvalidArgument:
            await client.send_message(message.channel, " Da ist leider etwas schiefgelaufen!")            
        except discord.ClientException:
            await client.send_message(message.channel, "Ich bin bereits in einem Voice Channel!")
    elif message.content.startswith("!disconnect"):
        await client.send_message(message.channel,"bye bye")
        inChannel = False
        await client.logout()
    elif message.content.startswith("!krabbelante"):
        await client.send_file(message.channel,"krabbe.png")

    elif message.content.startswith("!schweinepriester"):
        await client.send_file(message.channel, "images.jpg")
    
    elif message.content.startswith("?commands"):
        await client.send_message(message.channel, str(commands))

client.run("Mzg3OTg1Mzk0Mzg3NTE3NDQw.DQmdCQ.2C1TRBOjmu-in6wukZmew5G9-Sc")
