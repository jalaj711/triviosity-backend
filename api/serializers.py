from rest_framework import serializers
from .models import Question, User, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    current_genre = GenreSerializer()
    class Meta:
        model = Question
        fields = "__all__"
class UserSerializer(serializers.ModelSerializer):
    current_genre = GenreSerializer()
    class Meta:
        model = User
        fields = ("username", "current_round_overall", "current_genre_round", "points", "first_name", "last_name", "current_genre", "picture")

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "current_round_overall", "current_genre_round", "points", "first_name", "last_name", "current_genre", "picture")
