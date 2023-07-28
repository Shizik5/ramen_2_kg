from django.shortcuts import render
from rest_framework import generics, permissions
from comment.serializers import CommentSerializer
from comment.models import Comment
from comment.tasks import send_new_comment_email

# Create your views here.


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        comment = serializer.save(owner=self.request.user)
        send_new_comment_email.delay(comment.id)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return permissions.AllowAny(),
        return permissions.IsAuthenticated(),  # For retrieving and updating comments
