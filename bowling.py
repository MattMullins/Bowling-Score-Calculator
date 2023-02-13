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
[6,/,X,4,5,X,X,3,/,X,3,4,9,-,X,3,/] -> 164
[X,X,X,X,X,X,X,X,X,X,X,X] -> 300
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
    rolls = ["6","/","X","4","5","X","X","3","/","X","3","4","9","-","X","3","/"]
    
    printScore(rolls)

main()
    









