from django.urls import path
from .views import text_transform_view,delete_history,detail_history

urlpatterns = [
    path('', text_transform_view,name='text_transform'),
    path('detail/<int:id>/', detail_history,name='detail'),
    path('delete/<int:id>/', delete_history,name='delete'),
]
