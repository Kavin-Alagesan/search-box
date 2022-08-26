from rest_framework import serializers
from .models import Blogmodel,SearchModel

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blogmodel
        fields='__all__'
class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model=SearchModel
        fields='__all__'
