#!/usr/bin/env python3
import dbSetup
import os
import time

ignored= [".git", "__pycache__", "fs.db", "fs.db-journal"]

def insertFiles(db, currentDir):
    
    for file in os.scandir(currentDir):
        if file.name in ignored:
            continue
        
        if file.is_dir():
            insertFiles(db, file.path)
        db.execute("""
            INSERT INTO files VALUES (
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?
            );
        """, [
            file.name,
            file.path,
            1 if file.is_file() else 0,
            1 if file.is_dir() else 0,
            file.stat().st_mode,
            file.stat().st_size,
            file.stat().st_atime,
        ])
        # print(file.name)
    return

def main():
    db = dbSetup.Migration()
    
    cur = db.cursor()
    cur.execute("DELETE FROM files")
    insertFiles(cur, ".")
    cur.close()
    db.commit()
    
    # insertFiles(db, '.')
    print("Welcome to the fsDB\n\n")
    while(True):
        inp = input("What would you like to do?\n> ").lower().split()
        
        if(len(inp)>0 and inp[0] == "refresh"):
            cur = db.cursor()
            cur.execute("DELETE FROM files")
            insertFiles(cur, ".")
            cur.close()
            db.commit()
        elif(len(inp)> 0 and inp[0] == "exit"):
            db.close()
            return 0

if __name__ =="__main__":
    main()