from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post

# Create your views here.
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts':posts,
#         }
#     )

class PostList(ListView): #얘는 그냥 post_list 변수를 받는다 
    model = Post #post_list 변수 models.py에 있는 post
    # template_name = 'blog/post_list.html' 템플릿 이름 바꾸기
    ordering = '-pk'
    paginate_by=5
    template_name = 'blog/post_list.html'
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#
#         request,
#         'blog/single_post_detail.html',
#         {
#             'post':post,
#         }
#     )

class PostDetail(DetailView): #=> post_detail.html 자동으로 찾아준다.
    model = Post
#    template_name = 'blog/single_post_detail.html'
