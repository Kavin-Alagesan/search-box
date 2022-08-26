from rest_framework import generics
from api.models import Blogmodel,SearchModel
from api.serializers import BlogSerializer,SearchSerializer

class BlogListCreateAPI(generics.ListCreateAPIView):
    queryset=Blogmodel.objects.all()
    serializer_class=BlogSerializer

class BlogListViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blogmodel.objects.all()
    serializer_class=BlogSerializer

class SearchListCreateAPI(generics.ListCreateAPIView):
    queryset=SearchModel.objects.all()
    serializer_class=SearchSerializer
