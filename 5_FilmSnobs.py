def film_snob(movies):
    output = []
    
    for movie in movies:
        if not movie[-8].isnumeric():
            output.append(movie)
    
    return output

lstTest = ["Cars 2 (2011)", "Cars (2006)", "Cars 3 (2017)", "Shrek (2001)", "Shrek 2 (2004)", "12 Monkeys (1995)", "12 Monkeys 2 (1995)", "The Amazing Adventures of Snowball (2010)", "The Amazing Adventures of Snowball 2 (2010)"]
print(film_snob(lstTest))