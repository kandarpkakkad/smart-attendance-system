from django.shortcuts import render, redirect
from login.models import Professor, Student, Admin, FacultyAdvisor as fa
from home.models import ProfessorTimeTable as ptt, TimeTable as ttable, Attendance as att, StudentSubject
import numpy as np
import ast
import datetime
import itertools
import xlwt

import os
import sys
sys.path.append('../')

# from Facenet_Real_time_face_recognition.identify_face_video import *



# sys.path.insert(0, 'F://study//Mini Project 3//Facenet_Real_time_face_recognition//')
# print(smart_attendance())

# Create your views here.


role1 = ''
role = ''
result = []
username = ''
login = 0
timetable = {}
dat = ''
cname = ''
lec_type = 0
subject = ''
sub = list()
pern = list()
perl = list()
pert = list()
colorn = list()
colorl = list()
colort = list()
colora = list()
lec = list()
tut = list()
lab = list()
avg = list()
all = list()


def index(array, key):
    if key in array:
        return array.index(key)
    return -1


def calculate_attendance(username):
    global role
    sub = list()
    pern = list()
    perl = list()
    pert = list()
    colorn = list()
    colorl = list()
    colort = list()
    colora = list()
    lec = list()
    tut = list()
    lab = list()
    avg = list()
    all = list()
    result = Student.objects.filter(username=username)
    branch = ''
    semester = ''
    roll = ''
    if len(result):
        for i in result:
            branch = i.branch
            semester = i.semester
            roll = i.roll_number
        ss = StudentSubject.objects.filter(branch=branch, semester=semester)
        for i in ss:
            s = ''
            if i.lecture_type == '0':
                s = i.lecture + '-N'
            elif i.lecture_type == '1':
                s = i.lecture + '-L'
            elif i.lecture_type == '2':
                s = i.lecture + '-T'
            sub.append(s)
        sub.sort()
        for i in sub:
            d1 = att()
            d2 = att()
            if i[len(i) - 1] == 'N':
                d1 = att.objects.filter(roll_number=roll, lecture=i[:-2], lecture_type='0', status='P')
                d2 = att.objects.filter(roll_number=roll, lecture=i[:-2], lecture_type='0')
                if len(d2) == 0:
                    pern.append(0)
                    colorn.append('red')
                    lec.append(i[:-2])
                else:
                    pern.append(len(d1) / len(d2) * 100)
                    if len(d1) / len(d2) * 100 < 65:
                        colorn.append('red')
                    elif len(d1) / len(d2) * 100 < 75:
                        colorn.append('orange')
                    if len(d1) / len(d2) * 100 < 85:
                        colorn.append('yellow')
                    else:
                        colorn.append('green')
                    lec.append(i[:-2])
            elif i[len(i) - 1] == 'L':
                d1 = att.objects.filter(roll_number=roll, lecture=i[:-2], lecture_type='1', status='P')
                d2 = att.objects.filter(roll_number=roll, lecture=i[:-2], lecture_type='1')
                if len(d2) == 0:
                    perl.append(0)
                    colorl.append('red')
                    lab.append(i[:-2])
                else:
                    perl.append(len(d1) / len(d2) * 100)
                    if len(d1) / len(d2) * 100 < 65:
                        colorl.append('red')
                    elif len(d1) / len(d2) * 100 < 75:
                        colorl.append('orange')
                    if len(d1) / len(d2) * 100 < 85:
                        colorl.append('yellow')
                    else:
                        colorl.append('green')
                    lab.append(i[:-2])
            elif i[len(i) - 1] == 'T':
                d1 = att.objects.filter(roll_number=roll, lecture=i[:-2], lecture_type='2', status='P')
                d2 = att.objects.filter(roll_number=roll, lecture=i[:-2], lecture_type='2')
                if len(d2) == 0:
                    pert.append(0)
                    colort.append('red')
                    tut.append(i[:-2])
                else:
                    pert.append(len(d1) / len(d2) * 100)
                    if len(d1) / len(d2) * 100 < 65:
                        colort.append('red')
                    elif len(d1) / len(d2) * 100 < 75:
                        colort.append('orange')
                    if len(d1) / len(d2) * 100 < 85:
                        colort.append('yellow')
                    else:
                        colort.append('green')
                    tut.append(i[:-2])
            if i[:-2] not in all:
                all.append(i[:-2])
        for i in all:
            cnt = 0
            per = 0
            n = i + '-N'
            l = i + '-L'
            t = i + '-T'
            if n in sub:
                d1 = att.objects.filter(roll_number=roll, lecture=i, lecture_type='0', status='P')
                d2 = att.objects.filter(roll_number=roll, lecture=i, lecture_type='0')
                if len(d2) == 0:
                    per += 0
                    cnt += 1
                else:
                    per += len(d1) / len(d2) * 100
                    cnt += 1
            if l in sub:
                d1 = att.objects.filter(roll_number=roll, lecture=i, lecture_type='1', status='P')
                d2 = att.objects.filter(roll_number=roll, lecture=i, lecture_type='1')
                if len(d2) == 0:
                    per += 0
                    cnt += 1
                else:
                    per += len(d1) / len(d2) * 100
                    cnt += 1
            if t in sub:
                d1 = att.objects.filter(roll_number=roll, lecture=i, lecture_type='2', status='P')
                d2 = att.objects.filter(roll_number=roll, lecture=i, lecture_type='2')
                if len(d2) == 0:
                    per += 0
                    cnt += 1
                else:
                    per += len(d1) / len(d2) * 100
                    cnt += 1
            per = per / cnt
            avg.append(per)
            if per < 65:
                colora.append('red')
            elif per < 75:
                colora.append('orange')
            elif per < 85:
                colora.append('yellow')
            else:
                colora.append('green')
        dict = {
            'subsa': all,
            'subsn': lec,
            'subsl': lab,
            'subst': tut,
            'percentagea': avg,
            'percentagen': pern,
            'percentagel': perl,
            'percentaget': pert,
            'clra': colora,
            'clrn': colorn,
            'clrl': colorl,
            'clrt': colort,
        }
        return dict


