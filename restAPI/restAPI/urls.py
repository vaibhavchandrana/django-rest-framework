
from django.contrib import admin
from django.urls import path
from api.views import Student_detail,getAllDetails,insertData

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_detail/<int:pk>', Student_detail),
    path('all_student_detail/', getAllDetails),
    path('insert_data/', insertData),
]
