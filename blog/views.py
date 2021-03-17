from django.shortcuts import render, get_object_or_404
from .models import Posts
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView
    )

# Create your views here.

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2019'
    }


]
def home(request):
    """handles traffic from the home page of our blog"""
    
    return render(request, 'blog/home.html', {'title': 'Home'}) #the user will see this when sent to this route

def about(request):
    """handles traffic from about page"""
    return render(request, 'blog/about.html', {'title': 'About'})



class PostListView(ListView):
    """creates a list of posts"""
    model = Posts
    template_name = 'blog/blog.html'# <app>/<model>_<viewtpye>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5 #number of posts per page

class UserPostListView(ListView):
    """creates a list of posts for user only"""
    model = Posts
    template_name = 'blog/user_posts.html'# <app>/<model>_<viewtpye>.html
    context_object_name = 'posts'
    #ordering = ['-date_posted']
    paginate_by = 5 #number of posts per page

    def get_queryset(self):
        #checks if user exists or not and then shows user
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Posts.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    """To see a detailed form"""
    model = Posts
   

class PostCreateView(LoginRequiredMixin, CreateView):
    """To create a new form"""
    model = Posts
    fields = ['title', 'content']

    def form_valid(self, form):
        #connects logged in user to post updates
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """To create a new form"""
    model = Posts
    fields = ['title', 'content']

    def form_valid(self, form):
        #connects logged in user to post updates
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        #avoids users updating others posts
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """To see a detailed form"""
    model = Posts
    success_url = '/' #redirect to home page when post is deleted
    def test_func(self):
        #avoids users updating others posts
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False












