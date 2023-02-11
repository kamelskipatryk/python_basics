from requests import get

class Author:
    def __init__(self, author_id:int, name:str, slug:str, api_books_url:str):
        self.author_id = author_id
        self.name = name
        self.slug = slug
        self.api_books_url = api_books_url
    
    def __str__(self) -> str:
        return f'{self.author_id}. {self.name}'

class WolneLekturyAdapter:
    API_URL = 'https://wolnelektury.pl/api/'

    def get_authors(self, search_name:str=None):
        authors = []
        query_author = get(self.API_URL + 'authors/')
        for author_id, author in enumerate(query_author.json(), start=1):
            if search_name in author['name']:
                authors.append(Author(
                    author_id = author_id,
                    name = author.get("name", "Not found"),
                    slug = author.get('slug'),
                    api_books_url = author.get("href") + 'books/'
                ))
                # print(f'{author_id}. {author.get("name", "Not found")}')

        return authors # return table of objects
    
    def get_books(self, author_slug):
        return get(f'{self.API_URL}authors/{author_slug}/books/').json()

class Aplication:
    def main(self):
        adapter = WolneLekturyAdapter()
        authors = adapter.get_authors('Adam')
        for author in authors:
            print(author)

        search_author_id = int(input('Which author of the book do you want to see?: '))
        found_author = next(filter(lambda author: author.author_id == search_author_id, authors))
        #print(list(found_author)) # filter object to list -> <class 'list'>
        #print(type(next(found_author))) # filter object to (in this case) dict -> <class 'dict'>

        for book in adapter.get_books(found_author.slug):
            print(book['title'])

if __name__ == '__main__':
    app = Aplication()
    app.main()


