from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)


class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()


class Membership(models.Model):
    team = models.ForeignKey(Team, related_name='memberships', on_delete=models.CASCADE)
    member = models.ForeignKey(Member, related_name='memberships', on_delete=models.CASCADE)
