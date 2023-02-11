
from requests import get

query_author = get('https://wolnelektury.pl/api/authors/')
#print(query_author.json())
search_name = 'Adam'
author_dict = {}

for author_id, author in enumerate(query_author.json(), start=1):
    if search_name in author['name']:
        print(f'{author_id}. {author.get("name", "unknown")}')
        author_dict[author_id] = author.get("name", "unknown")

# print(author_dict)

search_author_id = int(input('Which author of the book do you want to see?: '))

author_name = ''
# search_author_id = 4

if author_dict.get(search_author_id):
    author_name = author_dict.get(search_author_id)
else:
    print('Author not found!')
    
print('Author name:', author_name)

query_book = get('https://wolnelektury.pl/api/books/')

print('Books:')
if author_name:
    for book in query_book.json():
        if author_name in book['author']:
            print(book['title'])

print('lol')




