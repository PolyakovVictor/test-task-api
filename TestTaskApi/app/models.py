from django.db import models


# Team model representing a team with a name field
class Team(models.Model):
    name = models.CharField(max_length=100)


# Member model representing an individual team member with name and email fields
class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()


# Membership model representing the membership relationship between a team and member
class Membership(models.Model):
    team = models.ForeignKey(Team, related_name='memberships', on_delete=models.CASCADE)
    member = models.ForeignKey(Member, related_name='memberships', on_delete=models.CASCADE)
