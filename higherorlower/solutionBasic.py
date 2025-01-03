import art
import game_data
import random


More_followers=""
def get_data(data,strText):
    MY_TEXT = ""
    for key in data:
        MY_TEXT += data[key] +","
    print(strText + ": " +MY_TEXT)

def play_game():
    global More_followers
    countA=0
    countB=0
    for i in range(2):
        my_dictionary = {}
        if i==0:
            print(art.logo)
            my_dictionary=random.choice(game_data.data)
            countA=my_dictionary.pop("follower_count")
            get_data(my_dictionary,'Compare A')
        else:
            print(art.vs)
            my_dictionary = random.choice(game_data.data)
            countB=my_dictionary.pop("follower_count")
            get_data(my_dictionary, 'Against B')

    if int(countA) > int(countB):
        More_followers="A"
    else:
        More_followers = "B"
    print(More_followers)

run_game=True
while run_game:
    play_game()
    followers_count=input("Who has more followers, Type 'A' or 'B': ")
    if str(followers_count) == str(More_followers):
        run_game = True
    else:
        print("you loose the game")
        run_game=False