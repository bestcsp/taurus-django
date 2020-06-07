from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView
                                    )

from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request,'blog/home.html')

class PostListView(ListView):
    model=Post
    template_name='blog/Post_list.html' #foldername/model_view_type
    context_object_name='posts'  
    ordering=['-date']
    paginate_by = 4
    def get_queryset(self):
        return Post.objects.filter(approved=True)
"""
class PostDetailView(DetailView):
    model=Post  
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        #post=
        post=Post.objects.filter(id=self.kwargs.get['pk'])
        #print("post value",post)
        
        context['comments']=Comment.objects.filter(post=post)
        return context
"""
def detail(request,pk):
    posts=Post.objects.filter(id=pk).first()
    comments=Comment.objects.filter(post=posts)
    print("comments",comments)
    context={'posts':posts,'comments':comments}
    return render(request,'blog/detailpage.html',context)  

    


class UserPostListView(ListView):
    model=Post
    template_name='blog/Userpost.html'   #<app>/<model>_<viewtype>.html
    context_object_name='posts'
    #ordering=['-date']
    paginate_by = 4

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user,approved=True).order_by('-date')

    
    
        


class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content','pic']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content','pic']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'
    
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

def comment(request):
    content=request.POST['content']
    postid=request.POST.get('comment_id')
    post=Post.objects.get(id=postid)
    user=request.user
    c=Comment(user=user,post=post,content=content)
    c.save()
    return redirect('detail',pk=post.id)





def about(request):
    return render(request,'blog/intro.html')

def promotion(request):
    return render(request,'blog/promotionpage.html')

