#!/usr/bin/env python3 

import sqlite3
import sys
conn = sqlite3.connect('wizard_duels.db')
c = conn.cursor()

if sys.argv[1] == 'wizards':
    c.execute("INSERT INTO wizards VALUES (?,?,?,?)", (sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]))
elif sys.argv[1] == 'houses':
    c.execute("INSERT INTO houses VALUES (?,?,?)", (sys.argv[2],sys.argv[3],sys.argv[4]))
else:
    print('that table in not in the schema')

conn.commit()
