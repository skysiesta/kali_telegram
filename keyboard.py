from telebot.types import ReplyKeyboardMarkup,KeyboardButton,KeyboardButtonPollType,ReplyKeyboardRemove

keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard.row('art_com', 'update', 'advice', 'anime', 'manga')
keyboard.row('rus', 'eng')
keyboard.row('help')

keyboardART = ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
keyboardART.row('art', 'azurlane', 'blade', 'darling', 'genshin')
keyboardART.row('neko', 'rezero', 'succubs', 'tate', 'tensura')
keyboardART.row('vtubers', 'back')
