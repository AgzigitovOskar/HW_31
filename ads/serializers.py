from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ads.models import Ad, Category, Selection
from ads.validators import not_null
from users.models import User
from users.serializers import UserSerializer, UserLocationSerializer


class AdSerializer(serializers.ModelSerializer):
    is_published = serializers.BooleanField(validators=[not_null], required=False)

    class Meta:
        model = Ad
        fields = '__all__'


class AdListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", queryset=Category.objects.all())
    author = UserLocationSerializer()

    class Meta:
        model = Ad
        fields = ['name', 'price', 'author', 'category']


class AdDetailSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    category = serializers.SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = '__all__'


class SelectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionCreateSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all(), required=False)

    def create(self, validated_data):
        request = self.context.get("request")
        if "owner" not in validated_data:
            validated_data["owner"] = request.user
        elif "owner" in validated_data and request.user.role not in ["moderator", "admin"]:
            raise ValidationError("Нет доступа")
        return super().create(validated_data)

    class Meta:
        model = Selection
        fields = '__all__'

