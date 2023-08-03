import random


def intro():
    print(f"\nWelcome to Country Trivia!\nA Trivia Game designed and built by Rajiv Wallace.")


def shuffle_pack(country_data):
    data = random.sample(country_data, len(country_data))
    return data


def category():
    prompt = input(
        f"\nTo guess capitals, type '1'.\nTo guess countries, type '2'.\n")

    if prompt == "1":
        print(f"\nLet's start guessing capitals!")
        return "1"
    elif prompt == "2":
        print(f"\nLet's start guessing countries!")
        return "2"
    else:
        print("\nYou must type 1 or 2 to continue!")
        return


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
        print("Incorrect!")


def check_answer_for_country(prompt_answer, country_data):
    if prompt_answer == country_data[0][0]:
        print("Correct!")
    else:
        print("Incorrect!")
