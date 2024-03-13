letters = [
    ['h', 'o','l','i','d','a','y'],
    ['p', 'r','o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g'],
    ['b', 'o','o','t', 'c', 'a', 'm', 'p'],
    ['f', '1', 'o','w', 'c', 'h', 'a', 'r', 't'], 
    ['w', 'o', 'r', 'd', 's', 'c', 'a', 'p', 'e', 's']
    ]


words = [
    ["hi", "hay", "day", "had", "lay", "dal", "lad", "lid", "hold", "lady", "hail"],
    ["go", "an", "in", "no", "on", "map", "mom", "gap", "gag", "pig", "man", "ping",
     "pong", "pram", "prom", "ramp"],
    ["am", "at", "to",
     "cab", "cap", "cob", "cop", "map", "mop", "act", "bat", "camp",
     "comb", "boom", "pact", "atom"],
    ["of", "at", "or", "to", "caw", "cow", "how", "who", "calf", "claw", "flaw", "flow",
     "fowl", "Wolf", "crow", "half"],
     ["we","do","as","cap","caw", "cop", "cow", "paw", "cod", "dew", "pad", "cape",
    "cope", "crap", "crew","crop","pace"]
]


lives=5
level=0
answer=[]
chance=3
flag=True
count=0
name=input("Enter Your Name: ")
name=name.title()

# At each level the user will be given some letters and the user has to guess 3 words to move to the next level.
while(flag and level<5):
    print("Make 3 Words from the Below Letters. ")
    print(letters[level])
    while(flag):  
        if flag is False:
            break
        word=input("Enter  word: ")  
        word=word.lower()   
        if word in words[level]: 
            count+=1         
            print("You have Guessed ", count, " word correctly")
            answer.append(word)
            print(answer)
            if len(answer)==3:
                print(name," You won")
                if level==4:
                    print("Congratulations! " ,name," you won the game")
                    print("Your final score is: ",count)
                    flag=False
                    break


                next_level=input("do you want to try next level (yes/no): ")
                next_level=next_level.lower()
                if next_level=="yes":
                    flag=True
                    print("Your final score is: ",count)
                    level+=1
                    answer.clear()
                    break
                else:
                    flag=False
                    print("Your final score is: ",count)
                    break               
                
    

        else:
            print("OOPS! You Have Guessed Wrong Word")
            lives-=1
            print("Now you have only ",lives," chance left")
            if lives==0:
                print("You loose")
                print("Your final score is: ",count)
                flag=False
                break




