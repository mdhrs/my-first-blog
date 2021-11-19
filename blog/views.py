from django.shortcuts import render
from django.utils import timezone  #この行を追加
from .models import Post  #この行を追加

# Create your views here.
def post_list(request):
    """下の1行を追加　Postから必要なデータを取り出して変数postsに代入している"""
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')  #この行
    """
    ●下の行の{}の中に 'posts': posts を追加する　 'posts'という名前とpostsという値をセットにしなくてはなりません
    ●requestというのはインターネット介してユーザから受け取った全ての情報が詰まったもの
    """
    return render(request, 'blog/post_list.html', {'posts': posts})  
