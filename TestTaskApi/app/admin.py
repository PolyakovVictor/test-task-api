from django.contrib import admin
from .models import Member, Team, Membership


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('team', 'member',)
    search_fields = ('team__name', 'member__first_name', 'member__last_name',)
