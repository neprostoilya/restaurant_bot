from django.urls import path
from .views import GetTablesAPIView, UpdateTableStatusAPIView


app_name = 'Tables'

urlpatterns = [
    path('get_tables/', GetTablesAPIView.as_view()),
    path('update_table/<table_id>/', UpdateTableStatusAPIView.as_view()),
]