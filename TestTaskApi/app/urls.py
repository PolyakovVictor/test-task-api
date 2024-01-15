from django.urls import path
from . import views


app_name = 'api'

urlpatterns = [
    path('teams/', views.TeamView.as_view(), name='team-list'),
    path('teams/<int:pk>/', views.TeamView.as_view(), name='team-detail'),
    path('members/', views.MemberView.as_view(), name='member-list'),
    path('members/<int:pk>/', views.MemberView.as_view(), name='member-detail'),
    path('memberships/', views.MembershipView.as_view(), name='membership-list'),
    path('memberships/<int:team_id>/<int:member_id>/', views.MembershipView.as_view(), name='membership-detail'),
    path('single-team-with-members/<int:pk>/', views.SingleTeamWithMembersView.as_view(), name='single-team-with-members'),
    path('all-teams-with-members/', views.AllTeamsWithMembersView.as_view(), name='all-teams-with-members'),
]
