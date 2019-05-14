from rest_framework import serializers
from .models import Category, Sections, Product, Basket
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        # {'name': 'new category 3'}
        # name='new category 3'
        category = Category(**validated_data)
        category.save()
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class CategorySerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'created_by',)
        # fields = '__all__'


class SectionsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    category = CategorySerializer2(read_only=True)

    class Meta:
        model = Sections
        fields = ('id', 'name', 'category',)
        # fields = '__all__'


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    # img = serializers.CharField(required=False)
    name = serializers.CharField(required=True)
    price = serializers.FloatField()
    description = serializers.CharField()
    status = serializers.CharField()
    sections = SectionsSerializer()

    class Meta:
        model = Product
        fields = ('id', 'img', 'name', 'description', 'price', 'status', 'sections')


class BasketSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    product = ProductSerializer()
    count = serializers.IntegerField()

    class Meta:
        model = Basket
        fields = ('id', 'product', 'count')
