# Country Trivia Game by Rajiv Wallace

from country_data import country_capital_data as ccd
from player_data import *
from game_functions import *


intro()
exit_trivia()

while True:

    choice = category()

    while True:

        new_game_pack = shuffle_pack(ccd)
        used_game_cards = []

        if choice == "1":
            capital_answer = capital_prompt(new_game_pack)
            if go_back(capital_answer):
                break
            else:
                check_answer_for_capital(capital_answer, new_game_pack)
                exit_trivia()

        elif choice == "2":
            country_answer = country_prompt(new_game_pack)
            if go_back(country_answer):
                break
            else:
                check_answer_for_country(country_answer, new_game_pack)
                exit_trivia()
        else:
            break
