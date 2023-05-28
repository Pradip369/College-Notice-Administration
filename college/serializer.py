from rest_framework import serializers
from college.models import Branch,Notice
from django.contrib.auth.models import User

class BranchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Branch
        # fields = ["name","age"]
        fields = "__all__"
        
class NoticeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Notice
        fields = ["subject","msg"]        
