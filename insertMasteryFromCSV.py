#!/usr/bin/env python3 

import sys
import sqlite3
import pandas as pd

data = pd.read_csv(sys.argv[1])
df = pd.DataFrame(data)

conn = sqlite3.connect('wizard_duels.db')
c = conn.cursor()

for row in df.itertuples():
    c.execute('''
                INSERT INTO mastery (wizard_id, spell_id)
                VALUES(?,?)
              ''',
              [row.wid,
              row.sid]
              )
conn.commit()
