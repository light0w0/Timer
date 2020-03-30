# -+- coding: utf-8 -*-
 
import tkinter as Tk
import time
import winsound
from multiprocessing import Process

class Timer(Tk.Frame):

    def __init__(self, master=None):
        Tk.Frame.__init__(self,master)
 
        self.master.title('TIMER')
        self.tokei=Tk.Label(self,text=u'00:00',font='Arial, 200')
 
        b1 = Tk.Button(self,text='Start',command=self.start)
        b2 = Tk.Button(self,text='Stop',command=self.stop)
        b3 = Tk.Button(self,text='Reset',command=self.reset)

        b1.grid(row=1, column=0,columnspan=2, padx=5, pady=2,sticky=Tk.W+Tk.E)
        b2.grid(row=1, column=2,columnspan=2, padx=5, pady=2,sticky=Tk.W+Tk.E)
        b3.grid(row=1, column=4,columnspan=2, padx=5, pady=2,sticky=Tk.W+Tk.E)

        self.tokei.grid(row=2, column=0,columnspan=4, padx=5, pady=2,sticky=Tk.W+Tk.E)

        self.start_time = 0
 
    # Start
    def start(self):
        self.started = True
        self.start_time = time.time()
        self.count()   
 
    # Reset
    def reset(self):
        self.start_time = 0
        self.tokei.config(text=u'00:00')

    # Stop
    def stop(self):
        self.started  = False
  
    def count(self):
        if self.started:
            
            t = time.time() - self.start_time

            if round(t) == (60*5 - 2) :
                p= Process(target=sound1)
                p.start()
            
            elif round(t) == (60*7) :
                p= Process(target=sound2)
                p.start()
 
            # 表示時間を1秒毎に書き換え
            self.tokei.config(text='%02d:%02d'%(t/60,t%60))
            self.after(500, self.count)
            


def sound1():
    winsound.PlaySound("bell1.wav", winsound.SND_FILENAME)

def sound2():
    winsound.PlaySound("bell2.wav", winsound.SND_FILENAME)

 
if __name__ == '__main__':
    f = Timer()
    f.pack()
    f.mainloop()