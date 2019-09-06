import model as m
import view as v


class Controller:

    def __init__(self):
        self.x = m.Model()
        self.y = v.View()

    def save_cover(self):
        '''
        save the book
        '''
        name = self.y.enter.get()
        self.img = self.x.image(self.x.cover_search(name))
        self.y.show_cover(self.img)
    
if __name__ == "__main__":
    srch = Controller()
    srch.y.canvas(srch.save_cover)