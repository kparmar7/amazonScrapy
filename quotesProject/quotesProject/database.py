import sqlite3

conn = sqlite3.connect('sqlite3.db')
curr = conn.cursor()

# curr.execute("""
#                 create table quotes(
#                     title text,
#                     author text,
#                     tab text)
#             """)

curr.execute("""insert into quotes values('aa','bb','cc')""")

conn.commit()
conn.close()