from django.urls import path
from django.views.generic import TemplateView
from .views import index, feedbackView,user_login, signup, user_logout, login_success, profile_view
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', index.as_view(), name='index'),
    path('feedback/', feedbackView.as_view(), name='feedback'),
    path('feedback/index/', index.as_view(), name='index'),
    path('signup/', signup, name='signup'),
    path('signup/account/', login_success , name='signup_success'),
    path('login/', user_login, name='login'),
    path('login/account/', login_success , name='login_success'),
    path('account/', profile_view.as_view() , name='account'),
    #path('login/account/', profile_view.as_view() , name='account'),
    #path('login/account/', login_success , name='login_success'),
    #path('account/', user_logout, name='logout'),
    #path('account/login', user_login, name='login'),
]