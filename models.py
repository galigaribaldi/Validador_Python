#from __future__ import print_function
#from googleapiclient import errors
from googleapiclient.discovery import build
import os.path
import pickle
def returns_service():
    #####
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    service = build('classroom', 'v1', credentials=creds)
    return service