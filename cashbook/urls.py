from django.urls import path
from . import views

urlpatterns = [
    path('mycashbooks/', views.CashbookList.as_view(), name='my_cashbooks'),
    path('<slug:slug>', views.CashbookDetail.as_view(),
         name='cashbook_detail'),
    path('createcashbook/', views.CashbookCreate.as_view(),
         name='create_cashbook'),
]
