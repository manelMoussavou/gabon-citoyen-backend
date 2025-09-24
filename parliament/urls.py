from django.urls import path
from .views import (
    BillListView, BillDetailView, ActiveBillsView, RecentBillsView,
    VoteListView, ParliamentSessionListView, ParliamentaryDocumentListView
)

urlpatterns = [
    path('bills/', BillListView.as_view(), name='bill-list'),
    path('bills/<int:pk>/', BillDetailView.as_view(), name='bill-detail'),
    path('bills/active/', ActiveBillsView.as_view(), name='active-bills'),
    path('bills/recent/', RecentBillsView.as_view(), name='recent-bills'),
    path('votes/', VoteListView.as_view(), name='vote-list'),
    path('sessions/', ParliamentSessionListView.as_view(), name='session-list'),
    path('documents/', ParliamentaryDocumentListView.as_view(), name='document-list'),
]
