import telebot, configparser, os, json, logging, datetime, sys, random, time, schedule
from telebot import types

config = configparser.ConfigParser()
config.read('config.ini')
tokn = config['Telegram']['tokn']


bot = telebot.TeleBot(f'{tokn}')
telebot.logger.setLevel(logging.DEBUG)

helloes = {"Afrikaans":    "Hello Wêreld!",
"Albanian":     "Përshendetje Botë!",
"Amharic":      'ሰላም ልዑል!',
"Armenian":     'Բարեւ աշխարհ!',
"Basque":       'Kaixo Mundua!',
"Belarussian":  'Прывітанне Сусвет!',
"Bengali":      'ওহে বিশ্ব!',
"Bulgarian":    'Здравей свят!',
"Catalan":      'Hola món!',
"Chichewa":     'Moni Dziko Lapansi!',
"Chinese":      '你好世界!',
"Croatian":     'Pozdrav svijete!',
"Czech":        'Ahoj světe!',
"Danish":       'Hej Verden!',
'Dutch':        'Hallo Wereld!',
"English":      'Hello World!',
"Estonian":     'Tere maailm!',
"Finnish":      'Hei maailma!',
"French":       'Bonjour monde!',
"Frisian":      'Hallo wrâld!',
"Georgian":     'გამარჯობა მსოფლიო!',
"German":       'Hallo Welt!',
'Greek':        'Γειά σου Κόσμε!',
"Hausa":        'Sannu Duniya!',
"Hindi":        'नमस्ते दुनिया!',
"Hungarian":    'Helló Világ!',
"Icelandic":    'Halló heimur!',
"Igbo":         'Ndewo Ụwa!',
"Indonesian":   'Halo Dunia!',
"Italian":      'Ciao mondo!',
"Japanese":     'こんにちは世界！',
"Kazakh":       'Сәлем Әлем!',
"Khmer":        'សួស្តី​ពិភពលោក!',
"Kyrgyz":       'Салам дүйнө!',
"Lao":          'ສະ​ບາຍ​ດີ​ຊາວ​ໂລກ!',
"Latvian":      'Sveika pasaule!',
"Lithuanian":   'Labas pasauli!',
"Luxemburgish": 'Moien Welt!',
"Macedonian":   'Здраво свету!',
"Malay":        'Hai dunia!',
"Malayalam":    'ഹലോ വേൾഡ്!',
"Mongolian":    'Сайн уу дэлхий!',
"Myanmar":      'မင်္ဂလာပါကမ္ဘာလောက!',
"Nepali":       'नमस्कार संसार!',
"Norwegian":    'Hei Verden!',
"Polish":       'Witaj świecie!',
"Portuguese":   'Olá Mundo!',
"Punjabi":     ' ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਦੁਨਿਆ!',
"Romanian":     'Salut Lume!',
"Russian":      'Привет мир!',
'Scots Gaelic': 'Hàlo a Shaoghail!',
"Serbian":      'Здраво Свете!',
"Sesotho":      'Lefatše Lumela!',
"Sinhala":      'හෙලෝ වර්ල්ඩ්!',
"Slovenian":    'Pozdravljen svet!',
"Spanish":      '¡Hola Mundo!',
"Sundanese":    'Halo Dunya!',
"Swahili":      'Salamu Dunia!',
"Swedish":      'Hej världen!',
"Tajik":        'Салом Ҷаҳон!',
"Thai":         'สวัสดีชาวโลก!',
"Turkish":      'Selam Dünya!',
"Ukrainian":    'Привіт Світ!',
'Uzbek':        'Salom Dunyo!',
"Vietnamese":   'Chào thế giới!',
"Welsh":        'Helo Byd!',
"Xhosa":        'Molo Lizwe!',
'Yoruba':       'Mo ki O Ile Aiye!',
'Zulu':         'Sawubona Mhlaba!'}

def hello():
    hello_list = list(helloes.items())
    hello_lang = random.choice(hello_list)
    res = hello_lang[1]
    return (res)
schedule.every(1).minutes.do(hello)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'{hello()} I will work, if you\'ll add me in any group chat! Also, I have bad memory and only will remember those, who joined after me! Use me with /loser and use /reset to delete my memory about chat members! :-) ')

@bot.message_handler(commands=['reset'])
def reset_message(message):
    chatId = message.chat.id
    chat_file_name = f'chats/{chatId}.json'
    try:
        os.remove(chat_file_name)
        bot.send_message(chatId, f'Oops! It seems, that I forgot chat members again! :/ ')
    except FileNotFoundError:
        bot.send_message(chatId, f'What? It\'s not like I remember anyone at all :|')


@bot.message_handler(content_types=['new_chat_members'])
def handler_new_member(message):

    day = datetime.datetime.now().strftime('%d')
    user_name = message.new_chat_members[0].username
    chatId = message.chat.id
    chat_file_name = f'chats/{chatId}.json'

    new_usr = [user_name]

    if user_name == 'DailyLoserBot':
        bot.send_message(chatId, f'{hello()} I will remember new ones, that will join this group chat! :D')
    else:
        if os.path.exists(chat_file_name) == False:
            with open(chat_file_name, 'w') as chat_create:
                json.dump(new_usr, chat_create)
        else:
            with open(chat_file_name, 'r') as chat_open:
                data = json.load(chat_open)
                if user_name in data:
                    pass
                else:
                    data.append(user_name)
                    with open(chat_file_name, "w") as updated_file:
                        json.dump(data, updated_file)
    
        bot.send_message(chatId, f'{hello()} @{user_name}, a-ha, I will remember your name >;)')


@bot.message_handler(commands=['loser'])
def loser(message):

    chatId = message.chat.id
    chat_file_name = f'{chatId}.json'

    try:
        with open('chats/' + chat_file_name, 'r') as chat_open:
            data = json.load(chat_open)
            user_name = random.choice(data)
            bot.send_message(chatId, f'{hello()} Today\'s loser is @{user_name} (:')
    except FileNotFoundError:
        bot.send_message(chatId, 'Don\'t remember anyone! :o')


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nExiting by user request.\n')
        sys.exit(0)