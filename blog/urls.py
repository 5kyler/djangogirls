from django.urls import path
from . import views
#
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]


#post/<int:pk>/ url 패턴을 의미
#post/ 는 url이 post 문자를 포함해야한다는것을 말함
#<int:pk>는 장고는 정수값을 기대하고 이를 pk라는 변수로 뷰로 전송하는것
#/은 다음에 /가 한번 더 와야 한다는 의미
