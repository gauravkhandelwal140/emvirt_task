from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response

from .serializers import *
# Create your views here.
def response_handler(data,message,status):
    dict={"status":status,"message":message,"data":data}
    return Response(dict)



from rest_framework.authtoken.models import Token

class Sign_up(viewsets.ViewSet):
    permission_classes = [AllowAny]
    def create(self, request):
        serializer = User_reg_serializers(data=request.data)
        if serializer.is_valid():
            first_name = serializer.validated_data.get('first_name','')
            username=serializer.validated_data.get('username','')
            email = serializer.validated_data.get('email', '')
            password = serializer.validated_data.get('password', '')
            user= User.objects.create(username=username,first_name=first_name,email=email,password=password)
            user.set_password(password)
            user.save()
            Token.objects.create(user=user)
            serilizer=User_serializers(user)
            m="User Create Successful"
            s=1003
            d = serilizer.data
            return response_handler(message=m, status=s, data=d)
        else:
            m = serializer.errors  # "Error"
            s = False
            d = {}
            return response_handler(message=m, status=s, data=d)



class Device_view(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = DeviceSerializers
    queryset = Device.objects.all()

    def create(self, request):
        serializer = DeviceSerializers(data=request.data)
        user=request.user
        if serializer.is_valid():
            diskpartition=serializer.validated_data.get('diskpartition','')
            uptime=serializer.validated_data.get('uptime','')
            memory_usage = serializer.validated_data.get('memory_usage', '')
            cpu_usage = serializer.validated_data.get('cpu_usage', '')
            device= Device.objects.create(user=user,uptime=uptime,memory_usage=memory_usage,cpu_usage=cpu_usage,)
            device.save()
            for y in diskpartition:
                d=Diskpartitioninfo.objects.create(device=device,info=y)
                d.save()

            serilizer=DeviceSerializers_res(device)
            m="Device Add Successful"
            s=True
            d = serilizer.data
            return response_handler(message=m, status=s, data=d)
        else:
            m = serializer.errors  # "Error"
            s = False
            d = {}
            return response_handler(message=m, status=s, data=d)



class Device_list(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def retrieve(self, request, pk=None):
        try:
            user_id=User.objects.get(id=pk)
        except:
            m = "User id incorrect"
            s = True
            d = {}
            return response_handler(message=m, status=s, data=d)

        device=Device.objects.filter(user=user_id)
        serilizer = DeviceSerializers_res(device,many=True)
        m = "List of all Devices"
        s = True
        d = serilizer.data
        return response_handler(message=m, status=s, data=d)