def colspan(s, e):
    start = {'09:00:00': 0, '09:50:00': 1, '11:15:00': 2, '12:15:00': 3, '14:00:00': 4, '15:00:00': 5, '16:15:00': 6, '17:15:00': 7}
    end = {'09:50:00': 0, '10:50:00': 1, '12:15:00': 2, '13:15:00': 3, '15:00:00': 4, '16:00:00': 5, '17:15:00': 6, '18:05:00': 7}
    st = start[str(s)]
    ed = end[str(e)]
    return ed - st + 1


def dashboard(request):
    global role, result, username, login, timetable, sub, pern, colorn, perl, pert, avg, colora, colorl, colorn, colort, lec, tut, lab, all
    if request.method == 'POST':
        sub = list()
        pern = list()
        perl = list()
        pert = list()
        colorn = list()
        colorl = list()
        colort = list()
        colora = list()
        lec = list()
        tut = list()
        lab = list()
        avg = list()
        all = list()
        role = request.POST.get('role', None)
        if role == 'professor':
            username = request.POST['username']
            password = request.POST['password']
            result = Professor.objects.filter(username=username, password=password)
            timetable = {
                'name': ['', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'],
                'time': ['9:00 - 9:50', '9:50 - 10:50', '11:15 - 12:15', '12:15 - 1:15', '2:00 - 3:00', '3:00 - 4:00',
                         '4:15 - 5:15', '5:15 - 6:05'],
                'start_time': [[] for i in range(6)],
                'end_time': [[] for i in range(6)],
                'cols': [[] for i in range(6)],
                'subject': [[] for i in range(6)],
                'classes': [[] for i in range(6)],
            }
            days = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5}
            if len(result):
                prof_tt = ptt.objects.filter(prof_username=username)
                for i in prof_tt:
                    timetable['start_time'][days[i.day]].append(str(i.start_time))
                    timetable['end_time'][days[i.day]].append(str(i.end_time))
                    timetable['cols'][days[i.day]].append(colspan(i.start_time, i.end_time))
                    timetable['subject'][days[i.day]].append(str(i.lecture))
                    timetable['classes'][days[i.day]].append(str(i.class_name))
                x = ""
                for r in result:
                    x = str(r.name)
                res = {'name': x}
                response = render(request, 'home/dashboard.html', {'tt': timetable, 'result': x, 'role': role})
                response.set_cookie('username', username, max_age=86400*2)
                response.set_cookie('result', res, max_age=86400*2)
                response.set_cookie('role', role, max_age=86400*2)
                response.set_cookie('tt', timetable, max_age=86400 * 2)
                return response
            else:
                return redirect('/login/')
        elif role == 'student':
            username = request.POST['username']
            password = request.POST['password']
            result = Student.objects.filter(username=username, password=password)
            branch = ''
            semester = ''
            roll = ''
            if len(result):
                dict = calculate_attendance(username)
                x = ""
                y = ""
                for r in result:
                    x = r.name
                    y = r.roll_number
                res = {'name': x, 'roll_number': y}
                response = render(request, 'home/dashboard.html', {'percentagea': avg, 'subsa':all, 'subst': tut, 'subsl':lab , 'subsn': lec, 'percentagen': pern, 'percentagel': perl, 'percentaget': pert, 'result': x, 'role': role, 'clrn': colorn, 'clrl': colorl,'clrt': colort,'clra': colora})
                response.set_cookie('username', username, max_age=86400 * 2)
                response.set_cookie('result', res, max_age=86400 * 2)
                response.set_cookie('role', role, max_age=86400 * 2)
                response.set_cookie('dict', dict, max_age=86400 * 2)
                return response
            else:
                return redirect('/login/')
        elif role == 'admin':
            username = request.POST['username']
            password = request.POST['password']
            result = Admin.objects.filter(username=username, password=password)
            if len(result):
                response = redirect('/admin/')
                response.set_cookie('result', result, max_age=86400 * 2)
                response.set_cookie('role', role, max_age=86400 * 2)
                return response
            else:
                return redirect('/login/')
        elif role == 'facultyAdvisor':
            username = request.POST['username']
            password = request.POST['password']
            result = Professor.objects.filter(username=username, password=password)
            timetable = {
                'name': ['', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'],
                'time': ['9:00 - 9:50', '9:50 - 10:50', '11:15 - 12:15', '12:15 - 1:15', '2:00 - 3:00', '3:00 - 4:00',
                         '4:15 - 5:15', '5:15 - 6:05'],
                'start_time': [[] for i in range(6)],
                'end_time': [[] for i in range(6)],
                'cols': [[] for i in range(6)],
                'subject': [[] for i in range(6)],
                'classes': [[] for i in range(6)],
            }
            days = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5}
            if len(result):
                prof_tt = ptt.objects.filter(prof_username=username)
                for i in prof_tt:
                    timetable['start_time'][days[i.day]].append(str(i.start_time))
                    timetable['end_time'][days[i.day]].append(str(i.end_time))
                    timetable['cols'][days[i.day]].append(colspan(i.start_time, i.end_time))
                    timetable['subject'][days[i.day]].append(str(i.lecture))
                    timetable['classes'][days[i.day]].append(str(i.class_name))
                x = ""
                for r in result:
                    x = str(r.name)
                res = {'name': x}
                result = fa.objects.filter(username=username, password=password)
                if len(result):
                    branch = ""
                    for r in result:
                        branch = str(r.branch)
                    response = render(request, 'home/dashboard.html', {'tt': timetable, 'result': x, 'role': role, 'branch': branch})
                    response.set_cookie('username', username, max_age=86400 * 2)
                    response.set_cookie('result', res, max_age=86400 * 2)
                    response.set_cookie('role', role, max_age=86400 * 2)
                    response.set_cookie('tt', timetable, max_age=86400 * 2)
                    response.set_cookie('branch', branch, max_age=86400 * 2)
                    return response
                else:
                    return redirect('/login/')
            else:
                return redirect('/login/')
        else:
            return redirect('/login/')
    else:
        if request.COOKIES.get('result') != "":
            role = request.COOKIES.get('role')
            if role == 'professor':
                result = request.COOKIES.get('result')
                result = ast.literal_eval(result)
                timetable = request.COOKIES.get('tt')
                timetable = ast.literal_eval(timetable)
                response = render(request, 'home/dashboard.html', {'tt': timetable, 'result': result['name'], 'role': role})
                response.set_cookie('result', result, max_age=86400 * 2)
                response.set_cookie('role', role, max_age=86400 * 2)
                response.set_cookie('tt', timetable, max_age=86400 * 2)
                return response
            elif role == 'student':
                result = request.COOKIES.get('result')
                result = ast.literal_eval(result)
                dict = request.COOKIES.get('dict')
                dict = ast.literal_eval(dict)
                response = render(request, 'home/dashboard.html', {'percentagea': dict['percentagea'], 'subsa': dict['subsa'], 'subst': dict['subst'], 'subsl': dict['subsl'], 'subsn': dict['subsn'], 'percentagen': dict['percentagen'], 'percentagel': dict['percentagel'], 'percentaget': dict['percentaget'], 'result': result['name'], 'role': role, 'clrn': dict['clrn'], 'clrl': dict['clrl'], 'clrt': dict['clrt'], 'clra': dict['clra']})
                response.set_cookie('result', result, max_age=86400 * 2)
                response.set_cookie('role', role, max_age=86400 * 2)
                response.set_cookie('dict', dict, max_age=86400 * 2)
                return response
            elif role == 'facultyAdvisor':
                result = request.COOKIES.get('result')
                result = ast.literal_eval(result)
                timetable = request.COOKIES.get('tt')
                timetable = ast.literal_eval(timetable)
                branch = request.COOKIES.get('branch')
                response = render(request, 'home/dashboard.html', {'tt': timetable, 'result': result['name'], 'role': role, 'branch': branch})
                response.set_cookie('result', result, max_age=86400 * 2)
                response.set_cookie('role', role, max_age=86400 * 2)
                response.set_cookie('tt', timetable, max_age=86400 * 2)
                response.set_cookie('branch', branch, max_age=86400 * 2)
                return response
            else:
                return redirect('/admin/')
        else:
            return redirect('/login/')


