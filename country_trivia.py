
user = input('Name: ')
user_country = input('Country: ')

greet_prompt = input("Hello " + user + ". Are you ready to play? ")
greet_prompt.capitalize()

if greet_prompt == 'Yes' or greet_prompt == 'Y':
     print("Ok, let's begin!")
elif greet_prompt == 'No' or greet_prompt == 'N':
    print("Ok, Maybe next time!")
else:
   print("Please answer 'Yes (Y)' or 'No (N)'")


def guess_country():
    input('What is the capital of ?')
    
def guess_city():
    input(' is the capital of what country?')