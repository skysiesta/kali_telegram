from multiprocessing import Process
import threading
def t_art():
    import telebot, requests, random, sys, os, re
    # ИМПОРТ СОБСТВЕННЫХ МОДУЛЕЙ
    # sys.path.insert(0, '/home/skysiesta/bot/t_bot/aneks')
    sys.path.insert(0, '/home/skysiesta/Рабочий стол/telegram/anime_bot/search/')
    sys.path.insert(0, '/home/skysiesta/Рабочий стол/telegram/anime_bot/cartoon/')
    sys.path.insert(0, '/home/skysiesta/Рабочий стол/telegram/anime_bot/audio/')
    import animeSearch, gsearch, cartoon, audio, adv, keyboard
    import r_youtube
    from random_words import RandomWords
    api = 'МОЙ АПИ'
    bot = telebot.TeleBot(api)

    # ОБРАБОТКА ФОТОГРАФИЙ ОТ ПОЛЬЗОВАТЕЛЯ
    @bot.message_handler(content_types=['photo'])
    def get_text_messages(message):
        if message:
            def pho():
                # print(message.json['photo'][0]['file_id'])
                file_id = message.json['photo'][0]['file_id']
                response = requests.get('https://api.telegram.org/bot' + api + '/getFile?file_id=' + file_id)

                response = response.json()
                photo_path = response['result']['file_path']

                # ЗАГРУЗКА ФОТОГРАФИИ
                photo_download_url = 'https://api.telegram.org/file/bot' + api + '/' + photo_path
                download = requests.get(photo_download_url, allow_redirects=True)
                name = 'cartoon/' + str(random.randrange(20000)) + '.jpg'
                open(name, 'wb').write(download.content)
                
                # ОБРАБОТКА ФОТОГРАФИИ С ПОМОЩЬЮ САМОПИСНОГО МОДУЛЯ
                cartoon.colorize(name)

                bot.send_photo(message.from_user.id, open(name, 'rb'))
                os.remove(name)
            # МУЛЬТИТРЕДИНГ
            pho2 = threading.Thread(target=pho)
            pho2.start()

    # ГОЛОСОВОЕ УПРАВЛЕНИЕ - ПЕРЕВОД ТЕКСТА НА ЯПОНСКИЙ ЯЗЫК
    @bot.message_handler(content_types=['voice'])
    def get_text_messages(message):
        if message:
            def trans():
                try:
                    file_id = message.json['voice']['file_id']
                    response = requests.get('https://api.telegram.org/bot' + api + '/getFile?file_id=' + file_id)

                    response = response.json()
                    audio_path = response['result']['file_path']

                    # ЗАГРУЗКА ФАЙЛА С ГОЛОСОМ ПОЛЬЗОВАТЕЛЯ
                    audio_download_url = 'https://api.telegram.org/file/bot' + api + '/' + audio_path
                    download = requests.get(audio_download_url, allow_redirects=True)
                    name = 'audio/' + str(random.randrange(20000)) + '.wav'
                    open(name, 'wb').write(download.content)
                    any_name = str(random.randrange(20000))
                    # ОБРАБОТКА ГОЛОСА ПОЛЬЗОВАТЕЛЯ И ПЕРЕВОД
                    audio.ru_ja(name, any_name)

                    bot.send_audio(message.from_user.id, open(name, 'rb'))
                    os.remove(name)
                except Exception as e:
                    pass
            trans2 = threading.Thread(target=trans)
            trans2.start()

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        # СПИСОК ОБНОВЛЕНИЙ
        if message.text == "update":
            def upd():
                if str(message.from_user.id) in open('database/rus.txt').read().split():
                    lines = ''.join(open("update_rus.txt").readlines())
                    bot.send_message(message.from_user.id, lines)
                elif str(message.from_user.id) in open('database/eng.txt').read().split():
                    lines = ''.join(open("update.txt").readlines())
                    bot.send_message(message.from_user.id, lines)
                else:
                    lines = ''.join(open("update.txt").readlines())
                    bot.send_message(message.from_user.id, lines)
            upd2 = threading.Thread(target=upd)
            upd2.start()
        # ХЕЛП/ПОМОЩЬ
        elif message.text == "help":
            def helpm():
                if str(message.from_user.id) in open('database/rus.txt').read().split():
                    help = ''.join(open("help_rus.txt").readlines())
                    bot.send_message(message.from_user.id, help)
                elif str(message.from_user.id) in open('database/eng.txt').read().split():
                    help = ''.join(open("help.txt").readlines())
                    bot.send_message(message.from_user.id, help)
                else:
                    help = ''.join(open("help.txt").readlines())
                    bot.send_message(message.from_user.id, help)
            helpm2 = threading.Thread(target=helpm)
            helpm2.start()
        # ОТПРАВКА РАНДОМНЫХ ВИДЕО
        elif message.text == "uvid":
            def uvidm():
                if str(message.from_user.id) in open('database/rus.txt').read().split():
                    name = 'txt_server/' + str(random.randrange(2000)) + '.txt'
                    try:
                        # ГЕНЕРАЦИЯ ССЫЛКИ НА ВИДЕО С ПОМОЩЬЮ МОДУЛЯ
                        r_youtube.fun(name)
                        url = open(name).readlines()
                        url = ''.join(url)
                        t_message = 'Ссылка:\n\n' + url
                        bot.send_message(message.from_user.id, t_message)
                        os.remove(name)
                    except Exception as e:
                        os.remove(name)
                        t_message = 'Повторите команду'
                        bot.send_message(message.from_user.id, t_message)

                elif str(message.from_user.id) in open('database/eng.txt').read().split():
                    name = 'txt_server/' + str(random.randrange(2000)) + '.txt'
                    try:
                        r_youtube.fun(name)
                        url = open(name).readlines()
                        url = ''.join(url)
                        t_message = 'Url:\n\n' + url
                        bot.send_message(message.from_user.id, t_message)
                        os.remove(name)
                    except Exception as e:
                        os.remove(name)
                        t_message = 'Try again'
                        bot.send_message(message.from_user.id, t_message)
                else:
                    name = 'txt_server/' + str(random.randrange(2000)) + '.txt'
                    try:
                        r_youtube.fun(name)
                        url = open(name).readlines()
                        url = ''.join(url)
                        t_message = 'Url:\n\n' + url
                        bot.send_message(message.from_user.id, t_message)
                        os.remove(name)
                    except Exception as e:
                        os.remove(name)
                        t_message = 'Try again'
                        bot.send_message(message.from_user.id, t_message)
            uvidm2 = threading.Thread(target=uvidm)
            uvidm2.start()
        # РАНДОМНЫЙ СОВЕТ
        elif message.text == "advice":
            def advm():
                if str(message.from_user.id) in open('database/rus.txt').read().split():
                    bot.send_message(message.from_user.id, 'Совет этого дня:\n\n' + random.choice(adv.advices))
                elif str(message.from_user.id) in open('database/eng.txt').read().split():
                    advice = open("advices.txt").readlines()
                    bot.send_message(message.from_user.id, 'Here is advice:\n\n' + random.choice(advice))
                else:
                    advice = open("advices.txt").readlines()
                    bot.send_message(message.from_user.id, 'Here is advice:\n\n' + random.choice(advice))
            advm2 = threading.Thread(target=advm)
            advm2.start()
        # ОБРАТНАЯ СВЯЗЬ
        elif "-adv" in message.text:
            def advom():
                if str(message.from_user.id) in open('database/rus.txt').read().split():
                    print('New advice - ' + str(message.text.replace('-adv ', '')), file=open("data_adv/updates.txt", "a"))
                    bot.send_message(message.from_user.id, 'Ваш совет сохранен. Спасибо!')
                elif str(message.from_user.id) in open('database/eng.txt').read().split():
                    print('New advice - ' + str(message.text.replace('-adv ', '')), file=open("data_adv/updates.txt", "a"))
                    bot.send_message(message.from_user.id, 'Your advice saved. Thank you!')
                else:
                    print('New advice - ' + str(message.text.replace('-adv ', '')), file=open("data_adv/updates.txt", "a"))
                    bot.send_message(message.from_user.id, 'Your advice saved. Thank you!')
            advom2 = threading.Thread(target=advom)
            advom2.start()
        # ПОИСК В ГУГЛЕ
        elif "-gog" in message.text:
            def gogm():
                if str(message.from_user.id) in open('database/rus.txt').read().split():
                    t_message = 'Секунду'
                    bot.send_message(message.from_user.id, t_message)
                elif str(message.from_user.id) in open('database/eng.txt').read().split():
                    t_message = 'One sec'
                    bot.send_message(message.from_user.id, t_message)
                else:
                    t_message = 'One sec'
                    bot.send_message(message.from_user.id, t_message)

                results = random.randrange(10)
                txt = 'txt_server/' + str(random.randrange(2000)) + '.txt'
                cutcut = message.text
                cutcut = cutcut.replace('-gog ', '')
                # print(cutcut)
                # ОБРАБОТКА ЗАПРОСА В МОДУЛЕ И ЗАПИСЬ ОТВЕТОВ В ГУГЛЕ НА ФАЙЛ
                gsearch.gosearch(cutcut, txt, results)

                f = open(txt, "r")

                if str(message.from_user.id) in open('database/rus.txt').read().split():
                    t_message = 'Вот что выдал гугл\n\n' + str(f.read())
                    bot.send_message(message.from_user.id, t_message)
                elif str(message.from_user.id) in open('database/eng.txt').read().split():
                    t_message = 'Here is results\n\n' + str(f.read())
                    bot.send_message(message.from_user.id, t_message)
                else:
                    t_message = 'Here is results\n\n' + str(f.read())
                    bot.send_message(message.from_user.id, t_message)
                os.remove(txt)
            gogm2 = threading.Thread(target=gogm)
            gogm2.start()
        # ПОИСК В ЮТУБЕ
        elif "-utube" in message.text:
            def utubem():
                if str(message.from_user.id) in open('database/rus.txt').read().split():
                    t_message = 'Секунду'
                    bot.send_message(message.from_user.id, t_message)
                elif str(message.from_user.id) in open('database/eng.txt').read().split():
                    t_message = 'One sec'
                    bot.send_message(message.from_user.id, t_message)
                else:
                    t_message = 'One sec'
                    bot.send_message(message.from_user.id, t_message)

                results = random.randrange(10)
                txt = 'txt_server/' + str(random.randrange(2000)) + '.txt'
                cutcut = message.text
                cutcut = cutcut.replace('-utube ', '')
                # print(cutcut)
                gsearch.yousearch(cutcut, txt, results)

                f = open(txt, "r")

                if str(message.from_user.id) in open('database/rus.txt').read().split():
                    t_message = 'Вот что выдал гугл\n\n' + str(f.read())
                    bot.send_message(message.from_user.id, t_message)
                elif str(message.from_user.id) in open('database/eng.txt').read().split():
                    t_message = 'Here is results\n\n' + str(f.read())
                    bot.send_message(message.from_user.id, t_message)
                else:
                    t_message = 'Here is results\n\n' + str(f.read())
                    bot.send_message(message.from_user.id, t_message)
                os.remove(txt)
            utubem2 = threading.Thread(target=utubem)
            utubem2.start()
        # ВЫБОРКА АРТОВ
        elif "art_com" in message.text:
            def art():
                if str(message.from_user.id) in open('database/rus.txt').read().split():
                    text = 'Выбери арт'
                    bot.send_message(message.from_user.id, text, reply_markup=keyboard.keyboardART)
                elif str(message.from_user.id) in open('database/eng.txt').read().split():
                    text = 'Choose art'
                    bot.send_message(message.from_user.id, text, reply_markup=keyboard.keyboardART)
                else:
                    text = 'Choose art'
                    bot.send_message(message.from_user.id, text, reply_markup=keyboard.keyboardART)
            art2 = threading.Thread(target=art)
            art2.start()
        # КЛАВИАТУРА НАЗАД/ВКЛЮЧИТЬ/ВЫКЛЮЧИТЬ
        elif "keyboard" in message.text or 'back' in message.text:
            def kboardm():
                if str(message.from_user.id) in open('database/rus.txt').read().split():
                    text = 'Выбери команду'
                    bot.send_message(message.from_user.id, text, reply_markup=keyboard.keyboard)
                elif str(message.from_user.id) in open('database/eng.txt').read().split():
                    text = 'Choose command'
                    bot.send_message(message.from_user.id, text, reply_markup=keyboard.keyboard)
                else:
                    text = 'Choose command'
                    bot.send_message(message.from_user.id, text, reply_markup=keyboard.keyboard)
            kboardm2 = threading.Thread(target=kboardm)
            kboardm2.start()
        elif "keyboard_off" in message.text:
            def kboardmoff():
                if str(message.from_user.id) in open('database/rus.txt').read().split():
                    text = 'Клавиатура убрана'
                    bot.send_message(message.from_user.id, text, replyKeyboardHide=keyboard.keyboard)
                    bot.send_message(message.from_user.id, text, replyKeyboardHide=keyboard.keyboardART)
                elif str(message.from_user.id) in open('database/eng.txt').read().split():
                    text = 'Keyboard removed'
                    bot.send_message(message.from_user.id, text, replyKeyboardHide=keyboard.keyboard)
                    bot.send_message(message.from_user.id, text, replyKeyboardHide=keyboard.keyboardART)
                else:
                    text = 'Keyboard removed'
                    bot.send_message(message.from_user.id, text, replyKeyboardHide=keyboard.keyboard)
                    bot.send_message(message.from_user.id, text, replyKeyboardHide=keyboard.keyboardART)
            kboardmoff2 = threading.Thread(target=kboardmoff)
            kboardmoff2.start()
        # переключение языка англ/рус
        elif "rus" in message.text:

            def rusm():
                import fileinput
                for line in fileinput.input('database/eng.txt', inplace =1):
                    line = line.strip()
                    if not str(message.from_user.id) in line:
                        print(line)

                print(message.from_user.id, file=open("database/rus.txt", "a"))
                bot.send_message(message.from_user.id, 'Вы выбрали русский язык')
            rusm2 = threading.Thread(target=rusm)
            rusm2.start()
        elif "eng" in message.text:

            def engm():
                import fileinput
                for line in fileinput.input('database/rus.txt', inplace =1):
                    line = line.strip()
                    if not str(message.from_user.id) in line:
                        print(line)

                print(message.from_user.id, file=open("database/eng.txt", "a"))
                bot.send_message(message.from_user.id, 'You have chosen English')
            engm2 = threading.Thread(target=engm)
            engm2.start()
        # АРТЫ
        elif message.text == "art":
            def artm():
                # ВЫБОР АРТОВ ИДЕТ ИЗ БАЗЫ В ВК (ИЗ СВОЕЙ ГРУППЫ), ССЫЛКИ В ФАЙЛЕ
                art = open("Tserver/art.txt").readlines()
                bot.send_photo(message.from_user.id, random.choice(art))
            artm2 = threading.Thread(target=artm)
            artm2.start()
        elif message.text == "/azurlane":
            def azurm():
                art = open("Tserver/azurlane.txt").readlines()
                bot.send_photo(message.from_user.id, random.choice(art))
            azurm2 = threading.Thread(target=azurm)
            azurm2.start()
        elif message.text == "blade":
            def bladem():
                art = open("Tserver/blade.txt").readlines()
                bot.send_photo(message.from_user.id, random.choice(art))
            bladem2 = threading.Thread(target=bladem)
            bladem2.start()
        elif message.text == "darling":
            def darm():
                art = open("Tserver/darling.txt").readlines()
                bot.send_photo(message.from_user.id, random.choice(art))
            darm2 = threading.Thread(target=darm)
            darm2.start()
        elif message.text == "genshin":
            def genm():
                art = open("Tserver/genshin.txt").readlines()
                bot.send_photo(message.from_user.id, random.choice(art))
            genm2 = threading.Thread(target=genm)
            genm2.start()
        elif message.text == "neko":
            def nekom():
                art = open("Tserver/neko.txt").readlines()
                bot.send_photo(message.from_user.id, random.choice(art))
            nekom2 = threading.Thread(target=nekom)
            nekom2.start()
        elif message.text == "rezero":
            def rezm():
                art = open("Tserver/rezero.txt").readlines()
                bot.send_photo(message.from_user.id, random.choice(art))
            rezm2 = threading.Thread(target=rezm)
            rezm2.start()
        elif message.text == "succubs":
            def sucm():
                art = open("Tserver/succubs.txt").readlines()
                bot.send_photo(message.from_user.id, random.choice(art))
            sucm2 = threading.Thread(target=sucm)
            sucm2.start()
        elif message.text == "tate":
            def tatem():
                art = open("Tserver/tate.txt").readlines()
                bot.send_photo(message.from_user.id, random.choice(art))
            tatem2 = threading.Thread(target=tatem)
            tatem2.start()
        elif message.text == "tensura":
            def tenm():
                art = open("Tserver/TenSura.txt").readlines()
                bot.send_photo(message.from_user.id, random.choice(art))
            tenm2 = threading.Thread(target=tenm)
            tenm2.start()
        elif message.text == "vtubers":
            def vtm():
                art = open("Tserver/vtubers.txt").readlines()
                bot.send_photo(message.from_user.id, random.choice(art))
            vtm2 = threading.Thread(target=vtm)
            vtm2.start()
        elif message.text == "anime":
            def animem():
                word = RandomWords().random_word()
                animeSearch.loop.run_until_complete(animeSearch.anime_search(word))
                txt_name = animeSearch.text_name
                f = open(str(txt_name), "r")
                bot.send_message(message.from_user.id, str(f.read()))
                os.remove(str(txt_name))
            animem2 = threading.Thread(target=animem)
            animem2.start()
        # РАНДОМНЯ МАНГА
        elif message.text == "manga":
            def mangam():
                word = RandomWords().random_word()
                animeSearch.loop.run_until_complete(animeSearch.manga_search(word))
                txt_name = animeSearch.text_name
                f = open(str(txt_name), "r")
                bot.send_message(message.from_user.id, str(f.read()))
                os.remove(str(txt_name))
            mangam2 = threading.Thread(target=mangam)
            mangam2.start()
        # ПОИСК АНИМЕ И МАНГИ
        elif '-anime' in message.text:
            def animesm():
                # ОБРАБОТКА СООБЩЕНИЯ ПОЛЬЗОВАТЕЛЯ
                inp = message.text
                word = re.compile("-anime (.*)")
                cut = word.findall(inp)
                cutcut = ''.join(cut)
                # ПОИСК АНИМЕ В БАЗЕ ДАННЫХ С ПОМОЩЬЮ ГОТОВОГО МОДУЛЯ
                animeSearch.loop.run_until_complete(animeSearch.anime_search(cutcut))
                txt_name = animeSearch.text_name
                f = open(str(txt_name), "r")
                bot.send_message(message.from_user.id, str(f.read()))
                os.remove(str(txt_name))
            animesm2 = threading.Thread(target=animesm)
            animesm2.start()
        elif '-manga' in message.text:
            def mangasm():
                # ОБРАБОТКА СООБЩЕНИЯ ПОЛЬЗОВАТЕЛЯ
                inp = message.text
                word = re.compile("-manga (.*)")
                cut = word.findall(inp)
                cutcut = ''.join(cut)
                # ПОИСК МАНГИ В БАЗЕ ДАННЫХ С ПОМОЩЬЮ ГОТОВОГО МОДУЛЯ
                animeSearch.loop.run_until_complete(animeSearch.manga_search(cutcut))
                txt_name = animeSearch.text_name
                f = open(str(txt_name), "r")
                bot.send_message(message.from_user.id, str(f.read()))
                os.remove(str(txt_name))
            mangasm2 = threading.Thread(target=mangasm)
            mangasm2.start()
        else:
            # ПРИ ЛЮБОМ НЕПОНЯТНОМ СООБЩЕНИИ ОТ ПОЛЬЗОВАТЕЛЯ
            def elsem():
                bot.send_message(message.from_user.id, "I don't understand. Type /help for help")
            elsem2 = threading.Thread(target=elsem)
            elsem2.start()
    bot.polling(none_stop=True, interval=0)

if __name__ == '__main__':

    # МУЛЬТИПРОЦЕССИНГ

    p = Process(target=t_art)
    p.start()
