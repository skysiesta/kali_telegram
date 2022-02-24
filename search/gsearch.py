# ПОИСК В ГУГЛЕ
def gosearch(word, txt_out, results):
    from googlesearch import search

    search = search(word, num_results=results, lang="ru")
    search = '\n'.join(search)

    # print(search, file=open(txt_out, 'a'))
    resu = search.split()[-1][:7]
    if resu == '/search':
        search = search.replace(resu, 'https://www.google.com' + resu)
        print(search, file=open(txt_out, 'a'))
    else:
        print(search, file=open(txt_out, 'a'))

# ПОИСК В ЮТУБЕ
def yousearch(word, txt_out, results):
    from youtubesearchpython import VideosSearch

    search = VideosSearch('NoCopyrightSounds', limit = results)

    count = 0
    for soup in range(results):
        url = search.result()['result'][count]['id']
        url = 'https://www.youtube.com/watch?v=' + url
        print(url, file=open(txt_out, 'a'))
        count += 1
    # print(results['videos'])
    # print([i['id'] for i in results['result']])
    # print('https://www.youtube.com/watch?v=' + str(results['videos']['id']))
