import tkinter as tk


class View:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Cover Search')

    def canvas(self, fct):
        '''
        creates a window for searching cover
        '''
        self.C = tk.Canvas(self.window, width = 300, height = 300)
        self.C.pack()
        self.enter = tk.Entry(self.window)
        self.enter.pack()
        tk.Button(self.window, text = 'Submit', command = fct).pack()
        self.window.mainloop()
        
    def show_cover(self, img):
        '''
        save the book
        '''
        self.C.create_image(150, 150, image = img
