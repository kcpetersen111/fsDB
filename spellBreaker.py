import sys
import sqlite3


def runTournament():
    pass

def runDuels(house):
    pass

def runTrain(house, c):
    
    # get the people from  all of the people from a house
    # get a user have them fight someone in there house 
    # keep going until one wins 
    c.execute("""
        WITH train(wizard) AS (
            
        ) 

    """)
    

def getYears(year):
    pass

def getHouse(house):
    pass

def getWeakness(house):
    pass

def getStalemate(house):
    pass

def getSpells(wizzard):
    pass

conn = sqlite3.connect('wizard_duels.db')
c = conn.cursor()
if sys.argv[1] == "tournament":
    print(runTournament())
elif sys.argv[1] == "duels":
    print(runDuels(sys.argv[2]))
elif sys.argv[1] == "year":
    print(getYears(sys.argv[2]))
elif sys.argv[1] == "weakness":
    print(getWeakness(sys.argv[2]))
elif sys.argv[1] == "stalemate":
    print(getStalemate(sys.argv[2]))
elif sys.argv[1] == "spells":
    print(getSpells(sys.argv[2]))
elif sys.argv[1] == "train":
    print(runTrain(sys.argv[2], c))
else:
    print("I dont know what you mean")
conn.commit()