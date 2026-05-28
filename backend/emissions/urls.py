from django.urls import path

from .views import (
    records,
    upload_sap,
    upload_utility,
    sync_travel,
    approve_record
)

urlpatterns = [
    path('records/', records),

    path('upload/sap/', upload_sap),

    path('upload/utility/', upload_utility),

    path('travel/sync/', sync_travel),

    path('approve/<int:pk>/', approve_record),
]