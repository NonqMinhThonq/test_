from django.urls import path
from .views import CreateAccountView, GetAllAccountsView, GetAccountView, UpdateAccountView, DeleteAccountView

urlpatterns = [
    path('accounts/create/', CreateAccountView.as_view(), name='create-account'),
    path('accounts/get/', GetAllAccountsView.as_view(), name='get-all-accounts'),
    path('accounts/get/<int:pk>/', GetAccountView.as_view(), name='get-account'),
    path('accounts/update/<int:pk>/', UpdateAccountView.as_view(), name='update-account'),
    path('accounts/delete/<int:pk>/', DeleteAccountView.as_view(), name='delete-account'),
]
