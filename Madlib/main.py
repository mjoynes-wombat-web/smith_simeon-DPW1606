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


#3 Main template strings that makeup the story, one the story, one about getting a drink, one about not being able to afford a drink.
main_story = ''' you get up to go and a {british_insult_1} runs right into you.
"You {british_insult_2}," you shout, "Watch where you're going".
He turns around, fists clenched, but you deck him before he can even swing.
The bar keep laughs, passing you a {favorite_drink}.
"That {british_insult_1} has been giving us plenty of trouble. He needed to be taken down a peg."
At least the day's ending well.
'''

get_drink = '''
You walk into Yorkshire Pub after a long day.
You find a quite seat at the bar hoping to blow off some steam.
"What'll you have?" the bar keep asks.
"Give me a {favorite_drink}."
After quitely finising your drink,'''

no_drink = '''
You get to your favorite watering hole, the Yorkshire Pub.
After finding a quite seat you reach into your pocket for some cash to find it empty.
"What can I get for you?" asks the bar keep.
"Ah bugger, I'm out of cash."
"Ain't that just the way of it." he replies.
Disappointed,'''

#An array of British insults to insert into the template strings.

#A dictionary containing drinks and their prices

#A prompt asking for the users drinks budget.

#A prompt asking for a their favorite liquor.

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

print get_drink + main_story
print no_drink + main_story