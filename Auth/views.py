from rest_framework import viewsets,mixins
from Auth.serializers import AuthSerializer, JwtTokenSerializerPair
from rest_framework.response import Response
from rest_framework import  status
from rest_framework.views import APIView
from .models import CustomUserModel
from rest_framework_simplejwt.views import TokenObtainPairView,TokenVerifyView
# Create your views here.
class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = AuthSerializer
    queryset = CustomUserModel.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "message": "User successfully registered"
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "error",
            "message": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
class LoginViewSet(TokenObtainPairView):
    serializer_class = JwtTokenSerializerPair
    queryset = CustomUserModel.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "message": "User successfully registered"
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "error",
            "message": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
class NotFoundViewSet(APIView):
    def get(self,request):
        return Response({
                "status":"error",
                "message":"not found"
            },status=status.HTTP_404_NOT_FOUND)
    def post(self,request):
        return Response({
                "status":"error",
                "message":"nothing found here"
            },status=status.HTTP_404_NOT_FOUND)