from cProfile import label
from tkinter.ttk import Labelframe
import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("1000x700")
root.configure(bg="black")
Label(root,text="unMute", bg="brown", fg="blue").pack()

f1 = LabelFrame(root,bg="blue")
f1.pack()
L1 = Label(f1,bg="pink")
L1.pack()

cap = cv2.VideoCapture(0)

try:
    while True:
        img = cap.read()[1]
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(Image.fromarray(img))
        L1['image'] = img
        root.update()
except:
    cap.release()