def take_attendance(request, lecture, class_name):
    global role, result, username, login
    if request.COOKIES.get('result') != "":
        stu = Student.objects.all()
        stun = []
        if lecture != '-' and class_name != '-':
            length = len(class_name)
            if length == 4:
                sem = class_name[0]
                branch = class_name[1:length - 1]
                batch = class_name[length - 1]
                stu = Student.objects.filter(semester=sem, branch=branch, batch=batch)
                for i in stu:
                    stun.append(i.roll_number)
            elif length == 5:
                sem = class_name[0]
                branch = class_name[1:length - 2]
                batch = class_name[length - 2:]
                print(sem, branch, batch)
                stu = Student.objects.filter(semester=sem, branch=branch, lab_batch=batch)
                for i in stu:
                    print(i.roll_number)
                    stun.append(i.roll_number)
            elif length == 6:
                sem = class_name[0]
                branch = class_name[1:length - 3]
                cl = class_name[length - 3]
                batch = class_name[length - 2:]
                stu = Student.objects.filter(semester=sem, branch=branch, batch=cl,  tut_batch=batch)
                for i in stu:
                    stun.append(i.roll_number)
            if request.method == 'POST':
                arr = request.POST.getlist('roll')
                print(arr)
                for i in stun:
                    attend = att()
                    attend.lecture = lecture
                    attend.prof_username = request.COOKIES.get('result')
                    attend.prof_username = ast.literal_eval(attend.prof_username)
                    attend.prof_username = attend.prof_username['name']
                    attend.roll_number = i
                    if len(class_name) == 4:
                        attend.lecture_type = 0
                    elif len(class_name) == 5:
                        attend.lecture_type = 1
                    elif len(class_name) == 6:
                        attend.lecture_type = 2
                    if i in arr:
                        attend.status = 'P'
                    else:
                        attend.status = 'A'
                    attend.save()
                return redirect('/home/dashboard')
            else:
                result = request.COOKIES.get('result')
                result = ast.literal_eval(result)
                return render(request, 'home/take_attendance.html', {'class': class_name, 'subject': lecture, 'role': request.COOKIES.get('role'), 'result': result['name'], 'student': stu})
        else:
            if request.method == 'POST':
                stu = Student.objects.all()
                stun = []
                length = len(request.POST['class'])
                class_name = request.POST['class']
                print(length)
                lecture = request.POST['subject']
                print(lecture)
                if length == 4:
                    sem = class_name[0]
                    branch = class_name[1:length - 1]
                    batch = class_name[length - 1]
                    stu = Student.objects.filter(semester=sem, branch=branch, batch=batch)
                    for i in stu:
                        stun.append(i.roll_number)
                elif length == 5:
                    sem = class_name[0]
                    print(sem)
                    branch = class_name[1:length - 2]
                    print(branch)
                    batch = class_name[length - 2:]
                    print(batch)
                    stu = Student.objects.filter(semester=sem, branch=branch, lab_batch=batch)
                    for i in stu:
                        stun.append(i.roll_number)
                elif length == 6:
                    sem = class_name[0]
                    branch = class_name[1:length - 3]
                    cl = class_name[length - 3]
                    batch = class_name[length - 2:]
                    stu = Student.objects.filter(semester=sem, branch=branch, batch=cl, tut_batch=batch)
                    for i in stu:
                        stun.append(i.roll_number)
                arr = smart_attendance()
                print(arr)
                for i in stun:
                    attend = att()
                    attend.lecture = lecture
                    attend.prof_username = request.COOKIES.get('result')
                    attend.prof_username = ast.literal_eval(attend.prof_username)
                    attend.prof_username = attend.prof_username['name']
                    attend.roll_number = i
                    if len(class_name) == 4:
                        attend.lecture_type = 0
                    elif len(class_name) == 5:
                        attend.lecture_type = 1
                    elif len(class_name) == 6:
                        attend.lecture_type = 2
                    if i in arr:
                        attend.status = 'P'
                    else:
                        attend.status = 'A'
                    attend.save()
                return redirect('/home/dashboard')
            else:
                result = request.COOKIES.get('result')
                result = ast.literal_eval(result)
                return render(request, 'home/take_attendance.html', {'class': class_name, 'subject': lecture, 'role': request.COOKIES.get('role'), 'result': result['name'], 'student': stu})
    else:
        return redirect('/login/')


