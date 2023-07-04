from rest_framework import serializers
from .models import *


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'track_number', 'track_title']
        read_only_fields = ['album']



class AlbumSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    tracks = TrackSerializer(many=True, read_only=True)

    def get_tracks(self, instance):
        return instance.tracks.all()

    class Meta:
        model = Album
        fields = ['id', 'artist', 'title', 'released_at', 'description', 'tracks']
