#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter

root = tkinter.Tk()

l1 = tkinter.Label(root, text="simple app", 
    padx=10, pady=10, bg="red")
l1.pack()

l2 = tkinter.Label(root, text="simple app", 
    padx=10, pady=10, bg="blue")
l2.pack()

l2 = tkinter.Label(root, text="simple app", 
    padx=10, pady=10, bg="brown")
l2.pack()

root.mainloop()