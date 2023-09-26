from django.urls import path    
from website.views import *

app_name = 'website'

urlpatterns = [
    path('',index , name='index'),
    path('certification',full_stack , name='fullstack'),
    path('certification_python',python , name='python'),
    path('certification_mcsa',mcsa , name='mcsa'),
    path('certification_mcitp',mcitp , name='mcitp'),
    path('<int:pid>',single, name='single'),
]