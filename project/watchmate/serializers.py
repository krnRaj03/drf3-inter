from rest_framework.serializers import ModelSerializer
from .models import StreamingPlatform, WatchList



class WatchListSerializer(ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"
        # exclude = ("active",)


class StreamingPlatformSerializer(ModelSerializer):
    class Meta:
        model = StreamingPlatform
        fields = "__all__"
