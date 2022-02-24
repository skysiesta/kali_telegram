import asyncio

import kitsu, random
# МОДУЛИ ДЛЯ АНИМЕ - МАНГА ПОИСКА

client = kitsu.Client()
random_num = random.randrange(20000)
text_name = "search/" + str(random_num) + ".txt"


async def anime_search(query):
    # ОПРЕДЕЛЕНИЕ КОЛИЧЕСТВА ОТВЕТОВ И ЗАПРОСА
    entries = await client.search('anime', query, limit=1)
    if not entries:
        print(f'No entries found for "{query}"', file=open(text_name, "a"))
        return

    for i, anime in enumerate(entries, 1):
        print(f'\n{i}. {anime.title}:', file=open(text_name, "a"))
        print('---> Sub-Type:', anime.subtype, file=open(text_name, "a"))
        print('---> Status:', anime.status, file=open(text_name, "a"))
        print('---> Synopsis:\n' + anime.synopsis, file=open(text_name, "a"))
        print('---> Episodes:', anime.episode_count, file=open(text_name, "a"))
        print('---> Age Rating:', anime.age_rating_guide, file=open(text_name, "a"))
        print('---> Ranking:', file=open(text_name, "a"))
        print('-> Popularity:', anime.popularity_rank, file=open(text_name, "a"))
        print('-> Rating:', anime.rating_rank, file=open(text_name, "a"))

        if anime.started_at:
            print('---> Started At:', anime.started_at.strftime('%Y-%m-%d'), file=open(text_name, "a"))
        if anime.ended_at:
            print('---> Ended At:', anime.ended_at.strftime('%Y-%m-%d'), file=open(text_name, "a"))

        # ССЫЛКИ НА ЭПИЗОДЫ
        streaming_links = await client.fetch_anime_streaming_links(anime)
        if streaming_links:
            print('---> Streaming Links:', file=open(text_name, "a"))
            for link in streaming_links:
                print(f'-> {link.title}: {link.url}', file=open(text_name, "a"))

        print('---> Kitsu Page:', anime.url, file=open(text_name, "a"))


async def manga_search(query):
    entries = await client.search('manga', query, limit=1)
    if not entries:
        print(f'No entries found for "{query}"', file=open(text_name, "a"))
        return

    for i, manga in enumerate(entries, 1):
        print(f'\n{i}. {manga.title}:', file=open(text_name, "a"))
        print('---> Sub-Type:', manga.subtype, file=open(text_name, "a"))
        print('---> Status:', manga.status, file=open(text_name, "a"))
        print('---> Volumes:', manga.volume_count, file=open(text_name, "a"))
        print('---> Chapters:', manga.chapter_count, file=open(text_name, "a"))
        print('---> Synopsis:\n' + manga.synopsis, file=open(text_name, "a"))
        print('---> Age Rating:', manga.age_rating_guide, file=open(text_name, "a"))
        print('---> Ranking:', file=open(text_name, "a"))
        print('-> Popularity:', manga.popularity_rank, file=open(text_name, "a"))
        print('-> Rating:', manga.rating_rank, file=open(text_name, "a"))

        if manga.started_at:
            print('---> Started At:', manga.started_at.strftime('%Y-%m-%d'), file=open(text_name, "a"))
        if manga.ended_at:
            print('---> Ended At:', manga.ended_at.strftime('%Y-%m-%d'), file=open(text_name, "a"))

        print('---> Kitsu Page:', manga.url, file=open(text_name, "a"))

loop = asyncio.get_event_loop()
# loop.run_until_complete(anime_search(input('Insert an anime name: ')))
# loop.run_until_complete(manga_search(input('Insert a manga name: ')))
