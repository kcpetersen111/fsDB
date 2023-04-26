#!/usr/bin/env python3 

import sqlite3
import sys
conn = sqlite3.connect('wizard_duels.db')
c = conn.cursor()

if sys.argv[1] == 'users':
    c.execute("INSERT INTO users VALUES (?,?,?)", (sys.argv[2],sys.argv[3],sys.argv[4]))
elif sys.argv[1] == 'follows':
    c.execute("INSERT INTO follows VALUES (?,?)", (sys.argv[3],sys.argv[2]))
elif sys.argv[1] == 'posts':
    #c.execute("INSERT INTO posts VALUES (?,?,?)", (sys.argv[2],sys.argv[3],sys.argv[4]))
    c.execute("INSERT INTO posts (user_id, content) VALUES (4, 'This is post #1')")
    c.execute("INSERT INTO posts (user_id, content) VALUES (3, 'This is post #2')")
    c.execute("INSERT INTO posts (user_id, content) VALUES (1, 'This is post #3')")
elif sys.argv[1] == 'comments':
    #c.execute("INSERT INTO comments VALUES (?,?,?,?,?)", (sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6]))
    c.execute("INSERT INTO comments (post_id, user_id, content) VALUES (1, 2, 'This is a comment on post #1')")
    c.execute("INSERT INTO comments (post_id, user_id, content, parent_id) VALUES (1, 1, 'This is a reply to the first comment', 1)")
    c.execute("INSERT INTO comments (post_id, user_id, content, parent_id) VALUES (1, 2, 'This is a reply to the reply', 2)")
    c.execute("INSERT INTO comments (post_id, user_id, content) VALUES (2, 1, 'This is a comment on post #2')")
    c.execute("INSERT INTO comments (post_id, user_id, content, parent_id) VALUES (1, 2, 'This is a nested reply to the first comment', 3)")

    c.execute("INSERT INTO comments (post_id, user_id, content, parent_id) VALUES (1, 2, 'This is a reply to the second comment', 6)")
elif sys.argv[1] == 'house':
    c.execute("INSERT INTO houses (user_id, housename) VALUES (?,?)", (sys.argv[2],sys.argv[3]))
else:
    print('that table in not in the schema')

conn.commit()