def modify_attendance(request):
    global role, result, username, login, dat, cname, subject, lec_type
    role = request.COOKIES.get('role')
    if request.COOKIES.get('result') != "":
        if request.method == 'POST':
            if 'cname' in request.POST:
                cname = request.POST['cname']
                subject = request.POST['subject']
                dat = request.POST['date']
                stu = att.objects.all()
                stun = []
                length = len(cname)
                if length == 4:
                    lec_type = 0
                    stu = att.objects.filter(date=dat, lecture=subject, lecture_type=lec_type, status='A')
                    for i in stu:
                        stun.append(i.roll_number)
                elif length == 5:
                    lec_type = 1
                    stu = att.objects.filter(date=dat, lecture=subject, lecture_type=lec_type, status='A')
                    for i in stu:
                        stun.append(i.roll_number)
                elif length == 6:
                    lec_type = 2
                    stu = att.objects.filter(date=dat, lecture=subject, lecture_type=lec_type, status='A')
                    for i in stu:
                        stun.append(i.roll_number)
                result = request.COOKIES.get('result')
                result = ast.literal_eval(result)
                return render(request, 'home/modify_attendance.html', {'student': stu, 'role': role, 'result': result['name']})
            elif'submit_2' in request.POST:
                arr = request.POST.getlist('roll')
                for i in arr:
                    attend = att.objects.get(date=dat, lecture=subject, lecture_type=lec_type, status='A', roll_number=i)
                    attend.status = 'P'
                    attend.save()
                return redirect('/home/dashboard/')
        else:
            result = request.COOKIES.get('result')
            result = ast.literal_eval(result)
            return render(request, 'home/modify_attendance.html', {'role': role, 'result': result['name']})
    else:
        return redirect('/login/')


