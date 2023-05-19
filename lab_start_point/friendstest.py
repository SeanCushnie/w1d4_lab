import pdb 

def get_name(person):
    name = person["name"]
    return name

def get_favourite_tv_show(person):
    favourite_tv_show = person["favourites"]["tv_show"]
    return favourite_tv_show

def likes_to_eat(person,food):
    for snack in person["favourites"]["snacks"]:
    if snack == food:
        return True
    else:
        return False
# return food in person["favourites":["snacks"]]
    # # # likes_food = bool
    # # likes_to_eat = person["favourites"]["snacks"]
    # # # pdb.set_trace()
    # # #for loop to check whether "food" = items in likes_to eat
    # # # if that's true, return "true" else return false
    # # food = "bread"
    # # for food in likes_to_eat:
    # #     if food in likes_to_eat:
    # #         return True
    # #     else:
    # #          return False
# or
# return food in person["favourites"]["food"]

#4
def add_friend(person, new_friend):
    person["friends"].append(new_friend)

def remove_friend(person, old_friend):
    person["friends'"].remove(old_friend)

def total_money(people):
    total_money = 0
    for person in people:
        total_money += person["monies"]
    return person

def lend_money(lender, lendee, amount):
    lender ["monies"] -= amount
    lendee ["monies"] += amount

def all_favourite_foods(people):
    favourite_foods = []
    for person in people:
        for snack in person["favourites"]["snacks"]:
            favourite_foods.append(snack)
    return favourite_foods

def find_no_friends(people):
    nofriends = []
    for person in people:
        if len(person["friends"]) == 0:
            nofriends.append(person)
    return nofriends

def unique_favourite_tv_shows(people):
    unique_tv_shows = []
    for person in people:
        if person["favourites"]["tv_show"] not in unique_tv_shows:
            unique_tv_shows.append(person)
            ["favourites"]["tv_show"]
    return unique_tv_shows




