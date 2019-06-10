from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('lists', views.lists, name='lists'),
    # path('new_board', views.add_board, name='new_board'),
    path('new_board', views.BookCreateView.as_view(), name='new_board'),
    path('board/<int:board_id>', views.board, name="board"),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('create_list/<int:board_id>', views.ListCreate.as_view(), name='new_list'),

]
