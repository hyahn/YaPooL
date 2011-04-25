#Author: RemiBouchar
'''
This module contain the method to create database and query view
the defaut database is load once the module is loaded

Security:
the access is now secure, so to make it work in dev mode, you need to:
1Set Up a admin account on your couchdb instance
2create a file called .couchDbCredentials at the root of the djangoproject(kuestionsWS),

the file should contain only one line, formated like this:
login:password

NOTE: it may not work on windows, because of the different convention for the nextline character
'''

print 'loading couchdb layer'
from couchdb import *

USER_DB='_users'
YAPOOL_DB='yapooldb'
SERVER_URL='http://localhost:5984/'
def loadDatabase (server,dbname=USER_DB) :
  '''
  This method aim to load or create any couchdb database in a LOCAL couchdb installation
  '''
  try :
    print 'loading the database ',dbname
    db = server[dbname]
    return db
  except Exception :
    print 'unable to retrieve the users database'
    return None
  
server=None
  
def initServer(server=server,url=SERVER_URL) :
  if server == None :
    server=Server(url)
  server=Server(url)
  file = open('.couchDbCredentials','r')
  creds=file.readline().replace('\n','').split(':')
  server.resource.credentials = (creds[0],creds[1])
  print server
  return server

server=initServer()
db=loadDatabase(server)

def getDb() : return db
def getServer() : return server


def query (query) :
  '''
  this function perform a new javascript query directly in the database,
  thus it's not optimized at all, but for now it will do the trick.
  TODO : fix the loaded or not part( add condition)
  '''
  try :
    return db.query(query)
  except ServerError :
    print 'ServerError, error in query'





def view(viewName,keyValue=None) :
  '''
  This function question directly a existing couchdb view
  thus it's a optimized way to retrieve data quickly
  TODO: add offset parameters
  '''
  return db.view(viewName,key=keyValue)

def getDocument(id):
  return db.get(id)

    
  

    



  
 
    

