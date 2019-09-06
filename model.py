import urllib.request
from PIL import Image, ImageTk
import json


class Model:

    def __init__(self):
        pass

    def cover_search(self, search):
        '''
        takes a book title and returns cover id
        '''
        search = search.replace(' ', '+')
        url = 'http://openlibrary.org/search.json?q=' + str(search)
        response = urllib.request.urlopen(url)
        string = json.load(response)
        response.close()
        docs = string['docs']
        for dict in docs:
            if 'cover_i' in dict:
                self.cover_id = dict['cover_i']
                break
        return self.cover_id

    def image(self, cover_id):
        '''
        takes a url and returns image
        '''
        url = 'http://covers.openlibrary.org/b/id/' + str(cover_id) + '-M.jpg'
        response = urllib.request.urlopen(url)
        self.img = Image.open(response)
        self.img = ImageTk.PhotoImage(self.img)
        response.close()
        return self.img

