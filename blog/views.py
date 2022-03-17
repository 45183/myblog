from django.shortcuts import render, get_object_or_404

from blog.models import Post


def index(request):
    # 포스트 목록
    post_list = Post.objects.all()
    context = {'post_list':post_list}
    return render(request, 'blog/post_list.html', context)

def detail(request, post_id):
    # 상세 페이지
    post = get_object_or_404(Post, pk=post_id)
    # post = Post.objects.get(id=post_id)             # 포스트 1개 가져오기
    context = {'post':post}
    return render(request, 'blog/post_detail.html', context)
