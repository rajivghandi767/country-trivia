# Country Trivia Game by Rajiv Wallace

from country_data import country_capital_data as ccd
from player_data import *
from game_functions import *


intro()

# game_pack = shuffle_pack(ccd)
# capital_answer = capital_prompt(game_pack)
# print(capital_answer)
# print(game_pack[0][1])
# check_answer_for_capital(capital_answer, game_pack)

# test = choice()
# print(test)
# print(type(test))

while True:

    choice = category()

    while True:

        new_game_pack = shuffle_pack(ccd)
        used_game_cards = []

        if choice == "1":
            capital_answer = capital_prompt(new_game_pack)
            used_game_cards.append(capital_answer)
            check_answer_for_capital(capital_answer, new_game_pack)

        elif choice == "2":
            country_answer = country_prompt(new_game_pack)
            check_answer_for_country(country_answer, new_game_pack)
        else:
            break
