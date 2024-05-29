"""
File: couchdb_data_store.py
Author: tushar
Description: This file contains a class for couchdb data store.
"""
import couchdb
from app.configuration.logging_config import logger
from app.databases.couch.couchdb_connection import connection
from couchdb.http import Unauthorized
from app.utilities.exceptions import UnprocessableEntity
from app.configuration.messages import Messages

class CouchDBDataStore:
    """
    CouchDBDataStore: Represents a connection to a CouchDB database.
    """
    def __init__(self) -> None:
        self.client = connection()
    
    def create_database(self, database_name):
        """
        Parameters:
            database_name (str): Name of the database.
        Opration:
            Create a new database in the couchdb.
        """
        try:
            # Create the database
            db = self.client.create(database_name)
            # Define design document with views
            design_doc = {
                "_id": "_design/example",
                "language": "python",
                "views": {
                    "by_url_key": {
                        "map": """
                            def map_function(doc):
                                if doc['type'] == 'PLATFORM_XPATH' and 'urls' in doc:
                                    for url in doc['urls']:
                                        emit(url['key'], None)
                        """
                    }
                }
            }
            # Save the design document to the database
            db.save(design_doc)
            logger.info("Database created successfully.")
        except couchdb.http.PreconditionFailed:
            logger.info("Database already exists.")

    def get_database(self, database_name):
        """
        Parameters:
            database_name (str): Name of the database.
        Opration:
            Get the database from the couchdb.
        """
        try:   
            if database_name in self.client:
                return self.client[database_name]
            else:
                return None
        except Unauthorized:
            raise UnprocessableEntity(Messages.COUCH_CREDENTAILS_ERROR)
    
    def find_one(self, database, query):
        """
        Parameters:
            query (dict): Query to find the document.
        Opration:
            Find the document in the couchdb.
        """
        try:
            all_documents = []
            framework_document = database.find(query)

            for row in framework_document:
                all_documents.append(row)

            if not len(all_documents):
                return {}
            return dict(all_documents[0])
        except Exception as err:
            logger.info("Error in couch db find_one fucntion:", err)
            raise err

    def find_all(self,database, query):
        """
        Parameters:
            query (dict): Query to find the document.
        Opration:
            Find the documents in the couchdb.
        """
        try:
            all_documents = []
            framework_document = database.find(query)

            for row in framework_document:
                all_documents.append(dict(row))

            if not len(all_documents):
                return []
            return all_documents
        except Exception as err:
            logger.info("Error in couch db find_one fucntion:", err)
            raise err
    
    def update(self, database, document_id, updated_value):
        """
        Parameters:
            document_id (string): id of the document which need to update.
            updated_value (dict): new  values for document.
        Opration:
            Update the document in the couchdb.
        """
        try:
            document = database[document_id]
            for key, value in updated_value.items():
                document[key] = value
            return database.save(document)
        except Exception as err:
            logger.info("Error in couch db update fucntion:", err)
            raise err
    
    def delete(self,database,doc_id):
        """
        Parameters:
            doc_id (string): id of the document which need to delete.
        Opration:
            Delete the document in the couchdb.
        """
        try:
            document = database[doc_id]
            return database.delete(document)
        except Exception as err:
            logger.info("Error in couch db delete fucntion:", err)
            raise err