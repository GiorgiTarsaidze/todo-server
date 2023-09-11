from .models import Tasks
from rest_framework import viewsets
from .serializers import TasksSerializer
from .filters import TasksFilter 

class TaskView(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    filterset_class = TasksFilter

