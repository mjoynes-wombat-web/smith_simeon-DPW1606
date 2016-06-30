#------------------------------REQUIREMENTS---------------------------------------
#3 Strings
#3 Numbers
#One Array
#One Dictionary
#2 Math Operators
#Two Conditional Statements with one logical operator
#One function with return value and 2 paramenters
#One Loop

#COMMENT WELL
#ORIGINAL
#ALL ELEMENTS USED
#6 COMMITS
#NO ERRORS
#PRINT OUT STORY


#VARIABLES---------------------------------------------------------------------------------------------------------------------------------------
#The main consistent portion of the story.
main_story = ''' you get up to go and a {british_insult_1} runs right into you.
"You {british_insult_2}," you shout, "Watch where you're going".
He turns around, fists clenched, but you deck him before he can even swing.
The bar keep laughs, passing you a {favorite_drink}.
"That {british_insult_1} has been giving us plenty of trouble. He needed to be taken down a peg."
At least the day's ending well.
'''

#If you can get a drink, the part of the story that is used.
get_drink = '''
It's {time} and you walk into Yorkshire Pub after a long day.
You find a seat at the bar hoping to blow off some steam.
"What'll you have?" the bar keep asks.
"Give me a {favorite_drink}."
After quietly finising your drink,'''

#If you can't get a drink, the part of the story that's returned.
no_drink = '''
You get to your favorite watering hole, the Yorkshire Pub, at {time}.
After finding a quiet seat you reach into your pocket for some cash to find it empty.
"What can I get for you?" asks the bar keep.
"Ah bugger, I'm out of cash."
"Ain't that just the way of it." he replies.
Disappointed,'''

#Random Numbers for Time
from random import randint
rand_num_1 = randint(5,12)
rand_num_2 = (randint(0, 5)*10) + randint(0, 9)

time =  str(rand_num_1) + ":" + str(rand_num_2) + " p.m."

#British Insults Array
british_insults = ["wazzok", "lummox", "skiver", "minger", "nincompoop", "pillock", "clod hopper", "dunaker", "git", "wanker"]

#Drinks Dict
drinks = dict()
drinks = {
    "Tequila":{"drink":"margarita", "price": 12},
    "Rum":{"drink":"cuba libre", "price":10},
    "Vodka":{"drink":"martini", "price":14},
    "Gin":{"drink":"singapore sling", "price":15},
    "Scotch":{"drink":"scotch, neat", "price":25},
    "Bourbon":{"drink":"old fashioned", "price":18},
    "Whiskey":{"drink":"irish car bomb", "price": 16}
}


#ASK FOR FAVORITE LIQUOR FUNCTION
def fav_liquor():
    #Variables for function
    liquors = ["Tequila", "Rum", "Vodka", "Gin", "Scotch", "Bourbon", "Whiskey"]
    liquor_options = ""

    #Print questions to console
    print "What's your favorite liquor?"
    print "Please, select from the options  below."
    
    #Setup options for liquor based on liquors variable.
    for idx, item in enumerate(liquors):
        liquor_options = liquor_options + str(idx+1) + ") " + item + " "

    #Print liquor options and allow raw input, making the input a number.
    liquor = int(raw_input(liquor_options))

    #If the number is larger than the number of liquors or less than 1 throw errro and rerun.
    if liquor>len(liquors) or liquor<1:
        print "You didn't select a valid liquor. Please try again.'"
        fav_liquor()
    #Else return the liquor chosen.
    else:
        return liquors[liquor-1]

#Define the favorite liquore based on the fav_liquor function.
favorite_liquor = fav_liquor()

#Ask how much they would pay for the drink option from that liquor
drink_budget = int(raw_input("What do you think is reasonable for a " + drinks[favorite_liquor]["drink"] + "?"))

#Ask them what their favorite letter is.
favorite_letter = raw_input("What is your favorite letter?")



def setup_story (liquor, budget, letter, time):
    favorite_drink = ""
    letter_num = (ord(letter.lower()) - ord("a"))%10
    british_insult_1 = british_insults[letter_num]
    british_insult_2 = british_insults[(len(british_insults)-letter_num-1)]

    if (drinks[liquor]["price"]<=budget):
        favorite_drink = drinks[liquor]["drink"]
    else:
        favorite_drink = False

    if favorite_drink:
        return get_drink.format(**locals()) + main_story.format(**locals())
    else:
        favorite_drink = drinks[liquor]["drink"]
        return no_drink.format(**locals()) + main_story.format(**locals())

story = setup_story(favorite_liquor, drink_budget, favorite_letter, time)

print story