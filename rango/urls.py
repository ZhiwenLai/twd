from django.urls import path, re_path, include
from rango import views


app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page,name='add_page'),
    path('category/<slug:category_name_slug>/', views.show_category,name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),

    # Regular expressions match different dog information interfaces through ID
    re_path('^doginfo/(?P<dog_id>\d+)/',views.dog_info,name = 'doginfo'),
    re_path('clt_note/',views.clt_note,name = 'clt'),
    # add comment
    path('add_comment/', views.addComment, name='add_comment'),

    # search result
    path('search/', views.search, name='search'),

    # my account
    path('userinfo/',views.userInfo,name='userinfo'),

    # classification of dogs
    path('bigdog/',views.bigDog,name='bigdog'),
    path('smalldog/',views.smallDog,name='smalldog'),
    path('mediumdog/',views.mediumDog,name='mediumdog'),


]