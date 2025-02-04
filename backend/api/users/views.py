from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializers import LoginUserSeraializer, UserSerializer,RegisterUserSerializer
from rest_framework.generics import RetrieveUpdateAPIView
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class UserInfosView(RetrieveUpdateAPIView):
    permission_classes=(IsAuthenticated),
    serializer_class=UserSerializer
    
    def get_object(self):
        return self.request.user
class UserRegistrationView(CreateAPIView):
    serializer_class=RegisterUserSerializer

class LoginUserView(APIView):
    def post(self,request):
        serializer=LoginUserSeraializer(data=request.data)
    #    generating token for ours users
        if serializer.is_valid():
            user=serializer.validated_data
            refrech=RefreshToken(user)
            access_token = str(refrech.access_token)
            response =Response({
                "user":UserSerializer(user).data},status=status.HTTP_200_OK)
            response.set_cookie(key="access_token",
                                value=access_token,
                                httponly=True,
                                secure=True,
                                samesite='Strict')
            response.set_cookie(key="refresh_token",
                                value=str(refrech),
                                httponly=True,
                                secure=True,
                                samesite='Strict')
            return response
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class LogoutUserView(APIView):
    def post(self,request):
        refrech_token=request.COOKIES.get('refresh_token')
        if refrech_token :
                refrech = RefreshToken(refrech_token)      