#bowling

'''
Have a list of rolls
'X' indicates a strike
'/' indicates a spare
'0' indicates a miss
'1-9' indicate # of pins knocked down
'''

'''
*****TEST CASES*****
["6","/","X","4","5","X","X","3","/","X","3","4","9","-","X","3","/"] -> 164
["X","X","X","X","X","X","X","X","X","X","X","X"] -> 300
[2,3,2,3,2,3,2,3,2,3,2,3,2,4,2,3,4,2,4,/,9] -> 66 

***PARAMETERS***
Min # of rolls: 12
Max # of rolls: 21

Strike at n: 10 + (n+1) + (n+2)
Spare at n: 10 + (n+1)

*Keep track of frames for final bonus


***Psuedocode***

If n is a number,
    - check (n+1),
        - if a spare,
            - list.score(n)
            - list.spare(n,n+1)
            - increment roll
            - increment frame
        - else if another int,
            - list.score(n+(n+1))
            - increment frame
            - increment roll
        - else if miss,
            - list.score(n)
            - increment frame
            - increment roll

if n is strike
    - increment frame
    - check (n+1) and (n+2)
    
when frame == 9:
    - calculate final frame bonus
'''

def calc(rolls):
    count = 0
    score = 0
    frames = 10
    toggle = 0
    
    numRolls = len(rolls)
    
    for x in range(len(rolls)):
        roll = rolls[x]
        if frames > 1:
            if roll == "X":
                score = score + tally(count, roll, rolls) + tally(count, rolls[x+1], rolls) + tally(count, rolls[x+2], rolls)
                frames -= 1
            elif roll == "/":
                score = score + tally(count, roll, rolls) + tally(count, rolls[x+1], rolls)
                frames -= 1
            else:
                score = score + tally(count, roll, rolls)
                toggle += 1
                if toggle % 2 == 0:
                    frames -= 1
        elif frames == 1:
            if numRolls == 3:
                if roll == "X":
                    score = score + tally(count, roll, rolls) + tally(count, rolls[x+1], rolls) + tally(count, rolls[x+2], rolls)
                    frames -= 1
                else:
                    score = score + tally(count, roll, rolls)
            elif numRolls == 2:
                if roll == "X" or roll == "/":
                    score = score + tally(count, roll, rolls) + tally(count, rolls[x+1], rolls)
                    frames -= 1
                else:
                    score = score + tally(count, roll, rolls)
                    toggle += 1
                    if toggle % 2 == 0:
                        frames -= 1
            elif numRolls == 1:
                score = score + tally(count, roll, rolls)
                if toggle % 2 == 0:
                        frames -= 1
                
                
        numRolls -= 1
        count += 1
    
    print("Score:", score)
    
def tally(count, roll, rolls):
    if roll == "X":
        return 10
    elif roll == "/":
        return int((10-rolls[count-1]))
    elif roll == "-":
        return 0
    else:
        return int(roll)

def printScore(rolls):
    numRolls = len(rolls)
    
    for x in range(numRolls):
        currRoll = rolls[x]
        if currRoll == "X":
            print("STRIKE!!!")
        elif currRoll == "/":
            print("Spare!")
        elif currRoll == "-":
            print("...miss :(")
        else:
            print(currRoll)

def main():
    rolls = ["X","X","X","X","X","X","X","X","X","X","X","X"]
    
    calc(rolls)

main()
    









