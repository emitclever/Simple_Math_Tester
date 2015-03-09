#-*-coding:utf8;-*-
# qpy:2
# qpy:console
# My very first program on python for my daughter first math problems.
# Need qpython3 application for android (python3 mac or windows)
# Lets play
from random import randint
import android
import sys
import random
import time

correct = 0
rng = 3
starnum = 5
speak = True
print("Hello Melissa")
droid=android.Android()

def ttsslow(millis):
    time.sleep(millis)
droid.ttsSpeak("bonjour melissa")
ttsslow(2)
droid.ttsSpeak("est-ce que tu est pret?")
ttsslow(2)
while True:
    for i in range (rng):  # (number of questions)
        n1 = randint(0,starnum)   # (numbers to choose randomly)
        n2 = randint(0,n1)
        opera = random.choice(r'+-') # random operation choosing could be '+-*/' depend on complexity
        resultat = eval(str(n1) + opera + str(n2))
        print(n1,opera,n2,end="") 
        if opera == "-": opera = "moins"
        if speak:
            ttsslow(1.5)
            droid.ttsSpeak(str(n1))
            ttsslow(0.5)
            droid.ttsSpeak(str(opera))
            ttsslow(0.5)
            droid.ttsSpeak(str(n2))
        inp=(input(" = "))
        if inp.isdigit(): # check if valid integer not empty
            ans = int(inp)
        else:
            ans = 0
        if ans == resultat:
            #print("TRUE. :) \n\n")
            droid.ttsSpeak("ces vrai")
            correct = correct + 1
        else:
            #print("FALSE :( , Answer is %d.\n\n" % resultat)
            droid.ttsSpeak("ces faux. le resultat est %s" % (resultat))
    print("\nResults %d / %d." % (rng,correct))
    ttsslow(1.5)
    droid.ttsSpeak("tu a reussi %s questions sur %s" % (str(correct), str(rng)))
    yes = set(['yes','y', 'ye', ''])
    no = set(['no','n'])
    droid.ttsSpeak("est-ce que on essay Encore en fois ?")
    choice = input("Start again? ").lower()
    if choice in no:
        break
    else:
        correct = 0
