from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.homepage, name="home-page"),
    path("home/", views.home, name="home"),
    path("freelancer/<str:pk>/", views.freelancer, name="freelancer"),
    path("signup/", views.signup, name="signup"),
    path("level/", views.level, name="level"),
    path("login/", views.login, name="login"),
    #path("loginasuser", views.loginasfreelancer, name = "loginasuser"),
    path("loginasemployer", views.loginasemployer, name = "loginasemployer"),
    path("logout/", views.logout, name="logout"),
    path("send-message/", views.send_message , name="send-message"),
    path('post_job/', views.post_job, name="post-job"),
    path('submit-proposal/', views.apply_job, name = "submit-proposal"),
    path('update-job/<str:pk>/', views.update_job, name = "update-job"),
    path('delete-job/<str:pk>', views.delete_job, name = "delete-job"),
]