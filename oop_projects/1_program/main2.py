from requests import get

def get_authors(search_name:str=None):
    authors = []
    query_author = get('https://wolnelektury.pl/api/authors/')
    for author_id, author in enumerate(query_author.json(), start=1):
        if search_name in author['name']:
            authors.append({
                'author_id' : author_id,
                'name' : author.get("name", "Not found"),
                'api_books_url' : author.get("href") + 'books/'
            })
            # print(f'{author_id}. {author.get("name", "Not found")}')

    return authors

authors = get_authors('Adam')
for author in authors:
    print(f'{author.get("author_id")}. {author.get("name", "Not found")}')

search_author_id = int(input('Which author of the book do you want to see?: '))
found_author = next(filter(lambda author: author.get('author_id') == search_author_id, authors))
#print(list(found_author)) # filter object to list -> <class 'list'>
#print(type(next(found_author))) # filter object to (in this case) dict -> <class 'dict'>

for book in get(found_author.get('api_books_url')).json():
    print(book['title'])


