from rest_framework import serializers
from .models import Comment, Good, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class GoodSerializer(serializers.ModelSerializer):
    # comments = CommentSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Good
        fields = '__all__'
        # fields = ['name', 'category', 'description', 'price', 'stock_availability']
