### Import packages 
``` import numpy as np```


### Understanding P-values 
1. Let's start by thinking about a game where you need to identify the suits of 12 cards drawn randomly with replacement from a 52 card deck.

	- Create a list of four string elements - hearts, diamonds, clubs and spades 
	- Create a new list using np.repeat to repeat each element 13 times (this list should contain 52 elements)
	- Use np.random.shuffle to shuffle the deck 

2. Let's assume you are completely guessing - i.e. your chance to get it right is 25%  - this assumption is called the null hypothesis and is denoted (H0)
 	  - The probability that someone is completely guessing (H0) and got x cards or more correctly will tell us the p-value. If it's really small - not a real chance to obtain this result we will reject the null hypothesis of guessing (prehaps we have sensory abilities)  
	- Create a varibale called ```chance``` and assign 0.25 (my guessing chance) to it.  

3. Create a ```correct_guess``` variable (initialize it with 0)

4. Create a ```counter``` variable (initialize it with 0) to see how many experiments are needed to guess 12 cards or more correctly 

5. Create a while loop with a nested for loop

	-    Stop the while loop only when you have 5 rounds with 12 correct guesses or more - keep the loop running for 20 steps always (Don't use break!)
	-    Run the for loop for a range of 20 (our test for identification)
	-    Each run draw randomly from your deck a card
	-    Also randomly choose from the list of 4 elements (spades, diamond etc..)
	-    If the draw from the deck equals your draw, increment ```correct_guess``` by one
	-    Every time the for loop ends, increment counter by one 
6. Divide 5 by the counter value --> this is the empirical P value