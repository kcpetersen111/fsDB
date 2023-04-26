import sys
import sqlite3


def runTournament(c):
    #c.execute("SELECT id, name FROM wizards")
    pass

def runDuels(house, c):
    pass

def runTrain(house, c):
    
    c.execute("DELETE FROM results;")
    
    # add everyone to res table
    # get one person who has not died 
    # get another one 
    # get a spell for each person 
    # set one to dead
    
    # ag query to take max  and then have people how have a max of 0 losses fight
    c.execute("INSERT INTO results SELECT w.name,0,0 FROM wizards AS w WHERE w.house = ?;",[house])
    c.execute("""
        WITH duelest (name) AS (
            SELECT r.name 
            FROM results AS r
            WHERE MAX(r.losses) == 0
            LIMIT 2
        )
        # CREATE VIEW randomCast AS
        # cast a spell
        SELECT wizard_id, spell_id, MIN(RANDOM()) AS rnd FROM mastery GROUP BY wizard_id;
        
        # get all of the people with zero losses
        SELECT r.name 
            FROM results AS r
            LIMIT 2;
            
        
     SELECT *
            FROM results AS r
            JOIN (SELECT wizard_id, spell_id, MIN(RANDOM()) AS rnd FROM mastery GROUP BY wizard_id) as w ON w.wizard_id = r.id
            JOIN spells ON spells.id = w.spell_id
            WHERE r.losses == 0
            LIMIT 2;
            
    # base case
    
     SELECT wizards.name, wizards.id, 0, 0
            FROM wizards
            WHERE 1= 1 LIMIT 1;
        
    # recursive 
    with wizardBattle(name, id, win, loss, battleNumber) AS (
        SELECT wizard.wizard_id, 0, 0 
            FROM wizards 
            WHERE wizards.house == ? LIMIT 1
            
    )
        
    """)
    # get the people from  all of the people from a house
    # make table 
    # get a user have them fight someone in there house 
    # keep going until one wins 
    c.execute("""
        WITH train(wizard, wins, losses) AS (
            SELECT wizard.wizard_id, 0, 0 
            FROM wizards 
            WHERE wizards.house == ? LIMIT 1
            
            Union
            
            SELECT x 
            FROM (
                SELECT wizard.wizard_id, 0, 0 
                FROM wizards 
                WHERE wizards.house == ? 
                    AND wizards.wizard_id NOT IN (
                        SELECT train.wizard FROM train
                    )
                )
            WHERE 
            LIMIT 1
            )
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
else:
    print("I dont know what you mean")
conn.commit()
