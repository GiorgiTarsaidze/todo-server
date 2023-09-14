from .models import Tasks
from rest_framework import viewsets, status
from .serializers import TasksSerializer
from .filters import TasksFilter 
from rest_framework.decorators import action
from rest_framework.response import Response


class TaskView(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    filterset_class = TasksFilter

    def perform_bulk_delete(self, task_ids):
        try:
            Tasks.objects.filter(id__in=task_ids, completed=True).delete()
        except Exception as e:
            raise Exception(str(e))

    @action(detail=False, methods=['delete'])
    def delete_tasks(self, request):
        try:
            task_ids = request.data.get('taskIds', [])
            task_ids = [int(task_id) for task_id in task_ids]

            self.perform_bulk_delete(task_ids)

            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)