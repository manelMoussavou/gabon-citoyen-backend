from django.urls import path
from .views import (
    DeputyListView, DeputyDetailView, get_user_deputy,
    DeputyActivityListView, CitizenMessageCreateView, CitizenMessageListView
)

urlpatterns = [
    path('', DeputyListView.as_view(), name='deputy-list'),
    path('<int:pk>/', DeputyDetailView.as_view(), name='deputy-detail'),
    path('my-deputy/', get_user_deputy, name='my-deputy'),
    path('<int:deputy_id>/activities/', DeputyActivityListView.as_view(), name='deputy-activities'),
    path('<int:deputy_id>/messages/', CitizenMessageListView.as_view(), name='deputy-messages'),
    path('messages/create/', CitizenMessageCreateView.as_view(), name='create-message'),
]
