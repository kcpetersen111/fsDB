import sys
import sqlite3


def runTournament():
    pass

def runDuels(house):
    pass

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
else:
    print("I dont know what you mean")
