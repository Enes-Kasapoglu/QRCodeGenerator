# _*_ coding:UTF-8 _*_
from tkinter import *
import time
import os
import pyqrcode

def main():

	def translate():
		linkentry = qrentry.get()
		link = pyqrcode.create(linkentry)

		linkname = (fentry.get()+".svg")
		link.svg(linkname,scale=8)

		banner["text"] = "https://kilavuzkod.blogspot.com"
		completetext["text"] = "Başarı ile oluşturuldu!"
		savetext["text"] = "Dosya Dizinine Kaydedildi!"

	window = Tk()
	window.title("QRCode Generator")
	window.geometry("450x250")
	window.resizable(False,False)
	window.config(bg="#21252E")

	wtext = Label(text="Çevirmek İstediğiniz Adresi Giriniz",bg="#21252E",fg="#fff")
	wtext.pack()
	wtext.place(x=10,y=20)

	qrentry = Entry()
	qrentry.pack()
	qrentry.place(x=12,y=50)

	ftext = Label(text="Kaydetmek İstediğiniz Dosya Adını Giriniz",bg="#21252E",fg="#fff")
	ftext.pack()
	ftext.place(x=10,y=90)

	fentry = Entry()
	fentry.pack()
	fentry.place(x=12,y=120)

	translatebutton = Button(text="Çevir",bg="#21252E",fg="#fff",activebackground="#1db954",command=translate)
	translatebutton.pack()
	translatebutton.place(x=10,y=160)

	banner = Label(text="",bg="#21252F",fg="#fff")
	banner.pack()
	banner.place(x=100,y=170)

	completetext = Label(text = "",bg="#21252E",fg="#fff")
	completetext.pack()
	completetext.place(x=10,y=210)

	savetext = Label(text = "",bg="#21252E",fg="#fff")
	savetext.pack()
	savetext.place(x=10,y=230)

	mainloop()


main()