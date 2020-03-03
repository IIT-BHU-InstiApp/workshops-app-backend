from datetime import date
from rest_framework import serializers
from .models import UserProfile, Club, Council, Workshop

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'email', 'phone_number', 'photo_url')


class ClubSerializer(serializers.ModelSerializer):
    # TODO : Add Subscribed Users here
    class Meta:
        model = Club
        fields = ('id', 'name', 'council', 'small_image_url', 'large_image_url')


class CouncilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Council
        fields = ('id', 'name', 'small_image_url', 'large_image_url')


class WorkshopSerializer(serializers.ModelSerializer):
    club = ClubSerializer(read_only=True)
    # TODO : Add Number of attendees here, and subscribed
    class Meta:
        model = Workshop
        fields = ('id', 'club', 'title', 'date', 'time',)


class ClubDetailSerializer(serializers.ModelSerializer):
    council = CouncilSerializer()
    secy = serializers.SerializerMethodField()
    joint_secy = serializers.SerializerMethodField()
    active_workshops = serializers.SerializerMethodField()
    past_workshops = serializers.SerializerMethodField()
    # TODO : Subscribed users, and whether subscribed or not

    def get_secy(self, obj):
        """
        Get the the value of secy field
        """
        serializer = UserProfileSerializer(obj.secy)
        return serializer.data

    def get_joint_secy(self, obj):
        """
        Get the the value of joint_secy field
        """
        serializer = UserProfileSerializer(obj.joint_secy, many=True)
        return serializer.data

    def get_active_workshops(self, obj):
        """
        Get the the value of active workshops field
        """
        # pylint: disable=no-member
        queryset = Workshop.objects.filter(
            club=obj, date__gte=date.today()).order_by('date', 'time')
        serializer = WorkshopSerializer(queryset, many=True)
        return serializer.data

    def get_past_workshops(self, obj):
        """
        Get the the value of past_workshops field
        """
        # pylint: disable=no-member
        queryset = Workshop.objects.filter(
            club=obj, date__lt=date.today()).order_by('-date', '-time')
        serializer = WorkshopSerializer(queryset, many=True)
        return serializer.data

    class Meta:
        model = Council
        fields = ('id', 'name', 'description', 'council',
                  'secy', 'joint_secy', 'active_workshops', 'past_workshops', 'small_image_url', 'large_image_url')


class CouncilDetailSerializer(serializers.ModelSerializer):
    secy = serializers.SerializerMethodField()
    joint_secy = serializers.SerializerMethodField()
    clubs = serializers.SerializerMethodField()

    def get_secy(self, obj):
        """
        Get the the value of secy field
        """
        serializer = UserProfileSerializer(obj.secy)
        return serializer.data

    def get_joint_secy(self, obj):
        """
        Get the the value of joint_secy field
        """
        serializer = UserProfileSerializer(obj.joint_secy, many=True)
        return serializer.data

    def get_clubs(self, obj):
        """
        Get the the value of clubs field
        """
        serializer = ClubSerializer(obj.clubs, many=True)
        return serializer.data

    class Meta:
        model = Council
        fields = ('id', 'name', 'description', 'secy', 'joint_secy', 'clubs', 'small_image_url', 'large_image_url')


class WorkshopCreateSerializer(serializers.ModelSerializer):
    def validate_club(self, club):
        """
        Validate the club field
        """
        request = self.context['request']
        # pylint: disable=no-member
        profile = UserProfile.objects.get(user=request.user)
        if club not in profile.club_secy.all() and club not in profile.club_joint_secy.all():
            raise serializers.ValidationError(
                "You are not authorized to create workshops for this club")
        return club

    def validate_contacts(self, contacts):
        """
        Validate the contacts field
        """
        request = self.context['request']
        # pylint: disable=no-member
        profile = UserProfile.objects.filter(user=request.user)
        if not profile:
            raise serializers.ValidationError("User does not exist")
        return contacts

    class Meta:
        model = Workshop
        fields = (
            'id', 'title', 'description', 'club', 'date', 'time',
            'location', 'audience', 'resources', 'contacts', 'image_url')


class WorkshopDetailSerializer(serializers.ModelSerializer):
    club = ClubSerializer(read_only=True)
    contacts = UserProfileSerializer(many=True, read_only=True)
    # TODO : Add number of attendees here and subscribed

    class Meta:
        model = Workshop
        fields = (
            'id', 'title', 'description', 'club', 'date', 'time',
            'location', 'audience', 'resources', 'contacts', 'image_url')
