#from __future__ import print_function
from googleapiclient.discovery import build
from googleapiclient import errors
import os.path
import pickle
###Modulo propio
import models as model

def get_all_courses():
    service = model.returns_service()
    results = service.courses().list(pageSize=10).execute()
    courses = []
    for i in results['courses']:
        l = []
        #print(i['id']);print(i['name']);print(i['descriptionHeading'])
        l.append(i['id'])
        l.append(i['name'])
        l.append(i['descriptionHeading'])
        courses.append(l)
    return courses
def get_users_by_idCourse(Courses_id):
    service = model.returns_service()
    results = service.courses().students().list(courseId=Courses_id)
    studentCourses =results.execute()
    studentInfo=[]
    for i in studentCourses['students']:
        l = []
        #print(i['userId']);print(i['profile']['name']['fullName']);print(i['profile']['emailAddress'])
        l.append(i['userId'])
        l.append(i['profile']['name']['fullName'])
        l.append(i['profile']['emailAddress'])
        studentInfo.append(l)
    return studentInfo
    
def viewTeachers(Courses_id):
    service = model.returns_service()
    results = service.courses().teachers().list(courseId=Courses_id)
    print(results, type(results))

def get_course_by_id(course_id):
    """ Retrieves a classroom course by its id. """
    service = model.returns_service()
    try:
        course = service.courses().get(id=course_id).execute()
        #print('Course "{%s}" found.' % course.get('name'))
    except errors.HttpError as error:
        #print('Course with ID "{%s}" not found.' % course_id)
    # [END classroom_get_course]
        return error
    return course

def courses_list_activities(course_id):
    service = model.returns_service()
    results = service.courses().courseWork().list(courseId=course_id).execute()
    list_activities = []
    for i in results['courseWork']:
        l = []
        #print(i['id'])
        l.append(i['id'])
        
        try:
            #print(i['title'])
            l.append(i['title'])
        except:
            l.append("Sin Titulo")
        
        try:
            #print(i['description'])
            l.append(i['description'])
        except:
            #print("Sin decripcion")
            l.append("Sin decripcion")
        
        try:
            #print(i['creationTime'])
            l.append(i['creationTime'])
        except:
            l.append("Sin hora")
        
        try:
            #print(i['maxPoints'])
            l.append(i['maxPoints'])
        except KeyError:
            #print("Sin puntaje")
            l.append("Sin puntaje")
        list_activities.append(l)
    return list_activities

def sumbiss_student_courseWork(course_id, course_work_id, student_id):
    service = model.returns_service()
    results = service.courses().courseWork().studentSubmissions().list(courseId=course_id, courseWorkId=course_work_id).execute()
    #print(results)
    for i in results['studentSubmissions']:
        print("Fecha de Dejado", i['creationTime'])
        print(i['state'])
        try:
            print(i['assignedGrade'])
        except KeyError:
            print("sin calificacion")
        try:
            print(i['updateTime'])
        except KeyError:
            print("sin Entregar")
        print(i['userId'])
        print("\n")
        print(i)
        print("\n")
#c = get_course_by_id(275450839438)
#c = get_users_by_idCourse(275450839438)
#c = get_all_courses()
CourseworkId=326779603805
StudentId=113580004965193682564
CourseId = 275450839438
#c = sumbiss_student_courseWork(CourseId,CourseworkId,StudentId)


courses_list_activities(CourseId)