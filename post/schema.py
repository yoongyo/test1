import graphene
from graphene_django.types import DjangoObjectType
from .models import Post, Comments, File


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class CommentsType(DjangoObjectType):
    class Meta:
        model = Comments


class FileType(DjangoObjectType):
    class Meta:
        model = File


class Query(object):
    all_posts = graphene.List(PostType)
    all_comments = graphene.List(CommentsType)
    all_files = graphene.List(FileType)

    def resolve_all_posts(self, info, **kwargs):
        return Post.objects.all()

    def resolve_all_comments(self, info, **kwargs):
        return Comments.objects.all()

    def resolve_all_files(self, infor, **kwargs):
        return File.objects.all()
