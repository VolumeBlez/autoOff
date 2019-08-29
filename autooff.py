''' программа должна автоматически выключать комп
	должно быть поле для ввода времени через сколько выключиться
	и снизу кнопка начала отсчета, запускающая механизм '''



from tkinter import * # импортируем модуль для оконных приложений
import os # импортируем модуль os


def stop (): # функция остановки обратного отсчета до выключения
	os.system('shutdown -a')

def off (): # функция выключения через поле ввода, в секундах
	e = e1.get()
	if int(e) >= 60 : # условие что введеное число должно быть больше 60 сек
		str(e) # перевод обратно в строку
		os.system('shutdown -s -t ' + e)
	else :
		win = Tk() # окно ошибки в случае маленького числа
		win.resizable(0, 0)
		win.title("Error")
		win.config(bg = "Gray")
		x = (win.winfo_screenwidth() - win.winfo_reqwidth()) / 2
		y = (win.winfo_screenheight() - win.winfo_reqheight()) / 2
		win.wm_geometry("+%d+%d" % (x, y))
		l2 = Label(win, text = "error, number < 60", font = "Arial 20", )
		l2.grid()


def off5 () : # функция выключения через 5 минут
	os.system('shutdown -s -t 300')

def off45 () : # функция выключения через 45 минут
	os.system('shutdown -s -t 2700')

def off60 () : # функция выключения через 60 минут
	os.system('shutdown -s -t 3600')


root = Tk() # создание окна
root.config(bg = "#A9A9A9")
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))
root.title("autoOFF")
root.resizable(0, 0)

# поле ввода
e1 = Entry(font = "Arial 16", width = 18) # поле ввода
e1.grid(row = 0, column = 1)

# перечень кнопок
b1 = Button(text = "In 5 minutes" , command = off5 , width = 17, height = 2, font = "Arial, 18", bg = "#F5F5F5")
b1.grid(row = 2 , column = 0)

b3 = Button(text = "In 45 minutes" , command = off45, width = 17, height = 2, font = "Arial, 18", bg = "#F5F5F5")
b3.grid(row = 3, column = 0)

b4 = Button(text = "In 60 minutes", command = off60, width = 17, height = 2, font = "Arial, 18", bg = "#F5F5F5")
b4.grid(row = 4, column = 0)

b5 = Button(text = "ok", command = off, width = 10, height = 2, font = "Arial, 18", bg = "#808080")
b5.grid(row = 1, column = 1)

b6 = Button(text = "stop", command = stop, width = 10, height = 2, font = "Arial, 18", bg = "#808080")
b6.grid(row = 3, column = 2)


l1 = Label(text = "Your time in second -->", height = 1, width = 19, font = "Arial 17")
l1.grid(row = 0, column = 0)




root.mainloop()