from rest_framework.serializers import ModelSerializer
from .models import Advocate

class advocate_serializer(ModelSerializer):
 
     class Meta:
          model=Advocate
          fields=['id','username',"bio"]

     

