

from django.urls import path
from college import views
urlpatterns = [
    
    path('genarate-college/',views.college_names_view,name='college'),


    path('',views.home,name='home'),

    path('all-colleges-display',views.College_display_data,name='allcolleges'),

    path('VSU-college/',views.vsu_view,name='vsu'),

    path('YVU-college/',views.yvu_view,name='yvu'),

    path('SVU-college/',views.svu_view,name='svu'),

    path('Maharasta-college/',views.mhu_view,name='mhu'),

    path('Delhi-college/',views.du_view,name='du'),
  

]
