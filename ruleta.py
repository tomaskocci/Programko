import random
money =int (input("Your money:"))
while money>0:
    bet =int (input("Put  bet: "))
    color = (input("Enter color:red,black: "))
    
    randomc=random.randint(0,36) 
    colorr=" "
    if randomc==0:
        colorr="green"
    elif randomc>=18:
        colorr="red"
    else:
        colorr="black"

    if color==colorr:
        money+= bet*2
        print("It is:",colorr)
        print("You wow:")
        print("Your left money is:",money)
    else:
        print("It is:",colorr)
        print("You lose:")
        money-=bet
        print("Your left money is:",money)
    if money==0:
        print("Better luck next time ):")






