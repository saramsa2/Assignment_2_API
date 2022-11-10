"""Assignment_2_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from attendance.views import index, semester_list, class_list, course_list, SemesterViewSet

router = DefaultRouter()
router.register('semester_viewset', SemesterViewSet, 'semester_model_viewset')
urlpatterns = router.urls
urlpatterns.append(path('', index))
urlpatterns.append(path('semester/', semester_list))
# urlpatterns.append(path('course/', course_list))
# urlpatterns.append(path('class/', class_list))

# urlpatterns = [
#     path('', index),
#     path('semester/', semester_list),
#     path('course/', course_list),
#     path('class/', class_list),
# ]
