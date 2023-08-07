import random


def intro():
    print(f"\nWelcome to Country Trivia!\nA Trivia Game designed and built by Rajiv Wallace.")


def exit_trivia():
    print("\nTo exit the game, press Ctrl^C.\nTo go back to Main Menu, type '0' and press 'Enter'.\n")


def go_back(code):
    if code == "0":
        return code


def shuffle_pack(country_data):
    data = random.sample(country_data, len(country_data))
    return data


def through_pack(pair):
    pass


def category():
    prompt = input(
        f"Main Menu\n\nTo guess capitals, type '1'.\nTo guess countries, type '2'.\n")

    if prompt == "1":
        print(f"\nLet's start guessing capitals!\n")
        return "1"
    elif prompt == "2":
        print(f"\nLet's start guessing countries!\n")
        return "2"
    else:
        print("\nYou must type 1 or 2 to continue!")


def capital_prompt(shuffled_country_data):
    capital_answer = input(
        f"What is the Capital City of {shuffled_country_data[0][0]}?\n")
    return capital_answer


def country_prompt(shuffled_country_data):
    country_answer = input(
        f"{shuffled_country_data[0][1]} is the capital city of which country?\n")
    return country_answer


def check_answer_for_capital(prompt_answer, country_data):
    if prompt_answer == country_data[0][1]:
        print("Correct!")
    else:
        print(
            f"Incorrect! The capital city of {country_data[0][0]} is {country_data[0][1]}.")


def check_answer_for_country(prompt_answer, country_data):
    if prompt_answer == country_data[0][0]:
        print("Correct!")
    else:
        print(
            f"Incorrect! {country_data[0][1]} is the capital city of {country_data[0][0]}.")
