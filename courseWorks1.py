#from __future__ import print_function
#from googleapiclient import errors
from googleapiclient.discovery import build
import os.path
import pickle
#####
###Course Id = 291374157706
### CourseWork = 291383409581
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

#createCourseWork(291374157706,'Nueva Tarea', 'Descripcion mamalona', 'https://youtu.be/pMbXKsp2hy4', 'https://youtu.be/9gA1DE1zqEA') 

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
        print(submissions)
        input()
        for submission in submissions:
            #print("%s was submitted at %s" %(submission.get('id'),submission.get('creationTime')))
            #print(submission)
            print("Curso ID: [%s]\Tarea ID: [%s]\nUserID: [%s]\nSubmission ID: [%s]" %(submission.get('courseId'), submission.get('courseWorkId'), submission.get('userId'), submission.get('id')))
            print("\n")
    # [END classroom_list_submissions]

list_submissions(291374157706, 291383409581)

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
        #print(submissions)
        for submission in submissions:
            #print("%s was submitted at %s" % (submission.get('id'),submission.get('creationTime')))
            print("Course ID: [%s]\nCourseWork ID: [%s]\nUserID: [%s]" %(submission.get('courseId'), submission.get('courseWorkId'), submission.get('userId')))
            print("Submission Id: ", submission.get('id'))
            print("\n")

#list_student_submissions(291374157706, 291383409581, 113580004965193682564)
def updateCalificacion(course_id, coursework_id, submission_id,student_id):
    studentSubmission = {
    'assignedGrade': 1000,
    'draftGrade': 8000
    }
    service.courses().courseWork().studentSubmissions().patch(
        courseId=course_id,
        courseWorkId=coursework_id,
        id=submission_id,
        updateMask='assignedGrade,draftGrade',
        body=studentSubmission).execute()
    ##
    
#updateCalificacion(291374157706, 291383409581, 'Cg4I99KxudYDEK33t769CA', 113580004965193682564)

##Agregar un archivo como respuesta
def add_attachment(course_id, coursework_id, submission_id):
    """ Adds an attachment to a student submission. """
    request = {
        'addAttachments': [
            {'link': {'url': 'http://example.com/quiz-results'}},
            {'link': {'url': 'http://example.com/quiz-reading'}}
        ]
    }
    coursework = service.courses().courseWork()
    coursework.studentSubmissions().modifyAttachments(
        courseId=course_id,    
        courseWorkId=coursework_id,
        id=submission_id,
        body=request).execute()

#add_attachment(291374157706, 291383409581, 'Cg4I99KxudYDEK33t769CA')

