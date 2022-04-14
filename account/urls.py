from django.urls import path

from account.views import(
    AccountView,
    EditAccountView,
    crop_image
)

app_name = 'account'

urlpatterns = [
    path('<user_id>/', AccountView, name='view'),
    path('<user_id>/edit/', EditAccountView, name='edit'),
    path('<user_id>/edit/cropImage', crop_image, name='crop_image'),
]