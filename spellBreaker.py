import sys
import sqlite3


def runTournament(c):
    pass

def runDuels(house, c):
    pass

def runTrain(house, c):
    
    # get the people from  all of the people from a house
    # get a user have them fight someone in there house 
    # keep going until one wins 
    c.execute("""
        WITH train(wizard) AS (
            SELECT * FROM wizards WHERE wizards.house == ? LIMIT 1
        ) 

    """)
    

def getYears(year, c):
    c.execute("SELECT * FROM wizards WHERE year = (?)", [year])
    w_names = c.fetchall()
    i = 0
    for i in range(len(w_names)):
        print(w_names[i][1])

def getHouse(house, c):
    c.execute("SELECT * FROM wizards WHERE house = (?)", [house])
    w_names = c.fetchall()
    i = 0
    for i in range(len(w_names)):
        print(w_names[i][1])

def getWeakness(house):
    c.execute("SELECT * FROM houses WHERE house = (?)", [house])
    h_name = c.fetchall()
    print(h_name[0][1])

def getStalemate(house):
    c.execute("SELECT * FROM houses WHERE house = (?)", [house])
    h_name = c.fetchall()
    print(h_name[0][2])

def getSpells(wizard, c):
    for spell in c.execute('''
        SELECT 
            spells.spell
        FROM 
            wizards JOIN mastery ON 
                wizards.id = wizard_id
            JOIN spells ON
                spells.id = spell_id
        WHERE
            name = ?
    ''', [wizard]).fetchall():
        print(spell[0])


def getMasters(spell ,c):
    pass

conn = sqlite3.connect('wizard_duels.db')
c = conn.cursor()
if sys.argv[1] == "tournament":
    runTournament(c)
elif sys.argv[1] == "duels":
    print(runDuels(sys.argv[2]), c)
elif sys.argv[1] == "year":
    getYears(sys.argv[2], c)
elif sys.argv[1] == "house":
    getHouse(sys.argv[2], c)
elif sys.argv[1] == "weakness":
    getWeakness(sys.argv[2])
elif sys.argv[1] == "stalemate":
    getStalemate(sys.argv[2])
elif sys.argv[1] == "spells":
    getSpells(sys.argv[2], c)
elif sys.argv[1] == "train":
    print(runTrain(sys.argv[2], c))
elif sys.argv[1] == "masters":
    print(getMasters(sys.argv[2], c))
else:
    print("I dont know what you mean")
conn.commit()
