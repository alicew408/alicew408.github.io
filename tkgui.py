class TkGuiAppbject):# class _main
    def __init__(self,errorl=0,l=1,debugmode=False) -> None:# class _main
        import tkinter as tk# import random,sys,tkinter as tk
        from tkinter import simpledialog# from tkinter import simpledialog
        from tkinter import messagebox# from tkinter import messagebox
        self.messagebox=messagebox
        self.simpledialog=simpledialog
    def init(self):
        self.root=tk.Tk()
        self.root.withdraw()
    def inputbox(self,text):
        return self.simpledialog.askstring('quiz', text)# askstring quiz text
    def mbox(self,text):# mbox
        self.messagebox.showinfo('message', text)
