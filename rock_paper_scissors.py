import random

def play():
    user = input("What's Your Choice? 'r' for rock, 'p' for paper, 's' for scissors ")
    computer = random.choice(['r','p','s'])

    #r>s,s>p,p>r
    if user == computer:
        return "It's a Tie!"

    if valid_win(user, computer):
        return 'You Won!'
    return 'You Lost!'

def valid_win(player, opp):
    if(player=='r' and opp=='s') or (player=='s' and opp=='p') or (player=='p' and opp=='r'):
        return True

print(play())
