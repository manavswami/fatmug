
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(GenericAPIView):
    def post(self,request):
        try:
            username=request.data.get("username")
            password=request.data.get("password")
            if username==None  or password==None :
                return Response({"Error": " 'username' and 'password' both the field should be non empty  field"}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.get(username=username, password=password)
            # returing the token 
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({"data":{"msg":"user created successfully","token":access_token}}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"Error": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
 