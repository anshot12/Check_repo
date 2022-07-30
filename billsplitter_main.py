import random
how_many_people = int(input("Enter the number of friends joining (including you):\n"))
try:
    how_many_people > 0
    message = "No one is joining for the party"
    assert how_many_people > 0, message
except AssertionError as error:
    print(error)
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    friends = {input(" "): 0 for key in range(how_many_people)}
    friends_name = list(friends)
    total_bill = int(input("\nEnter the total bill value:\n"))
    lucky_game = str(input("\nDo you want to use the 'Who is lucky?' feature? Write Yes/No:\n"))
    if lucky_game == "Yes":
        lucky_one = random.choice(friends_name)
        print(lucky_one, " is the lucky one!\n")
        bill_for_one = round(total_bill / (how_many_people - 1), 2)
        friends_bill = friends.fromkeys(friends_name, bill_for_one)
        friends_bill[lucky_one] = 0
        print(friends_bill)
    elif lucky_game == "No":
        print("\nNo one is going to be lucky\n")
        bill_for_one = round(total_bill / how_many_people, 2)
        friends_bill = friends.fromkeys(friends_name, bill_for_one)
        print(friends_bill)


