#!/usr/bin/env python3 

import sqlite3
import sys
conn = sqlite3.connect('wizard_duels.db')
c = conn.cursor()


conn.commit()
