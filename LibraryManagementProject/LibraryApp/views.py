from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from LibraryApp.models import Course, Student, Issue_Book, Books


# Create your views here.
def loging_fun(request):
    return render(request, "login.html", {'data': ""})


def logdata_fun(request):
    if request.method == 'POST':
        UserName = request.POST['txtUserName']
        Password = request.POST['txtPassword']
        user1 = authenticate(username=UserName, password=Password)
        if user1 is not None:
            if user1.is_superuser:
                login(request, user1)
                request.session['name'] = request.POST['txtUserName']
                return redirect('ahome')

            else:
                return render(request, "login.html", {'data': 'USer is not a superuser'})
        elif Student.objects.filter(Q(StudentName=UserName) & Q(Password=Password)).exists():
            request.session['S_name'] = UserName
            return render(request, "stuhome.html", {'studata': request.session['S_name']})
        else:
            return render(request, "login.html", {'data': 'Enter proper user name and password'})
    else:
        return render(request, 'login.html', {'data': ''})


def stuhome_fun(request):
    return render(request, 'stuhome.html')


def adminhome_fun(request):
    return render(request, 'adminhome.html')


def student_fun(request):
    course = Course.objects.all()
    return render(request, 'Student.html', {'Course_Data': course})


def studata_fun(request):
    s1 = Student()
    s1.StudentName = request.POST['txtStudentName']
    s1.Phno = request.POST['txtPhno']
    s1.Semester = request.POST['txtSemester']
    s1.Password = request.POST['txtPassword']
    s1.course = Course.objects.get(course_name=request.POST['ddlCourse'])
    s1.save()
    return redirect('log')


def admin_fun(request):
    return render(request, 'ADMIN.html', {'data': ''})


def admindata_fun(request):
    adminName = request.POST['txtAdminName']
    Email = request.POST['txtEmail']
    Password = request.POST['txtPassword']
    if User.objects.filter(Q(username=adminName) | Q(email=Email)).exists():
        return render(request, "ADMIN.html", {'data': 'USerName and Email is already exists'})

    else:
        u1 = User.objects.create_superuser(username=adminName, email=Email, password=Password)
        u1.save()
        return redirect('log')


def book_fun(request):
    course = Course.objects.all()
    return render(request, 'AddBook.html', {'Course_Data': course})


def addbook_fun(request):
    b1 = Books()
    b1.BookName = request.POST['txtBookName']
    b1.AuthorName = request.POST['txtAuthor']
    b1.Course_id = Course.objects.get(course_name=request.POST['ddlCourse'])
    b1.save()
    return redirect('add')


def display_fun(request):
    b1 = Books.objects.all()
    return render(request, 'display.html', {'data': b1})


def update_fun(request, id):
    b1 = Books.objects.get(id=id)
    course = Course.objects.all()

    if request.method == 'POST':
        b1.BookName = request.POST['txtBookName']
        b1.AuthorName = request.POST['txtAuthorName']
        b1.Course_id = Course.objects.get(course_name=request.POST['ddlCourse'])
        b1.save()
        return redirect('display')

    return render(request, 'update.html', {'data': b1, 'Course_Data': course})


def delete_fun(request, id):
    b1 = Books.objects.get(id=id)
    b1.delete()
    return redirect('display')


def assign_fun(request):
    course = Course.objects.all()
    return render(request, "assignbook.html", {'course': course, 'student': '', 'book': ''})


def assignread_fun(request):
    stu = Student.objects.filter(Q(Semester=request.POST['txtsam']) & Q(Course_id=Course.objects.get(course_name=request.POST['ddlcourse'])))
    book = Books.objects.filter(Course_id=Course.objects.get(course_name=request.POST['ddlcourse']))
    return render(request, "assignbook.html", {'student': stu, 'book': book})


def issue_fun(request):
    a1 = Issue_Book.objects.all()
    return render(request, 'issuebook.html', {'ddata': a1})


def issueread_fun(request):
    a1 = Issue_Book()
    a1.Student_Name = Student.objects.get(StudentName=request.POST['ddlstuname'])
    a1.BookName = Books.objects.get(BookName=request.POST['ddlbname'])
    a1.start_date = request.POST['sdate']
    a1.end_date = request.POST['edate']
    a1.save()
    return redirect('issue')


def issup_fun(request, id):
    a1 = Issue_Book.objects.get(id=id)
    s1 = Student.objects.get(id=a1.Student_Name_id)
    B1 = Books.objects.filter(Course_id=s1.Course_id)
    if request.method == 'POST':
        a1.Student_Name = Student.objects.get(StudentName=request.POST['textname'])
        a1.BookName = Books.objects.get(BookName=request.POST['txtbook'])
        a1.start_date = request.POST['txtstart_date']
        a1.end_date = request.POST['txtend_date']
        a1.save()
        return redirect('issue')
    return render(request, 'issueupdate.html', {'issue': a1, 'book': B1})


def issdel_fun(request, id):
    a1 = Issue_Book.objects.get(id=id)
    a1.delete()
    return redirect('issue')


def log_out_fun(request):
    return redirect('log')


def issuedetails_fun(request):
    a1 = Issue_Book.objects.filter(Student_Name=Student.objects.get(StudentName=request.session['S_name']))
    return render(request, 'issuedetails.html', {'ddata': a1})


def profile_fun(request):
    s1 = Student.objects.get(StudentName=request.session['S_name'])
    return render(request, 'profile.html', {'data': s1})


def updateprof_fun(request, id):
    s1 = Student.objects.get(id=id)
    if request.method == 'POST':
        s1.StudentName = request.POST['txtStuName']
        s1.Phno = request.POST['txtStuPhno']
        s1.Semester = request.POST['txtStuSem']
        s1.Password = request.POST['txtStuPassword']
        s1.save()
        return redirect('profile')
    return render(request, 'update_prof.html', {'data': s1})
