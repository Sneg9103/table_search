from django.urls import path
from .views import DatabaseCredentialsView, DatabaseSchemaView, TableSearchView

urlpatterns = [
    path('database-credentials/', DatabaseCredentialsView.as_view(), name='database-credentials'),
    path('database-schema/<str:db_name>/', DatabaseSchemaView.as_view(), name='database-schema'),
    path('table-search/<str:db_name>/<str:table_name>/', TableSearchView.as_view(), name='table-search'),
]
