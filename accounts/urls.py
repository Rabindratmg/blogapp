from django.urls import path,include
from . import views
from .views import login_view,logout_view,signup_view

urlpatterns = [
    # path("",views.post,name="posts")
    path("login/",login_view, name="login"),
    path("dashboard/",views.dashboard, name="dashboard"),
    path("logout/",logout_view, name="logout"),
    path("signup/",signup_view, name="signup"),
    path("profile/",views.profile, name="profile"),
    path('editprofile/<int:id>', views.editprofile, name= "editprofile"),
]

