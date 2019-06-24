# SQL Joins

### Import packages 
sqlite3
pandas
   
### Connect to databases cats.db, dogs.db and owners.db using sqlite3 (use for example conn = sqlite3.connect('cats.db') and then c = conn.cursor())

Let's try and work through some exercises to recap and retain the foundational knowledge of the language that our beloved databases use.

In the suburbs of Capitol Hill, there is a new pet daycare starting up that distributes pets among 4 houses.
Down below we have tables representing cats and dogs in the particular houses, and corresponding owners. 

Cats Table:

Name  			 | Breed 			| House_Number| Owner_ID|       
------------- | ------------- | ------------|---------
Bell  			| Siamese			|		1	    | 4
Jackson  		| Balinese 		|       2     |3
Precious  	| Himalayan  		|         3    | 4
Rocky			| Egyptian Mau 	| 4 		    | 2
Samson			| Javanese		|	4		| 1

Dogs Table:

Name  			 | Breed 	| House_Number	|Owner_ID|
-------------| ------------- | ------------|-----   
Rex  			| Chihuahua  		|		1	    |3
Clifford  	| German Shepherd|     2        |2
Lucky  		| Daschund  		|     3        |1
Bobo			| Shih-Tzu		|    2		   | 4
Buddy			| Golden Retriever | 4		   | 2
Leo				| English Bulldog | 1 | 2

Owners Table:

Name  		| Phone	| Address	|ID| 
-------------| ------------- | ------------|-----
Josh Daniell  | 313-287-9573  |1440 G St. |1
Alison Peebles Madigan| 214-709-8190| None |2
Avi Flombaum	| 469-878-0125  |  1776 New York Ave| 3
Justin Bieber | 410-381-0987 | None | 4


Write the appropriate SQL queries to satisfy the following prompts:

A. Write a SQL query that can grab the names of all pets owned by the founder of Flatiron School, Avi Flombaum

B. Which House_Number contains the most number of pets in it and how many?

C. The daycare realized that House 4 needs the owners of its pets to update their addresses. Grab the names and phone numbers of owners with pets in house 4 that do not currently have an address.

