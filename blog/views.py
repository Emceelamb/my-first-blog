from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def post_list(request):
	
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	paginator = Paginator(posts, 5) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)
	return render(request, 'blog/post_list.html', {'posts': posts})    

	"""
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
	return render(request, 'blog/post_list.html', {'posts': posts})
	"""


def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	
	
	if request.method == "POST":
	    
		form = PostForm(request.POST)
	    
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('blog.views.post_detail', pk=post.pk)
		
	else:
			
		form = PostForm()
    
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def project_list(request):
	projects = Post.objects.filter
	return render(request, 'blog/project_list.html', {'projects': projects})


