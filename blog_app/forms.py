from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name','name')
print(choices)
choice_list = []
for choice in choices:
	choice_list.append(choice)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'author', 'category','body', 'introduction')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.Select(attrs={'class': 'form-control'}),
			'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
			'introduction': forms.Textarea(attrs={'class': 'form-control'})
		}

class UpdateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'category', 'body', 'introduction')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),	
			'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),		
			'body': forms.Textarea(attrs={'class': 'form-control'}),
			'introduction': forms.Textarea(attrs={'class': 'form-control'})
		}

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ('name',)

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
		}