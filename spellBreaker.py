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
    
    c.execute("DELETE FROM results;")
    
    c.execute("INSERT INTO results SELECT w.id,w.name,0,0 FROM wizards AS w WHERE w.house = ?;",[house])
    for i in range(c.execute("SELECT COUNT(1) FROM results").fetchone()[0]-1):
        c.executescript("""

            CREATE table wizardBattle as
                SELECT r.name, spells.power
                FROM results AS r
                JOIN (SELECT wizard_id, spell_id, MIN(RANDOM()) AS rnd FROM mastery GROUP BY wizard_id) as w ON w.wizard_id = r.id
                JOIN spells ON spells.id = w.spell_id
                WHERE r.losses == 0
                LIMIT 2;
        
            CREATE VIEW twoPeopleBat AS
                SELECT name, max(power)
                    FROM wizardBattle;
            

            UPDATE results AS r1
                set wins = CASE
                            WHEN r1.name in (SELECT name FROM twoPeopleBat)
                                THEN (SELECT r2.wins FROM results AS r2 WHERE r1.id = r2.id)+1
                                ELSE (SELECT r2.wins FROM results AS r2 WHERE r1.id = r2.id)
                            END,
                    losses = CASE
                            WHEN r1.name NOT in (SELECT name FROM twoPeopleBat) AND r1.name in (SELECT name FROM wizardBattle)
                                THEN (SELECT r2.losses FROM results AS r2 WHERE r1.id = r2.id)+1
                                ELSE (SELECT r2.losses FROM results AS r2 WHERE r1.id = r2.id)
                            END;
            DROP VIEW twoPeopleBat;  
            DROP TABLE wizardBattle;
            SELECT * FROM results;
        """)
    for x in c.execute("SELECt * from results ORDER BY wins DESC;").fetchall():
        print(x)
   
   
def freeForAll(c):
    c.execute("DELETE FROM results;")
    
    
    c.execute("INSERT INTO results SELECT w.id,w.name,0,0 FROM wizards AS w;")
    for i in range(c.execute("SELECT COUNT(1) FROM results").fetchone()[0]-1):
        c.executescript("""

            CREATE table wizardBattle as
                SELECT r.name, spells.power
                FROM results AS r
                JOIN (SELECT wizard_id, spell_id, MIN(RANDOM()) AS rnd FROM mastery GROUP BY wizard_id) as w ON w.wizard_id = r.id
                JOIN spells ON spells.id = w.spell_id
                WHERE r.losses == 0
                LIMIT 2;
        
            CREATE VIEW twoPeopleBat AS
                SELECT name, max(power)
                    FROM wizardBattle;
            

            UPDATE results AS r1
                set wins = CASE
                            WHEN r1.name in (SELECT name FROM twoPeopleBat)
                                THEN (SELECT r2.wins FROM results AS r2 WHERE r1.id = r2.id)+1
                                ELSE (SELECT r2.wins FROM results AS r2 WHERE r1.id = r2.id)
                            END,
                    losses = CASE
                            WHEN r1.name NOT in (SELECT name FROM twoPeopleBat) AND r1.name in (SELECT name FROM wizardBattle)
                                THEN (SELECT r2.losses FROM results AS r2 WHERE r1.id = r2.id)+1
                                ELSE (SELECT r2.losses FROM results AS r2 WHERE r1.id = r2.id)
                            END;
            DROP VIEW twoPeopleBat;  
            DROP TABLE wizardBattle;
            SELECT * FROM results;
        """)
    for x in c.execute("SELECt * from results ORDER BY wins DESC;").fetchall():
        print(x)
  
   
    
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
elif sys.argv[1] == "free":
    freeForAll(c)
elif sys.argv[1] == "review":
    buildReview(c)
elif sys.argv[1] == "compare":
    compareWizards(sys.argv[2], sys.argv[3], c)
else:
    print("I dont know what you mean")
conn.commit()
