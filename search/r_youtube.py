# СЛУЧАЙНОЕ ВИДЕО ИЗ ЮТУБА
def fun(name):
    import json
    import urllib.request
    import string
    import random

    count = 1
    API_KEY = 'АПИ КЛЮЧ ОТ ГУГЛ СЕРВИСА'
    random = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))

    urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}".format(API_KEY,count,random)
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    results = json.loads(data.decode(encoding))

    for data in results['items']:
        videoId = (data['id']['videoId'])
    video = 'https://www.youtube.com/watch?v=' + videoId
    print(video, file=open(name, 'a'))
    # print(video)
        # print(videoId)
        # print('https://www.youtube.com/watch?v=' + videoId)
        #store your ids

    # api_key = 'AIzaSyAOXBiHMMSZQA23j46fJ0E34v2YSgDY5pE'
