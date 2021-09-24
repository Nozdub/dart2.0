import random

print("-------------------------------")
print("-----Let's play some darts-----")
print("-------------------------------")

# player_count antall spillere i INT
player_list = []
pointlist = []
results = []

# Input antall spillere.
player_count = int(input("Enter how many players who will participate: "))

# Input spiller navn.
for players in range(player_count):
    player = (input("Write player name: "))
    player_list.append(player)

print(f"\nAlright {player_list}, let's get ready to dart!")

# Konverterer playerlist til int slik at jeg har tall knyttet til spiller navn.
int(player_count)
player_count = 1
for player in player_list:
    player_count += 1


def give_random_number(range_start, range_stop):
    random_number = random.randrange(range_start, range_stop)
    return random_number

for player in range(player_count):

    # Dart 1
    random_number_variable_1 = give_random_number(1, 60)
    input(f"\nAlright {player_list[0]} throw your first dart by pressing any ENTER:")
    print(random_number_variable_1)
    dart_1 = random_number_variable_1

    # Dart 2
    random_number_variable_2 = give_random_number(1, 60)
    input(f"\nAlright {player_list[0]} throw your second dart by pressing any ENTER:")
    print(random_number_variable_2)
    dart_2 = random_number_variable_2

    # Dart 3
    random_number_variable_3 = give_random_number(1, 60)
    input(f"\nAlright {player_list[0]} throw your third dart by pressing any ENTER:")
    print(random_number_variable_3)
    dart_3 = random_number_variable_3

    p1_result = dart_1 + dart_2 + dart_3
    print(f"\nYour score {str(player_count)[0]} is {p1_result}")


   # player_score = (str(player_list[0]),  str(p1_result))
   # print(player_score)




#print(f"\nNice throwing! Your score is {p1_result}")