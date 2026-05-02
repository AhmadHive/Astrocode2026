from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('submit/', views.submission_view, name='submission'),
    path('submit/success/', views.success_view, name='success'),
    path('Team_List',views.teams_list_view,name='Team_list'),
    path("Submation_List",views.submission_list_view,name='sabmation_list'),
    path("Track_List",views.tracks_list_view,name="tracks_list"),
    path('Track_detail/<int:track_id>/', views.track_detail_view, name='track_detail'),
    path('Committee_Competitio',views.Comitee_Team,name='Committee_Competitio'),
    path('Courses',views.Courses,name='Courses'),
    path('AstroCode2025',views.AstroCode2025,name='AstroCode2025')

]