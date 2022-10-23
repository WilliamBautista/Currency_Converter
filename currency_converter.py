from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
from tkinter import *

def conversion(count1, count2,amount):

    c = CurrencyRates()
    t = CurrencyCodes()

    converted = c.convert(count1,count2,amount)
    lbl.config(text = f"{t.get_symbol(count1)}{round(amount,2)} {t.get_currency_name(count1)}\nis equal to\n{t.get_symbol(count2)}{round(converted,2)} {t.get_currency_name(count2)}")


def printInput():
    try:
        inp = float(amottxt.get(1.0, "end-1c"))
    except ValueError:
        lbl.config(text = f'ERROR: {amottxt.get(1.0, "end-1c")}  is not a numerical value')

    inp2 = country1.get(1.0, "end-1c").upper()
    inp3  = country2.get(1.0, "end-1c").upper()

    try:
        if inp2.isalpha() & inp3.isalpha():
            conversion(inp2[:3],inp3[:3],inp)
        else:
            lbl.config(text = f'ERROR: provided country values contain a number')
    except:
        lbl.config(text = f'ERROR: invalid currency code or not a numerical value')


windows = Tk()

windows.title("Currency Calculator")
windows.geometry("750x500")
windows.configure(bg="#FFC0CB")
frame = Frame(master=windows, padx=10)
frame.pack() 

intro = Label(windows,bg="#FFC0CB" ,text="Welcome To The Currency Converter!\n\nTo start off please enter the amount that you would like to be converted\n\nNext, enter country currency codes for the currency conversion\n")
intro.pack()

code_ex=Label(windows,bg="#FFC0CB" ,text="Example Currency Codes",font = 'helvetica 14 underline')
code_ex.pack()
code_list = Label(windows,bg="#FFC0CB" ,text="USD: United States Dollar\nEUR: Euro\nJPY: Japanesse Yen\nGBP: Pound Sterling\nCAD: Canadian Dollar")
code_list.pack()

lbl = Label(windows,bg="#FFC0CB", text = "\nAmount")
lbl.pack()

amottxt = Text(windows,highlightbackground="#FFC0CB",height = 1,width = 10)

amottxt.pack()

blurb = Label(windows,bg="#FFC0CB" ,text="Current Currency")
blurb.pack()

country1 = Text(windows,highlightbackground="#FFC0CB",height = 1,width = 10)
country1.pack()

blurb = Label(windows,bg="#FFC0CB" ,text="New Currency")
blurb.pack()

country2 = Text(windows,highlightbackground="#FFC0CB",height = 1,width = 10)
country2.pack()

space = Label(windows,bg="#FFC0CB", text = "")
space.pack()

greet_button = Button(windows, text="Convert",highlightbackground="#FFC0CB",height = 1,width = 10,command=printInput)
greet_button.pack()

lbl = Label(windows,bg="#FFC0CB", text = "")
lbl.pack()

windows.mainloop()