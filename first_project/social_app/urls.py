from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('signup/', sign_up, name='sign_up' ),
    path('signin/', sign_in, name='sign_in'),
    path('signout/', sign_out, name='sign_out'),
    path('profile_settings/', profile_settings, name='profile_settings'),
    path('add_post/', add_post, name='add_post'),
    path('like_post/<int:post_id>/', like_post, name='like_post'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    # path('block_user/<int:user_id>/', views.block_user, name='block_user'),
    # path('make_admin/<int:user_id>/', views.make_admin, name='make_admin')
]
