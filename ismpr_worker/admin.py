from django.contrib import admin
from .models import WorkerStatus, Worker


@admin.register(WorkerStatus)
class WorkerStatusAdmin(admin.ModelAdmin):
    list_display = ['id','status']
    list_editable = ['status']


@admin.register(Worker)
class WorkerStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'Phone', 'workerStatus', 'Company']
    list_editable = ['Phone', 'workerStatus', 'Company']