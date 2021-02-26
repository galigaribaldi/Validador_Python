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
###Crear una nueva tarea
def createCourseWork(numId, titulo, descripcion, link1, link2):
    coursework = {
        'title': titulo,
        'description': descripcion,
        'materials': [
            {'link': {'url': link1}},
            {'link': {'url': link2}}
        ],
        'workType': 'ASSIGNMENT',
        'state': 'PUBLISHED',
    }
    coursework = service.courses().courseWork().create(
        courseId=numId, body=coursework).execute()
    print('Assignment created with ID {%s}' % coursework.get('id'))

#createCourseWork(275450839438,'Nueva Tarea', 'Descripcion mamalona', 'https://youtu.be/pMbXKsp2hy4', 'https://youtu.be/9gA1DE1zqEA')

##Cosultar el progreso de todas las actividades
def list_submissions(course_id, coursework_id):
    """ Lists all student submissions for a given coursework. """
    submissions = []
    page_token = None
    while True:
        coursework = service.courses().courseWork()
        response = coursework.studentSubmissions().list(
            pageToken=page_token,
            courseId=course_id,
            courseWorkId=coursework_id,
            pageSize=10).execute()
        submissions.extend(response.get('studentSubmissions', []))
        page_token = response.get('nextPageToken', None)
        if not page_token:
            break

    if not submissions:
        print('No student submissions found.')
    else:
        print('Student Submissions:')
       # print(submissions)
        for submission in submissions:
            #print("%s was submitted at %s" %(submission.get('id'),submission.get('creationTime')))
            #print(submission)
            print("Course ID: [%s]\nCourseWork ID: [%s]\nUserID: [%s]" %(submission.get('courseId'), submission.get('courseWorkId'), submission.get('userId')))
            print("\n")
    # [END classroom_list_submissions]
#283498401726
list_submissions(275450839438, 283498401726)

##Consultar el progrso de las actividades de 
def list_student_submissions(course_id, coursework_id, user_id):
    """ Lists all coursework submissions for a given student. """
    # [START classroom_list_student_submissions]
    submissions = []
    page_token = None
    while True:
        coursework = service.courses().courseWork()
        response = coursework.studentSubmissions().list(
            pageToken=page_token,
            courseId=course_id,
            courseWorkId=coursework_id,
            userId=user_id).execute()
        submissions.extend(response.get('studentSubmissions', []))
        page_token = response.get('nextPageToken', None)
        if not page_token:
            break
    if not submissions:
        print('No student submissions found.')
    else:
        print('Student Submissions:')
        print(submissions)
        for submission in submissions:
            #print("%s was submitted at %s" % (submission.get('id'),submission.get('creationTime')))
            print("Course ID: [%s]\nCourseWork ID: [%s]\nUserID: [%s]" %(submission.get('courseId'), submission.get('courseWorkId'), submission.get('userId')))
            print("\n")
            print(submission.get('id'))

list_student_submissions(275450839438, 283498401726, 102278109585891765381)
def updateCalificacion(course_id, coursework_id, student_id):
    studentSubmission = {
    'assignedGrade': 99,
    'draftGrade': 80
    }
    service.courses().courseWork().studentSubmissions().turnIn(
        courseId=course_id,
        courseWorkId=coursework_id,
        id='Cg0I4teW1CYQvp_JjqAI',
        #updateMask='assignedGrade,draftGrade',
        body={}).execute()
        #body=studentSubmission).execute()
updateCalificacion(275450839438, 283498401726, 100905005032845497156)