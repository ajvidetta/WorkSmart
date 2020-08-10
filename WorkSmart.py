#!/usr/bin/env python

from tkinter import *
from tkinter import filedialog
import os
import PDFSearcher

root = Tk()
root.minsize(500, 250)


def run():
    if (tkvar.get() != "choose subject") and (keywordEntry.get() != ""):
        outpt["text"] = ""
        key = keywordEntry.get()
        #print(key)
        #print("dropdown is {}".format(tkvar.get()))
        
        directory = tkvar.get()
        
        subjectPath = os.listdir(tkvar.get())

        text = ""
        
        for i in range(len(subjectPath)):
            if ".pdf" in subjectPath[i]:
                result = PDFSearcher.search("{}/{}".format(directory, subjectPath[i]), key)
                #print(result)
                if result != "":
                    text += "{}:\n {}\n\n".format(subjectPath[i], result)
        if text == "":
            outpt["text"] = "No results found!"
        else:
            #print(text)
            outpt["text"] = text

def openfile():
    name =  filedialog.askdirectory()
    tkvar.set(name)
    subjectPath = os.listdir(name)
    subjectPath.sort()
    #print(subjectPath)
    txt = "Lectures found: \n"
    for i in range(len(subjectPath)):
        txt += "{}\n".format(subjectPath[i])
    #displayText.set(txt)
    files["text"] = txt

tkvar = StringVar(root)
tkvar.set("choose subject")

fileopen = Button(root, text = "Choose ", command=openfile)
fileopen.grid(row=1, column=0, pady=20)


#keyword 
keylabel = Label(root, text = "Keyword:")
keylabel.grid(row=2, column=0)

keywordEntry = Entry(root)
keywordEntry.grid(row=3, column=0)

#run button
runcall = Button(root, text="search", command=run)
runcall.grid(row=4, column=0)

#files found in selected path
files = Label(root, text="please select subject...", font=("Courier", 10))
files.grid(row=0, column=1, columnspan=2, rowspan=10)

#search outpt
outpt = Label(root, text = "Search Results: ", font=("Courier", 10))
outpt.grid(row=0, column=3, columnspan=2, rowspan=10)
