# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers
from models import Profile
        

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'attach_file_src',
            )
        depth = 1
        read_only_fields = ('id',)
    
    def __init__(self, *args, **kwargs):
        super(ProfileSerializer, self).__init__(*args, **kwargs)