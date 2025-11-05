from rest_framework.viewsets import ModelViewSet
from Auth.serializers import AuthSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import  status
from rest_framework.views import APIView
# Create your views here.
class RegisterViewSet(ModelViewSet):
    serializer_class = AuthSerializer
    queryset=None

    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "status":"success",
                "message":"user successfully registered"
            },status=status.HTTP_200_OK)
        return Response({
            "status":"error",
            "message":serializer.errors
        })
class NotFoundViewSet(APIView):
    def get(self,request):
        return Response({
                "status":"error",
                "message":"not found"
            },status=status.HTTP_404_NOT_FOUND)
    def post(self,request):
        return Response({
                "status":"error",
                "message":"not found"
            },status=status.HTTP_404_NOT_FOUND)