from rest_framework import serializers
from .models import Member, Membership, Team


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('__all__')


class TeamSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ('__all__')


class MembershipSerializer(serializers.ModelSerializer):
    team = TeamSerializer()
    member = MemberSerializer()

    class Meta:
        model = Membership
        fields = ('id', 'team', 'member')
