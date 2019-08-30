from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, redirect
from django. contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, UserProfile, Comment, User

class PostListView(ListView):
    model = Post
    template_name = 'home.html'

    def get_queryset(self):
        return Post.objects.all().order_by('-posted')

class PostDetailView(DetailView):
    model=Post
    template_name='popup_view.html' 

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model=Post
    template_name='get_update.html'
    fields=['description','post']
  
    def get_success_url(self, *args, **kwargs):
        return reverse('runaway:detail', args=(self.object.pk,))

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model=Post
    template_name='get_delete.html'
    success_url=reverse_lazy('runaway:home')

class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    template_name='get_create.html'
    fields=['location', 'lng', 'lat', 'description', 'post']
    
    def form_valid(self, form):
        form.instance.username=self.request.user
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self, *args, **kwargs):
        return reverse('profiles:post_list', args=(self.object.username,))

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model=Comment
    template_name='get_update.html'
    fields=['text']
 
    def get_success_url(self, *args, **kwargs):
        return reverse('runaway:detail', args=(self.object.post.pk,))
        
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model=Comment
    template_name='get_delete.html'
    
    def get_success_url(self, *args, **kwargs):
        return reverse('runaway:detail', args=(self.object.post.pk,))

class CommentView(LoginRequiredMixin, CreateView):
    model=Comment
    template_name='add_comment.html'
    fields=['text']

    def form_valid(self, form):
        form.instance.author=self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['pk'])
        form.save()
        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse('runaway:detail', args=(self.kwargs['pk'],))
    