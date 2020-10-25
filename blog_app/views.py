from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, UpdateForm, CategoryForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from ckeditor.widgets import CKEditorWidget
# Create your views here.

# def home(request):
# 	return render(request, 'home.html', {})

from django.shortcuts import redirect

def redirect_view(request):
	obj = Post.objects.last()
	response = redirect('post/'+str(obj.id))
	return response

class HomeView(ListView):
	model = Post
	template_name = 'home.html'	
	ordering = ["-post_date"]

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class PostDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'
	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(PostDetailView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	# def get_context_data(self, *args, **kwargs):
	# 	cat_menu = Category.objects.all()
	# 	context = super(AddPostView, self).get_context_data(*args, **kwargs)
	# 	context["cat_menu"] = cat_menu
	# 	return context
	
	# fields = '__all__'

class UpdatePostView(UpdateView):
	model = Post
	# fields = ['body', 'title', 'title_tag', 'author']
	form_class = UpdateForm
	template_name = 'update_post.html'
	# def get_context_data(self, *args, **kwargs):
	# 	cat_menu = Category.objects.all()
	# 	context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
	# 	context["cat_menu"] = cat_menu
		# return context

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy("home")
	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(DeletePostView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class AddCategoryView(CreateView):
	model = Category
	form_class = CategoryForm
	template_name = 'add_category.html'
	success_url = reverse_lazy("home")	
	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

def CategoryView(request, cats):
	cats = cats.replace("-", " ")
	category_posts = Post.objects.filter(category=cats)
	return render(request, 'categories.html', {"cats":cats.title(), 'category_posts': category_posts})


def CategoryListView(request):
	cat_menu_list = Category.objects.all()
	return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list })
