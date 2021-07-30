from rest_framework import serializers
from .models import Album, Review


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    Reviews = serializers.HyperlinkedRelatedField(
        view_name="review_detail", many=True, read_only=True
    )
    album_url = serializers.ModelSerializer.serializer_url_field(
        view_name="album_detail"
    )

    class Meta:
        model = Album
        fields = ("id", "title", "artist_name", "release_year", "reviews")


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    album = serializers.HyperlinkedRelatedField(
        view_name="album_detail", read_only=True
    )
    album_id = serializers.PrimaryKeyRelatedField(
        queryset=Album.objects.all(), source="album"
    )

    class Meta:
        model = Review
        fields = (
            "album",
            "author",
            "body",
        )
