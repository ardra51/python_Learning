'''
import my_module as mymod

num=int(input("enter the number : "))

print(mymod.is_even(num))

'''

from gtts import gTTS
import os

speech = gTTS(text="hello everyone.good morning",lang="en")
speech.save("sample.mp3")
os.system('start sample.mp3')


'''
from tkinter import *

window=Tk()
window.mainloop()

'''