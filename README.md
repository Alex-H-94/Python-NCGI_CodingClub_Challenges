# NCGI Coding Hub Challenges: Python

These are passing single-script entries for the NCGI Coding Hub challenges for Python.

#### Challenge 2: X's and O's
> Create a function that takes a string, checks if it has the same number of "x"s and "o"s and returns either True or False.
**Example:**
```
XO("ooxx") ➞ True 
XO("xooxx") ➞ False 
XO("ooxXm") ➞ True # Case insensitive. 
XO("zpzpzpp") ➞ True # Returns True if no x and o. 
XO("zzoo") ➞ False
```

### Challenge 3: Sequence of Numbers
> A sequence of numbers is alternating if each term has the opposite sign (positive or negative) to the terms immediately before and after it. Write a function is_alternating() that determines if a sequence is alternating, ie return True if it is and False if not.
**Example:**
```
sequence = [1,-1,2,-2,3,-3,4] should return True
sequence = (0.5,-0.33,0.25,-0.2,-0.12) should return False
```

### Challenge 4: The Fizz Buzz Classic
> A sequence of numbers is alternating if each term has the opposite sign (positive or negative) to the terms immediately before and after it. Write a function is_alternating() that determines if a sequence is alternating, ie return True if it is and False if not.
**Example:**
```
sequence = [1,-1,2,-2,3,-3,4] should return True
sequence = (0.5,-0.33,0.25,-0.2,-0.12) should return False
```

### Challenge 5: Film Snobs
> Film snobs love original movies and hate sequels. Given a list of movies, in the form Title (year), write a function that removes sequels. Assume all sequels use digits, not roman numerals.
```
movies=[‘Cars (2006)’,
‘Cars 2 (2011)’,
‘Cars 3 (2017)’,
‘Shrek (2001)’,
‘Shrek 2 (2004)’,
‘12 Monkeys (1995)’]
```
> **Example:**
```
film_snobs(movies) would return:
[‘Cars (2006)’, ‘Shrek (2001)’, ‘12 Monkeys (1995)’]
```

### Challenge 6: Dungeons and Dragons
> A hero is on their way to the castle to complete their mission. However, they have been told via messenger pigeon that the castle is surrounded with powerful dragons!! Each dragon takes 2 arrows to each knee to be defeated, our hero has no idea how many arrows they should carry… Given the hero needs a specific number of arrows to fight the dragons and survive, how many should they take? Write a function that takes two arguments (the number of dragons and the number of arrows) and returns True if they survive or False if they die. 
**Example:**
```
d_and_d(2, 8) would return True
```

### Challenge 7: Chickens and Rabbits 
> We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? Write a function to solve the problem.
- Extension:
> Generalise the function to solve from any number of heads and legs. Return “No Solution” if there are no solutions.
**Example:**
```
chickens_rabbits(35,94) would return ‘23 chickens and 12 rabbits’
```

### Challenge 11: TxtSpk 
> Strip the vowels from a string so that the string appears in text speak.
**Example:**
```
original_str = “The quick brown fox jumps over the lazy dog.”
Output:
“Th qck brwn fx jmps vr th lzy dg”
```

### Challenge 12: 100 Doors 
> There are 100 doors in a row that are all initially closed. You make 100 passes by the doors. The first pass, you visit every door and toggle its state (if the door is closed (False), you open it; if it is open (True), you close it). The second time, you only visit every 2nd door (door 2, 4, 6, …), and toggle it. The third time, you visit every 3rd door (door 3, 6, 9, …). Continue this pattern until you only visit the 100th door. Which doors are open, and which are closed after the last pass?

### Challenge 13: Morse Munch 
> Create a function that takes a string as an argument and returns the Morse code equivalent. One space between each letter, three spaces between each word.
**Example:**
```
encode_morse("HELP ME !") ➞ ".... . .-.. .--.   --.   -.-.--"
```

### Challenge 15: Mixed Feelings About This 
> According to a researcher at Cambridge University, it doesn't matter in what order the letters in a word are, the only important thing is that the first and last letter be at the right place. The rest can be a total mess and you can still read it without problem. Tihs is bcuseae the huamn mnid deos not raed ervey lteter by istlef, but the wrod as a wlohe. Can you create a python function that takes in a sentence and outputs the sentence with the letters mixed up whilst keeping the first and last letter in place?
**Example:**
```
my_string = “Mixed Feelings About This"
Output:
“Mexid Felegnis Auobt This”
```

### Challenge 16: Feeling HOT HOT HOT 
> Can you create a function that converts a given temperature in Celsius to Fahrenheit?
**Example:**
```
temp_c = 40
Output:
104
```
