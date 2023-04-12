from studentvue import StudentVue
import time as time


def studentcreate(x, y):
    # os.system('clear')
    sv = StudentVue(x, y, 'https://parent.spotsylvania.k12.va.us/PXP2_Login_Student.aspx?regenerateSessionId=True')
    # CGS Check
    return sv


def CGSCheck(x):
    try:
        n = x.get_schedule()
        n = list(n.items())
        n = n[0][1]
        n = list(n.items())
        n = n[4][1]
        n = list(n.items())
        n = n[1][1]
        n = list(n.items())
        n = list(n[0])
        n = list(n[1][0].items())
        n = (n[0][1])
        return n == 'Commonwealth Governors School'
    except (IndexError, ValueError, KeyError):
        return False


def name(x):
    info = x.get_student_info()
    moreinfo = info['StudentInfo']
    mminfo = moreinfo['FormattedName']
    name = mminfo['$']
    return name


def second_block(sv):
    cgs = CGSCheck(sv)
    if cgs:
        sched = sv.get_schedule(1)
        msched = sched['StudentClassSchedule']
        bsched = msched['TodayScheduleInfoData']['SchoolInfos']['SchoolInfo']
        n = list(bsched[1].items())
        m = list(n[2])
        o = list(m[1].items())
        o = o[0][1][1]
        p = list(o.items())
        return p[7][1]
    else:
        # 2nd NON CGS
        sched = sv.get_schedule(1)
        msched = sched['StudentClassSchedule']
        bsched = msched['TodayScheduleInfoData']['SchoolInfos']['SchoolInfo']
        bsched = list(bsched.items())
        n = list(bsched[2][1].items())
        n = (n[0][1][1])
        m = list(n.items())
        m = m[7][1]
        return m


def first_block(sv):
    cgs = CGSCheck(sv)
    if cgs:
        sched = sv.get_schedule(1)
        msched = sched['StudentClassSchedule']
        bsched = msched['TodayScheduleInfoData']['SchoolInfos']['SchoolInfo']
        n = list(bsched[1].items())
        m = list(n[2])
        o = list(m[1].items())
        p = list(o[0][1][0].items())
        return p[7][1]
    else:
        # FIRST NON CGS
        sched = sv.get_schedule(1)
        msched = sched['StudentClassSchedule']
        bsched = msched['TodayScheduleInfoData']['SchoolInfos']['SchoolInfo']
        bsched = list(bsched.items())
        n = list(bsched[2][1].items())
        n = (n[0][1][0])
        m = list(n.items())
        m = m[7][1]
        return m


def third_block(sv):
    cgs = CGSCheck(sv)
    if cgs:
        sched = sv.get_schedule(1)
        msched = sched['StudentClassSchedule']
        bsched = msched['TodayScheduleInfoData']['SchoolInfos']['SchoolInfo']
        n = list(bsched[1].items())
        m = list(n[2])
        o = list(m[1].items())
        p = list(o[0][1][2].items())
        return p[7][1]
    else:
        # THIRD NON CGS
        sched = sv.get_schedule(1)
        msched = sched['StudentClassSchedule']
        bsched = msched['TodayScheduleInfoData']['SchoolInfos']['SchoolInfo']
        bsched = list(bsched.items())
        n = list(bsched[2][1].items())
        n = (n[0][1][2])
        m = list(n.items())
        m = m[7][1]
        return m


def fourth_block(sv):
    cgs = CGSCheck(sv)
    if cgs:
        sched = sv.get_schedule(1)
        msched = sched['StudentClassSchedule']
        bsched = msched['TodayScheduleInfoData']['SchoolInfos']['SchoolInfo']
        n = list(bsched[1].items())
        m = list(n[2])
        o = list(m[1].items())
        p = list(o[0][1][3].items())
        return p[7][1]
    else:
        # FOURTH NON CGS
        sched = sv.get_schedule(1)
        msched = sched['StudentClassSchedule']
        bsched = msched['TodayScheduleInfoData']['SchoolInfos']['SchoolInfo']
        bsched = list(bsched.items())
        n = list(bsched[2][1].items())
        n = (n[0][1][3])
        m = list(n.items())
        m = m[7][1]
        return m


def gender(sv):
    info = sv.get_student_info()
    moreinfo = info['StudentInfo']
    mminfo = moreinfo['Gender']
    gender = mminfo['$']
    return gender


def hour():
    obj = time.localtime()
    hour1 = int(obj[3])
    return hour1


def min():
    obj = time.localtime()
    min1 = int(obj[4])  # change this
    return min1


def determineBlock():
    if hour() == 7:
        if min() >= 45:
            return 1
        else:
            return -1
    elif hour() == 8:
        if min() <= 45:
            return 1
        else:
            return -1
    elif hour() == 9:
        if min() >= 10:
            return 2
        else:
            return -1
    elif hour() == 10:
        if min() <= 10:
            return 2
        else:
            return -1
    elif hour() == 11:
        if min() >= 15:
            return 3
        else:
            return -1
    elif hour() == 12:
        if min() <= 45:
            return 3
        else:
            return -1
    elif hour() == 13:
        if min() >= 10:
            return 4
        else:
            return -1
    elif hour() == 14:
        if min() <= 10:
            return 4
        else:
            return -1
    else:
        return -1


def whatRoom(sv):
    if (determineBlock() == 1):
        return first_block(sv)
    elif (determineBlock() == 2):
        return second_block(sv)
    elif (determineBlock() == 3):
        return third_block(sv)
    elif (determineBlock() == 4):
        return fourth_block(sv)
    elif (determineBlock() == -1):
        return -1


def whatBathroom(room, x):
    if gender(x) == 'Male':
        if 100 < room < 132:  # Change The Numbers
            return 1
        if 134 < room < 166:  # Change The Numbers
            return 2
        if 200 < room < 232:  # Change The Numbers
            return 3
        if 234 < room < 264:  # Change The Numbers
            return 4
        else:
            return -1
    elif gender(x) == 'Female':
        if 100 < room < 132:  # Change The Numbers
            return 5
        if 134 < room < 136:  # Change The Numbers
            return 6
        if 200 < room < 232:  # Change The Numbers
            return 7
        if 234 < room < 264:  # Change The Numbers
            return 8
        else:
            return -1


def printB(x):
    if x == 1:
        return "Men's English"
    if x == 2:
        return "Men's History"
    if x == 3:
        return "Men's Language"
    if x == 4:
        return "Men's Math"
    if x == 5:
        return "Women's English"
    if x == 6:
        return "Women's History"
    if x == 7:
        return "Women's Language"
    if x == 8:
        return "Women's Math"
    if x == 9:
        return 'whatever bathroom you want'
    if x == -1:
        return "Cannot Sign in Right Now"


def bathr(x, y):
    student = studentcreate(x, y)
    room = whatRoom(student)
    bathroom = whatBathroom(room, student)
    return printB(bathroom)



def bathr2(x, y):
    student = studentcreate(x, y)
    room = whatRoom(student)
    bathroom = whatBathroom(room, student)
    return bathroom


