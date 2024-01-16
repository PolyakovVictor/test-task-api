# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Team, Member, Membership
from .serializers import TeamSerializer, MemberSerializer, MembershipSerializer


# CRUD for teams
class TeamView(APIView):
    serializer_class = TeamSerializer

    def get(self, request, *args, **kwargs):
        queryset = Team.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            team = Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            return Response({"error": "Team not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            team = Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            return Response({"error": "Team not found"}, status=status.HTTP_404_NOT_FOUND)

        team_name = team.name
        team.delete()
        return Response({"message": f"Team '{team_name}' was successfully deleted"}, status=status.HTTP_204_NO_CONTENT)


# CRUD for members
class MemberView(APIView):
    serializer_class = MemberSerializer

    def get(self, request, *args, **kwargs):
        queryset = Member.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            member = Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            return Response({"error": "Member not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            member = Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            return Response({"error": "Member not found"}, status=status.HTTP_404_NOT_FOUND)

        member_name = member.first_name
        member.delete()
        return Response({"message": f"Member '{member_name}' was successfully deleted"}, status=status.HTTP_204_NO_CONTENT)


# view adds a member to a team by team id and member id, and removes a member from the team
class MembershipView(APIView):
    def post(self, request):
        team_id = request.data.get('team_id')
        member_ids = request.data.get('member_ids', [])

        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"error": "Team not found"}, status=status.HTTP_404_NOT_FOUND)

        members = Member.objects.filter(pk__in=member_ids)
        memberships = []

        for member in members:
            membership, created = Membership.objects.get_or_create(team=team, member=member)
            memberships.append(membership.id)

        return Response({"memberships": memberships}, status=status.HTTP_201_CREATED)

    def delete(self, request, team_id, member_id):
        try:
            team = Team.objects.get(pk=team_id)
            member = Member.objects.get(pk=member_id)
        except (Team.DoesNotExist, Member.DoesNotExist):
            return Response({"error": "Team or Member not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            membership = Membership.objects.get(team=team, member=member)
        except Membership.DoesNotExist:
            return Response({"error": "Membership not found"}, status=status.HTTP_404_NOT_FOUND)

        team_name = team.name
        member_name = f"{member.first_name} {member.last_name}"

        membership.delete()

        return Response({"message": f"{member_name} was removed from the group {team_name}"}, status=status.HTTP_204_NO_CONTENT)


# returns all teams with their members
class AllTeamsWithMembersView(APIView):
    def get(self, request):
        memberships = Membership.objects.select_related('team', 'member').all()
        serializer = MembershipSerializer(memberships, many=True)
        return Response(serializer.data)


# class that returns a team with its members
class SingleTeamWithMembersView(APIView):
    def get(self, request, pk):
        team = Team.objects.get(id=pk)
        memberships = team.memberships.all()
        members = []

        for membership in memberships:
            members.append(membership.member)

        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)
