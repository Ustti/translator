from tkinter import *
from translate import Translator 

Screen = Tk()
Screen.geometry('800x250')
Screen.title('language translator with gui by- ur stary')


InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()


LanguageChoices = {'Hindi', 'English', 'French', 'German', 'Spanish'}
InputLanguageChoice.set('English')
TranslateLanguageChoice.set('German')

def Translate():
    translator = Translator(from_lang= InputLanguageChoice.get(), to_lang = TranslateLanguageChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)    
  


InputLanguageChoiceMenu = OptionMenu(Screen,InputLanguageChoice,*LanguageChoices)
InputLanguageChoiceMenu.configure(font=('Arial','15'),fg='black')
Label(Screen,text="Choose a Language", font=('Arial','15'),fg='black').grid(row=0,column=1)
InputLanguageChoiceMenu.grid(row=1,column=1)


NewLanguageChoiceMenu = OptionMenu(Screen,TranslateLanguageChoice,*LanguageChoices)
NewLanguageChoiceMenu.configure(font=('Arial','15'),fg='black')
Label(Screen,text="Translated Language", font=('Arial','15'),fg='black').grid(row=0,column=3)
NewLanguageChoiceMenu.grid(row=1,column=3)


Label(Screen, text='Enter Text', font=('Arial','12'),fg='black').grid(row=2, column=0)
TextVar = StringVar()
TextBox = Entry(Screen, textvariable = TextVar, font=('Arial','20'),fg='black').grid(row = 2, column = 1)

Label(Screen, text='Output Text', font=('Arial','12'),fg='black').grid(row=2, column=2)
OutputVar = StringVar()
TextBox = Entry(Screen, textvariable=OutputVar, font=('Arial','20'),fg='black').grid(row=2, column = 3)

B = Button(Screen, text='Translate', command=Translate, relief = GROOVE,  font=('Arial','37'),fg='black').grid(row=10, column=1, columnspan = 5)

mainloop()



