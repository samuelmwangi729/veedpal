from rest_framework import serializers
from Auth.models import CustomUserModel as User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class JwtTokenSerializerPair(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['role'] = user.role
        return token
class AuthSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,default=0)  # input only
    class Meta:
        model = User

        fields=[
            'username','email','first_name','last_name','password'
            ]

    def validate(self,attrs):
        #check if the username exists
        username = attrs.get('username')
        email = attrs.get('email')
        user = User.objects.filter(username=username)
        if user.exists():
            raise serializers.ValidationError({
                "status":"error",
                "message":"the username is already taken. Choose a different one"
                })
        userExists = User.objects.filter(email=email)
        if userExists.exists():
            raise serializers.ValidationError({
                "status":"error",
                "message":"the email is already taken. Choose a different one"
                })
        return attrs
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
        