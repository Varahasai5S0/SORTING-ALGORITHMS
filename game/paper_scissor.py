import random
def number_to_name(number): 
    d={0:'rock',1:'Spock',2:'paper',3:'lizard',4:'scissors'} 
    a=d[number]
    return a
def name_to_number(name): 
    d={'rock':0,'Spock':1,'paper':2,'lizard':3,'scissors':4} 
    a=d[name] 
    return a
def rpsls(player_choice): 
    print('Player chooses',player_choice)
    a=name_to_number(player_choice)
    b=random.randrange(0,4) 
    computer_choice=number_to_name(b) 
    print('Computer chooses',computer_choice)
    c=a-b
    if c==1 or c==2:
        return "Player" 
    elif c==0:
        return "No One"
    else:
        return "Computer"
while True: 
    player_choice=input('Select any: rock  Spock  paper  lizard  scissors  quit(to exit game)->->:')  
    if player_choice=='quit':
        break
    else:
        c=rpsls(player_choice) 
        print(c,'wins!\n')
