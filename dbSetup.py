import sqlite3

def Migration():
    con = sqlite3.connect("fs.db")
    cur = con.cursor()
    # test table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS test (
            testField TEXT
        );
    """)
    
    # the table with all of the files info
    # path will be the full path of the file including filename
    # isFile will be 1 if it is a file and zero otherwise
    # same goes for isDir but with directories 
    # fModeBits is the file permissions to parse https://stackoverflow.com/questions/5337070/how-can-i-get-the-unix-permission-mask-from-a-file
    # lastAccess is the last time the file was accessed in seconds
    cur.execute("""
        CREATE TABLE IF NOT EXISTS files (
            name TEXT,
            path TEXT,
            isFile INTEGER,
            isDir INTEGER,
            fModeBits INTEGER,
            size INTEGER,
            lastAccess INTEGER
        )
    """)
    
    cur.close()
    return con