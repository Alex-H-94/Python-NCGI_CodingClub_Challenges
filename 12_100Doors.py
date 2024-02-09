# Initialise the list of doors and 'jump' counter.
listDoors = [False] * 100
doorsToJump = 0

# Make 1 pass for every door: 100 doors = 100 passes.
for count in range(0, len(listDoors)):
    # Increase the number of doors we avoid with every pass.
    doorsToJump += 1
    # Set the doorsToJump as the starting point. Because lists and arrays start at entry '0' we need to 'take one step back' with -1.
    doorToToggle = doorsToJump - 1
        
    # 'Visit' and toggle each door, adding to the doorToToggle until we have no more doors.
    while doorToToggle < len(listDoors):                
        if (listDoors[doorToToggle]):
            listDoors[doorToToggle] = False
        else:
            listDoors[doorToToggle] = True
        
        doorToToggle += doorsToJump
        
# Finally, print the end result in a readable format:
for count in range(0, len(listDoors)):
    if listDoors[count]:
        print(f"Door {count + 1} is [OPEN]")
    else:
        print(f"Door {count + 1} is [CLOSED]")