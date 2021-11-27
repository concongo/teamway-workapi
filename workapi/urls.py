from django.urls import path
from . import views

worker_urls = [
    path('worker/create/', views.WorkerCreateAPIView.as_view(), name='worker_create'),
    path('worker/<str:personal_id>/', views.WorkerRetrieveAPIView.as_view(), name='worker_detail'),
    path('worker/update/<str:personal_id>/', views.WorkerRetrieveUpdateAPIView, name='worker_update'),
    path('worker/delete/<str:personal_id>', views.WorkerDestroyAPIView.as_view(), name='worker_delete'),
    path('worker/', views.WorkerListAPIView.as_view(), name='worker_list'),
]

shift_urls = [
    path('shift/create/', views.ShiftCreateAPIView.as_view(), name='shift_create'),
    path('shift/<int:id>/', views.ShiftRetrieveAPIView.as_view(), name='shift_detail'),
    path('shift/update/<int:id>/', views.ShiftRetrieveUpdateAPIView, name='shift_update'),
    path('shift/delete/<int:id>', views.ShiftDestroyAPIView.as_view(), name='shift_delete'),
    path('shift/', views.ShiftListAPIView.as_view(), name='shift_list'),
]

workplan_urls = [
    path('workplan/create/', views.WorkPlannerCreateAPIView.as_view(), name='workplan_create'),
    path('workplan/<int:id>/', views.WorkPlannerRetrieveAPIView.as_view(), name='workplan_detail'),
    path('workplan/update/<int:id>/', views.WorkPlannerRetrieveUpdateAPIView.as_view(), name='workplan_update'),
    path('workplan/delete/<int:id>', views.WorkPlannerDestroyAPIView.as_view(), name='workplan_delete'),
    path('workplan/', views.WorkPlanneListAPIView.as_view(), name='workplan_list'),
]

urlpatterns = worker_urls + shift_urls + workplan_urls
