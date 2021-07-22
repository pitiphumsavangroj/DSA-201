url = 'https://raw.githubusercontent.com/hjorturlarsen/IMDB-top-100/master/data/movies.json'
top = pd.read_json(url)
del top['id']
top[['rank', 'title']].rename(columns = {
    'rank': 'Rank',
    'title': 'Movie Title'
}).dropna()