import sys
import sqlite3


def runTournament():
    pass

def runDuels(house):
    pass

def getYears(year):
    conn = sqlite3.connect('wizard_duels.db')
    c = conn.cursor()
    c.execute("SELECT * FROM wizards WHERE year = (?)", [year])

def getHouse(house):
    pass

def getWeakness(house):
    pass

def getStalemate(house):
    pass

def getSpells(wizard):
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
