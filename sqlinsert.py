
















	
























#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import MySQLdb as mdb


# Obtain a database connection to the MySQL instance
db_host = 'localhost'
db_user = 'name'
db_pass = 'pass'
db_name = 'db-name'
con = mdb.connect(db_host, db_user, db_pass, db_name)

def obtain_parse_wiki_snp500():














      
  with open('/home/your-name/Downloads/your-file.csv') as yf_data:
     
    for y in yf_data:
       import unicodedata 
       )
  




            

          
       prices = []
             
       p = y.rstrip('\n')
       p = y.strip().split(',')
       prices.append( (
                   ("KR"),p[0], p[1], p[2], p[3], p[4],p[5]) )
      
       
       print prices 
  # Amend the data to include the vendor ID and symbol ID

       
#  print symbol
  # Create the insert strings
       column_str = """symbol, price_date,open_price, high_price, low_price,close_price, volume"""
       insert_str = ("%s, " * 7)[:-2]
       final_str = "INSERT INTO daily_price (%s) VALUES (%s)" % (column_str, insert_str)
      # data = [prices]
     #  print data  
  # Using the MySQL connection, carry out an INSERT INTO for every symbol
       with con: 
         cur = con.cursor()
         cur.executemany(final_str, prices)






if __name__ == "__main__":
  prices = obtain_parse_wiki_snp500()
  insert_snp500_symbols(prices)






