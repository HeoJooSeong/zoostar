import subprocess
import pymysql

conn = pymysql.connector(host='localhost'),user='root',passwd='1234',db='mysql')
cur=conn.cursor()
cur.execute("select~")
r=cur.fetchall()

cur.close()
conn.close()

subprocess.call('ls -al')
