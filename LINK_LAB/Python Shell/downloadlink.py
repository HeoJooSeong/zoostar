import requests
import pymysql
import urllib2
import os
import datetime
import time
from bs4 import BeautifulSoup

def mysql(sql):
	db = pymysql.connect(host='localhost',user='root',passwd='1234#link',db='papercrawler')
	cursor = db.cursor()
	cursor.execute(sql)
	db.commit()
	db.close()
	print "Success Database UPDATE!!!"

t = requests.get("http://sci-hub.io/")
print t
while True:
	db = pymysql.connect(host='localhost',user='root',passwd='1234#link',db='papercrawler')
	cursor = db.cursor()
	# cnt is value about fail count
	# execute SQL query using execute() method.
	cursor.execute("SELECT id,doi FROM manuscript WHERE archiveSave = 0 OR archiveSave is null LIMIT 1")
	results = cursor.fetchall()
	db.close()
	print results
	id = results[0][0]
	doi = results[0][1]
	print "manuscript id = " ,id
	print "doi = "  ,doi


	req = requests.post("http://sci-hub.io/" + doi)
	content = req.content
	bs = BeautifulSoup(content,"lxml")

	if(bs.find(id="save") != None):
		html =  bs.find(id="save")
		html = html.find('a')['onclick']
		html = html[(html.index('location.href=')):html.index('.pdf')].strip()
		html = html[(html.index('ht')):].strip() + ".pdf?download=true"
		print html
		html = '\''+html+'\''
		sql="INSERT into downloadLink(manuscript_id,downloadLink) VALUES (%d,%s)" % (id,html)
		mysql(sql)
		sql="UPDATE manuscript set archiveSave = -3 WHERE id = %d" % id  #download link is exist !!!!
		mysql(sql)
	else:
		print "Download Link is not exist"
		sql = "UPDATE manuscript set archiveSave = -1 WHERE id = %d" % id
		mysql(sql)
		print sql

	time.sleep(30) 