def view_attendance(request):
    global role, result, username, login
    typ = 0
    rol = ''
    at = []
    sear_sub = ''
    role = request.COOKIES.get('role')
    if request.COOKIES.get('result') != "":
        if request.method == 'POST':
            sear_sub = request.POST['search_sub']
            lt = request.POST['ltype']
            result = request.COOKIES.get('result')
            result = ast.literal_eval(result)
            rol = result['roll_number']
            if lt == 'lecture':
                typ = 0
            elif lt == 'lab':
                typ = 1
            else:
                typ = 2
            at = att.objects.filter(lecture=sear_sub, lecture_type=typ, roll_number=rol)
            result = request.COOKIES.get('result')
            result = ast.literal_eval(result)
            return render(request, 'home/view_attendance.html', {'role': role, 'result': result['name'], 'search_set': at})
        else:
            result = request.COOKIES.get('result')
            result = ast.literal_eval(result)
            return render(request, 'home/view_attendance.html', {'role': role, 'result': result['name'], 'search_set': at})
    else:
        return redirect('/login/')


def generate_report(request):
    global role, result, username, login, timetable, sub, pern, colorn, perl, pert, avg, colora, colorl, colorn, colort, lec, tut, lab, all
    if request.method == 'GET':
        result = request.COOKIES.get('result')
        result = ast.literal_eval(result)
        branch = request.COOKIES.get('branch')
        curr_month = datetime.datetime.now().month
        response = render(request, 'home/generate_report.html', {'result': result['name'], 'role': role, 'branch': branch, 'currentMonth': curr_month})
        return response
    else:
        wb = xlwt.Workbook()

        sheet1 = wb.add_sheet('Group B')
        sheet2 = wb.add_sheet('Group C')
        sheet3 = wb.add_sheet('Group D')

        # font: bold on; align: wrap on, vert centre, horiz center

        style_obj = xlwt.Style.easyxf("font: bold on; align: wrap on, vert centre, horiz center")

        sheet1.write(0, 0, 'Student Name', style_obj)
        sheet1.write(0, 1, 'Subject', style_obj)
        sheet1.write(0, 2, 'Lecture Attendance', style_obj)
        sheet1.write(0, 3, 'Lab Attendance', style_obj)
        sheet1.write(0, 4, 'Tutorial Attendance', style_obj)
        sheet1.write(0, 5, 'Average Attendance', style_obj)

        sheet2.write(0, 0, 'Student Name', style_obj)
        sheet2.write(0, 1, 'Subject', style_obj)
        sheet2.write(0, 2, 'Lecture Attendance', style_obj)
        sheet2.write(0, 3, 'Lab Attendance', style_obj)
        sheet2.write(0, 4, 'Tutorial Attendance', style_obj)
        sheet2.write(0, 5, 'Average Attendance', style_obj)

        sheet3.write(0, 0, 'Student Name', style_obj)
        sheet3.write(0, 1, 'Subject', style_obj)
        sheet3.write(0, 2, 'Lecture Attendance', style_obj)
        sheet3.write(0, 3, 'Lab Attendance', style_obj)
        sheet3.write(0, 4, 'Tutorial Attendance', style_obj)
        sheet3.write(0, 5, 'Average Attendance', style_obj)

        sem = request.POST['semester']
        sem = int(sem)
        branch = request.COOKIES.get('branch')
        result = Student.objects.filter(semester=sem, branch=branch)
        row1 = [1]
        row2 = [1]
        row3 = [1]
        for student in result:
            final_attendance = calculate_attendance(student.username)
            min_avg = min(final_attendance['percentagea'])
            if 75 <= min_avg < 85:
                write_in_sheet(sheet1, row1, student.name, final_attendance, style_obj)
            elif 65 <= min_avg < 75:
                write_in_sheet(sheet2, row2, student.name, final_attendance, style_obj)
            elif min_avg < 65:
                write_in_sheet(sheet3, row3, student.name, final_attendance, style_obj)
        wb.save(branch + "-" + str(sem) + '.xlsx')
        wb.save(branch + "-" + str(sem) + '.ods')
        return redirect('/home/generate_report')


