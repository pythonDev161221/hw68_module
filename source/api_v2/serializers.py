

from rest_framework import serializers


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(
            required=True,
            allow_null=False,
            allow_blank=False,
            max_length=200
    )

    content = serializers.CharField(
        required=True,
        max_length=2000,
        allow_blank=False,
        allow_null=False,
    )

    author_id = serializers.CharField(
        read_only=True,
    )

