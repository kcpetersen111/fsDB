import sys
import sqlite3


def runTournament(c):
    c.execute("DELETE FROM results")
    c.execute("SELECT id, name FROM wizards ORDER BY RANDOM() LIMIT 16")
    w_list = c.fetchall()
    # i = 0
    # for i in range(len(w_list)):
    #     print(w_list[i])
    for i in range(len(w_list)):
        c.execute("INSERT INTO results VALUES (?,?,?,?)", (w_list[i][0], w_list[i][1], 0, 0))
    c.execute("SELECT * FROM results")
    w_results = c.fetchall()
    # i = 0
    # for i in range(len(w_results)):
    #     print(w_results[i])


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
    for master in c.execute('''
        SELECT 
            wizards.name
        FROM 
            wizards JOIN mastery ON 
                wizards.id = wizard_id
            JOIN spells ON
                spells.id = spell_id
        WHERE
            spells.spell = ?
    ''', [spell]).fetchall():
        print(master[0])

def buildChain(c):
    for wizard in c.execute('''
        SELECT 
            wizards.name, SUM(spells.power) AS power
        FROM 
            wizards JOIN mastery ON 
                wizards.id = wizard_id
            JOIN spells ON
                spells.id = spell_id
        GROUP BY wizards.name
        ORDER BY power DESC
    ''').fetchall():
        print(f'{wizard[0]:20} : {wizard[1]:5}')

def compareWizards(wiz1, wiz2, c):
    c.execute('''
        SELECT wizards.name, SUM(spells.power)/5 AS power
        FROM wizards
        JOIN mastery
        ON wizards.id = wizard_id
        JOIN spells 
        ON spells.id = spell_id
        WHERE wizards.name == (?) OR wizards.name == (?)
        GROUP BY wizards.name
        ORDER BY power DESC
    ''', (wiz1, wiz2))
    w_comp = c.fetchall()
    print(f"{w_comp[0][0]}'s average power: {w_comp[0][1]}")
    print(f"{w_comp[1][0]}'s average power: {w_comp[1][1]}")
    print(f"{w_comp[0][0]} wins")

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
    getMasters(sys.argv[2], c)
elif sys.argv[1] == "foodchain":
    buildChain(c)
elif sys.argv[1] == "compare":
    compareWizards(sys.argv[2], sys.argv[3], c)
else:
    print("I dont know what you mean")
conn.commit()
