#import mysql.connector

#cnn = mysql.connector.connect(host ="localhost", user ="root", passwd ="Root2021", database ="ejemplopython")

#print(cnn)
#!/usr/bin/env python3

import tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None):

        tk.Frame.__init__(self, master)

        self.grid()

        self.createWidgets()

    

    def createWidgets(self):

        self.mondialLabel = tk.Label(self, text='Hola, Mundo!')

        self.mondialLabel.config(bg="#00ffff")

        self.mondialLabel.grid()

        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton = tk.Button(self, text='guardar', command=self.quit)

        self.quitButton.grid()


if __name__ == '__main__':

    app = Application()

    app.master.title('La aplicacion muestra dos cambio de otro usuario')

    app.mainloop()