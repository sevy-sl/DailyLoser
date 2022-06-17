import json
import discord
import random
import datetime
from discord.ext import commands

config_file = open('config.json')
config = json.load(config_file)

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '~', intents=intents, help_command=None)

day = datetime.datetime.now().strftime("%d")
random.seed(day)

helloes_dict = {'Afrikaans':	'Hello Wêreld',
    'Albanian':	'Përshendetje Botë',
    'Amharic':	'ሰላም ልዑል',
    'Armenia':	'Բարեւ աշխարհ',
    'Basque':	'Kaixo Mundua',
    'Belarussian':	'Прывітанне Сусвет',
    'Bengali':	'ওহে বিশ্ব',
    'Bulgarian':	'Здравей свят',
    'Catalan':	'Hola món',
    'Chichewa':	'Moni Dziko Lapansi',
    'Chinese':	'你好世界',
    'Croatian':	'Pozdrav svijete',
    'Czech':	'Ahoj světe',
    'Danish':	'Hej Verden',
    'Dutch':	'Hallo Wereld',
    'English':	'Hello World',
    'Estonian':	'Tere maailm',
    'Finnish':	'Hei maailma',
    'French':	'Bonjour monde',
    'Frisian':	'Hallo wrâld',
    'German':	'Hallo Welt',
    'Greek':	'Γειά σου Κόσμε',
    'Hausa':	'Sannu Duniya',
    'Hindi':	'नमस्ते दुनिया',
    'Hungarian':	'Helló Világ',
    'Icelandic':	'Halló heimur',
    'Igbo':	'Ndewo Ụwa',
    'Indonesian':	'Halo Dunia',
    'Italian':	'Ciao mondo',
    'Kazakh':	'Сәлем Әлем',
    'Kyrgyz':	'Салам дүйнө',
    'Latvian':	'Sveika pasaule',
    'Lithuanian':	'Labas pasauli',
    'Luxemburgish':	'Moien Welt',
    'Macedonian':	'Здраво свету',
    'Malay':	'Hai dunia',
    'Mongolian':	'Сайн уу дэлхий',
    'Norwegian':	'Hei Verden',
    'Polish':	'Witaj świecie',
    'Portuguese':	'Olá Mundo',
    'Romanian':	'Salut Lume',
    'Russian':	'Привет мир',
    'Scots Gaelic':	'Hàlo a Shaoghail',
    'Serbian':	'Здраво Свете',
    'Sesotho':	'Lefatše Lumela',
    'Slovenian':	'Pozdravljen svet',
    'Spanish':	'¡Hola Mundo',
    'Sundanese':	'Halo Dunya',
    'Swahili':	'Salamu Dunia',
    'Swedish':	'Hej världen',
    'Tajik':	'Салом Ҷаҳон',
    'Thai':	'สวัสดีชาวโลก',
    'Turkish':	'Selam Dünya',
    'Ukrainian':	'Привіт Світ',
    'Uzbek':	'Salom Dunyo',
    'Vietnamese':	'Chào thế giới',
    'Welsh':	'Helo Byd',
    'Xhosa':	'Molo Lizwe',
    'Yoruba':	'Mo ki O Ile Aiye',
    'Zulu':	'Sawubona Mhlaba'
}

helloes_list = list(helloes_dict.items())
hello_item = random.choice(helloes_list)
language = hello_item[0]
hello = hello_item[1]

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

@client.event
async def on_message(message):
    if message.content == 'loser?':
        guildId = message.guild.id
        guild = client.get_guild(guildId)
        losers = guild.members
        for member in losers:
            if member.bot == True:
                losers.remove(member)
            else:
                pass
        random.seed(day)
        loser = random.choice(losers)   
        await message.channel.send(f'{hello} ({language})! Today\'s loser is {loser.mention} :-)', reference=message)

@client.command()
async def help(ctx):
    await ctx.send("Ask me 'loser?' and I will tell you, who's loser today :D")

client.run(config['token'])