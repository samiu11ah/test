from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

posts = [
    {
        'id': 1,
        'title': 'title #1',
        'content': 'some content #1'
    },
    {
        'id': 2,
        'title': 'title #2',
        'content': 'some content #2'
    },
    {
        'id': 2,
        'title': 'title #2',
        'content': 'some content #2'
    },
]

class PostsView(APIView):


    def get(self, request):
        return Response(posts)
    
    def post(self, request):
        post = {
            'id': len(posts) + 1,
            'title': request.POST['title'],
            'content': request.POST['content']
        }
        posts.append(post)
        return Response(post)

        

class GetPost(APIView):

    def get(self, request, id):
        for post in posts:
            if post['id'] == int(id):
                return Response(post)
            else:
                return Response({'message': 'post not found'})