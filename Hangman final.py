from tkinter import *
import random

root=Tk()
root.title('HANGMAN GAME')
root.geometry('600x400')
root.configure(background='cyan')

sc1=StringVar("")
t1=Label(root,text='Guess the word!',font=('Comic Sans MS',28,'italic','underline','bold'),fg='red',bg='cyan')
t1.place(x=150,y=0)

t2=Label(root,text='Categories',font=('Comic Sans MS',24,'italic','underline','bold'),fg='red',bg='cyan')
t2.place(x=200,y=80)

def geog():
    print("Hangman")
    print("Category: Geography | Type:Continents")
    continents=("North America","South America","Europe","Antarctica","Asia","Africa","Oceanna")
    secret_word=random.choice(continents)
    losing_number=0
    guess_count=5
    word="Word:"+"*" * len(secret_word)
    print(word)


    while guess_count>losing_number:
        guess = input("Guess the word: ").title()
        guess_count -=1
        print(f"Guesses left:{guess_count}")
        if guess == secret_word:
            print("You won the game!")
            break
        elif guess != secret_word:
            print("Wrong Guess!")
        
        else:
            print("Sorry, you lost the Game!")
            print("The word was" +secret_word)

def gk():
    print("Hangman")
    print("Category: General Knowledge | Type:Prime Ministers of India till now!") 
    PrimeMinister=("JawaharlalNehru","LalBahadurShastri","AtalBihariVajpayee","IndiraGandhi","RajivGandhi","ManmohanSingh","NarendraModi")
    secret_word1=random.choice(PrimeMinister)
    losing_number=0
    guess_count=5
    word="Word:"+"*" * len(secret_word1)
    print(word)


    while guess_count>losing_number:
        guess = input("Guess the word: ").title()
        guess_count -=1
        print(f"Guesses left:{guess_count}")
        if guess == secret_word1:
            print("You won the game!")
            break
        elif guess != secret_word1:
            print("Wrong Guess!")
        
        else:
            print("Sorry, you lost the Game!")
            print("The word was" +secret_word1)

    








addbtn = Button(root,text="General Knowledge",command=gk)
addbtn.place(x=100,y=170)
addbtn1 = Button(root,text="Famous People")
addbtn1.place(x=100,y=230)
addbtn2 = Button(root,text="Art")
addbtn2.place(x=100,y=300)

addbtn3 = Button(root,text="Geography",command=geog)
addbtn3.place(x=280,y=170)
addbtn4 = Button(root,text="Music")
addbtn4.place(x=280,y=230)
addbtn5 = Button(root,text="Food")
addbtn5.place(x=280,y=300)

addbtn6 = Button(root,text="Movies")
addbtn6.place(x=450,y=170)
addbtn7 = Button(root,text="TV Shows")
addbtn7.place(x=450,y=230)
addbtn8 = Button(root,text="Sports")
addbtn8.place(x=450,y=300)
root.mainloop()




