from sqlalchemy.orm import sessionmaker
from models import Jackets, db_connect, create_jackets_table


class AsosPipeline(object):
    """Asos pipeline for storing scraped items in the database"""
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates jackets table.
        """
        # print 'AsosPipeline\n\n\n'
        engine = db_connect()
        create_jackets_table(engine)
        self.Session = sessionmaker(bind=engine)
    
    def process_item(self, item, spider):
        """Save jacket items in the database.
        
        This method is called for every item pipeline component.
        
        """
        session = self.Session()
        jacket = Jackets(**item)
        
        # print 'processing item', item['name'], '\n\n'
        
        try:
            session.add(jacket)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        
        return item
