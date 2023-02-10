from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.course_name}"

class Books(models.Model):
    BookName = models.CharField(max_length=50)
    AuthorName = models.CharField(max_length=50)
    Course_id = models.ForeignKey(Course,on_delete=models.CASCADE)


    def __str__(self):
         return f"{self.BookName}"


class Student(models.Model):
    StudentName = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Phno = models.BigIntegerField()
    Semester = models.IntegerField()
    Course_id = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
         return f"{self.StudentName}"

class Issue_Book(models.Model):

    Student_Name = models.ForeignKey( Student,on_delete=models.CASCADE)
    BookName = models.ForeignKey(Books, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