def write_in_sheet(sheet, row, student_name, final_attendance, style=None):
    sheet.write(row[0], 0, student_name, style)
    for sub_name in final_attendance['subsa']:
        sheet.write(row[0], 1, sub_name)
        ind_n = index(final_attendance['subsn'], sub_name)
        if ind_n != -1:
            sheet.write(row[0], 2, final_attendance['percentagen'][ind_n])
        ind_l = index(final_attendance['subsl'], sub_name)
        if ind_l != -1:
            sheet.write(row[0], 3, final_attendance['percentagel'][ind_l])
        ind_t = index(final_attendance['subst'], sub_name)
        if ind_t != -1:
            sheet.write(row[0], 4, final_attendance['percentaget'][ind_t])
        ind_a = index(final_attendance['subsa'], sub_name)
        sheet.write(row[0], 5, final_attendance['percentagea'][ind_a])
        row[0] += 1


def signout(request):
    global login
    login = 0
    response = redirect('/login/')
    response.delete_cookie('username')
    response.delete_cookie('result')
    response.delete_cookie('role')
    if 'branch' in request.COOKIES.keys():
        response.delete_cookie('branch')
    if 'dict' in request.COOKIES.keys():
        response.delete_cookie('dict')
    if 'tt' in request.COOKIES.keys():
        response.delete_cookie('tt')
    return response
