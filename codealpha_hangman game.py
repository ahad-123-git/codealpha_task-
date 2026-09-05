import random
list1=["PYTHON","COMPUTER","CODING","SCHOOL","PROGRAM","APPLE"]
word=random.choice(list1)
count_guess=0
string=["-"]*len(word)
print("==============================")
print("         🎮HANGMAN GAME                   ")
print("==============================")
while(True):
    guess=(input("Enter a Letter :")).upper()
    if(guess in word):
        print("✓ Good guess!")
        for i in range(len(word)):
           if(word[i]==guess):
               string[i]=guess
        print("Word :",string)    
        if(str("".join(string))==word):
           print("==============================")
           print("                 GAME WIN !                          ")
           print("          The word was ",word)
           print("==============================")
           break
    else:
        print("✗ Wrong guess!")
        count_guess=count_guess+1
        if(count_guess==6):
            print("==============================")
            print("              ❌ GAME OVER!                    ")
            print("            The word was :",word)
            print("==============================")
            break





