from django.urls import path
from .views import TaskView
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'tasks', TaskView, 'task')

urlpatterns = [
    path('', include(router.urls)),
]