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
You walk into Yorkshire Pub after a long day.
You find a quite seat at the bar hoping to blow off some steam.
"What'll you have?" the bar keep asks.
"Give me a {favorite_drink}."
After quitely finising your drink,'''

#If you can't get a drink, the part of the story that's returned.
no_drink = '''
You get to your favorite watering hole, the Yorkshire Pub.
After finding a quite seat you reach into your pocket for some cash to find it empty.
"What can I get for you?" asks the bar keep.
"Ah bugger, I'm out of cash."
"Ain't that just the way of it." he replies.
Disappointed,'''

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


    if liquor>len(liquors) or liquor<1:
        print "You didn't select a valid liquor. Please try again.'"
        fav_liquor()
    else:
        return liquors[liquor-1]

favorite_liquor = fav_liquor()

drink_budget = raw_input("What do you think is reasonable for a " + drinks[favorite_liquor]["drink"] + "?")

favorite_letter = raw_input("What is your favorite letter?")



#Ask the user for their favorite letter.

#A function that accepts the user prompts and returns the story.
    #Drink Variable
    #Insult Variable
    #Number of the letter var = num of letter %10

    #Based on their favorite liquor find out if they can afford a drink.
        #If yes then define the drink var as that drink.
    #Else
        #If no then define the drink var as false.
    
    #Using a loop find the insult using the number from the variable above.
        #Define the insult var as the insult.

    #if drink var is true
        #return the story inserting the british insult and the drink line inserting the drink
    #else
        #return the story inserting the birtish insult and the line about not being able to affor a drink

#story = function with the user prompts as params

#print story

#print get_drink + main_story
#print no_drink + main_story