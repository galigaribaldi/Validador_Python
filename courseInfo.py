#from __future__ import print_function
#from googleapiclient import errors
from googleapiclient.discovery import build
import os.path
import pickle
#####
creds = None
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
        
service = build('classroom', 'v1', credentials=creds)
# Call the Classroom API
results = service.courses().list(pageSize=10).execute()
courses = results.get('courses', [])
for i in courses:
    print(i["id"], i["name"])

course = service.courses().get(id=27773386961).execute()
print('Course "{%s}" found.' % course.get('name'))
#course = service.courses().create(body=course).execute()
#print('Course created: %s %s' % (course.get('name'), course.get('id')))