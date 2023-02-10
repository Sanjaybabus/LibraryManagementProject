from django.urls import path

from LibraryApp import views

urlpatterns = [
      path('', views.loging_fun, name='log'),
      path('logdata', views.logdata_fun),

      path('add',views.admin_fun,name='add'),
      path('admindata',views.admindata_fun),

      path('student', views.student_fun, name='stud'),
      path('stud', views.studata_fun),

      path('adminhome', views.adminhome_fun, name='ahome'),
      path('stuhome', views.stuhome_fun, name='shome'),

      path('addbook',views.addbook_fun),
      path('book',views.book_fun,name='book'),

      path('display', views.display_fun, name='display'),

      path('Update/<int:id>', views.update_fun, name='Update'),
      path('Delete/<int:id>', views.delete_fun, name='Delete'),


      path('assign',views.assign_fun, name='assig'),
      path('assignread',views.assignread_fun),
      path('issueread', views.issueread_fun),

      path('issue', views.issue_fun, name='issue'),
      path('issuedetails', views.issuedetails_fun, name='issuedetails'),

      path('Update/<int:id>', views.issup_fun, name='Update'),
      path('Delete/<int:id>', views.issdel_fun, name='Delete'),

      path('profile',views.profile_fun,name='profile'),
      path('updateprof/<int:id>',views.updateprof_fun,name='updateprof'),

      path('log_out', views.log_out_fun, name="log_out"),


]
