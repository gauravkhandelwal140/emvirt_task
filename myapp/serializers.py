from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
from rest_framework import filters
from rest_framework.authtoken.models import Token

class User_serializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','first_name','username','email']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        token = Token.objects.get(user=instance)
        response['Token'] = str(token)
        return response

class User_serializers1(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','first_name','username','email']


class User_reg_serializers(serializers.Serializer):
    first_name=serializers.CharField(max_length=10,required=False)
    username=serializers.CharField(max_length=10,required=True)
    email=serializers.EmailField(required=False)
    password=serializers.CharField(max_length=25,required=True)


class DeviceSerializers(serializers.ModelSerializer):
    diskpartition=serializers.ListField(required=False)

    class Meta:
        model=Device
        # fields = '__all__'
        exclude=('user',)

    def update(self, instance, validated_data):
        print(instance.id, '-----------------------90')
        try:
            diskpartition = validated_data.pop('diskpartition', None)
            print(diskpartition)
        except:
            vehicle_image = None

        instance = super(DeviceSerializers, self).update(instance, validated_data)

        if diskpartition != None and diskpartition != '' and len(diskpartition[0]):
            img = Diskpartitioninfo.objects.filter(device=instance)
            img.delete()
            for info in diskpartition:
                eventimg = Diskpartitioninfo.objects.create(info=info,device=instance)
                eventimg.save()
        return instance

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['User'] =User_serializers1(instance.user).data
        Diskpartition =Diskpartitioninfo.objects.filter(device=instance).values_list('info',flat=True)
        response['diskpartitioninfo'] = list(Diskpartition)
        return response



class DeviceSerializers_res(serializers.ModelSerializer):
    user = User_serializers1()
    class Meta:
        model=Device
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        Diskpartition =Diskpartitioninfo.objects.filter(device=instance).values_list('info',flat=True)
        response['diskpartitioninfo'] = list(Diskpartition)
        return response


# class Profile_image(serializers.Serializer):
#     image=serializers.ImageField()
#
#
# class BookTradeManSerilizer(serializers.Serializer):
#     trademan=serializers.CharField()
#     date=serializers.DateField(format="%Y-%m-%d")


