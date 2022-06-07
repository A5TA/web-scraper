# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class AmazonscraperPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = sqlite3.connect("products.db")
        self.curr = self.conn.cursor()
        
    def create_table(self):
        #create a table in sqlite
        self.curr.execute("""DROP TABLE IF EXISTS products_tb""")
        self.curr.execute("""CREATE TABLE products_tb(
                        name text,
                        reviews INTEGER,
                        price INTEGER,
                        url text
                        )""")
    
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self,item):
        self.curr.execute("""INSERT INTO products_tb values (?,?,?,?) """,(
            item['name'][0], 
            item['reviews'][0],
            item['price'][0],
            item['url'][0]
        ))
        self.conn.commit()
