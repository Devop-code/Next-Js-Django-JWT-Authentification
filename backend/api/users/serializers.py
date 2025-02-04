from rest_framework.serializers import ModelSerializer,Serializer
from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import authenticate
class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email','username']
        
# creation de la classe RegisterUserSerializer
class RegisterUserSerializer(ModelSerializer):
    # definition des champs du formulaire a covnertir en json 
    class Meta:
        model = CustomUser
        fields = [ 'email','username','password']
        # definition des champs a ne pas afficher
        extra_kwargs = {'password': {'write_only': True}}
    # creation de l'utilisateur
    def create(self, validated_data):
        # recuperation des champs du formulaire
        user = CustomUser.objects.create_user(**validated_data)
        return user

# creation de la classe LoginUserSeraializer
class LoginUserSeraializer(Serializer):
    # recuperation des champs email et password du formulaire 
   email = serializers.EmailField(required=True)
   password = serializers.CharField(write_only=True)
#    # validation des champs
   def validate(self, data):
    #    # recuperation des champs email et password
     user = authenticate(**data)
    #  # verification de l'existance de l'utilisateur
     if user and user.is_active:
       return user
    # si l'utilisateur n'existe pas ou n'est pas actif
   raise serializers.ValidationError('Incorrect Credentials')