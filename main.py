import logging
import telegram
import datetime
from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import Updater, CommandHandler, CallbackContext, InlineQueryHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

bot = telegram.Bot(token='')
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Pff loser \U0001F612')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Use me in group chats please :-)')


def loser(update: Update, context: CallbackContext) -> None:
    date = datetime.datetime.now().strftime("%d")
    query_user_name = update.inline_query.from_user.name
    result = [
        InlineQueryResultArticle(
            id='loser',
            title='Today\'s loser?',
            input_message_content=InputTextMessageContent('Hello! Today\'s loser is %s :-)' % query_user_name)
        ),
    ]
    update.inline_query.answer(result)



def main() -> None:
    upd = Updater('')
    dp = upd.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(InlineQueryHandler(loser))

    upd.start_polling()
    upd.idle()


if __name__ == '__main__':
    main()