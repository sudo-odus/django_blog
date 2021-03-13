from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
#from django.http import HttpResponse

def home(request):
	context={
	'key':Post.objects.all() #ab mza aaya na bheedu ab ye pass krdia asli data database se tgda h system babu ji
	}
	return render(request,'blog/home.html',context)


#a replacement of def home 
class PostListView(ListView):
	model = Post
	context_object_name='posts'
	template_name='blog/home.html'
	ordering=['-date_posted']
	paginate_by=2

class UserPostListView(ListView):
	model = Post
	context_object_name='posts'
	template_name='blog/user_posts.html'
	#ordering=['-date_posted']
	paginate_by=3

	def get_queryset(self):
		 user=get_object_or_404(User,username=self.kwargs.get('username'))
		 return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model=Post
	context_object_name='post'


class PostCreateView(LoginRequiredMixin,CreateView):
	model=Post
	
	fields=['title','content']
	#form.instance.author=self.request.user  #because self here is not defined that is why we hace to use that function I guess
	

	#What it returns is the result of the superclass implementation of the method,
	# which happens to be a redirect to the success URL
	def form_valid(self,form):   #overiding the form valid method of Create View
		form.instance.author=self.request.user
		return super().form_valid(form)  #this line is running form valid method on the parent class
										#which would have run anyway mtlb ki whi inbuilt hai smjhe
	#success_url='post/self.pk'


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model=Post
	
	fields=['title','content']
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
# Create your views here.
def about(request):
	return render(request,'blog/about.html')


	