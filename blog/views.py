from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


def home(request):
    search_query = request.GET.get('q', '').strip()
    category_filter = request.GET.get('category', '').strip()

    posts = Post.objects.all().order_by('-created_at')

    if search_query:
        posts = posts.filter(title__icontains=search_query)

    valid_categories = dict(Post.CATEGORY_CHOICES)

    if category_filter in valid_categories:
        posts = posts.filter(category=category_filter)
    else:
        category_filter = ''

    context = {
        'posts': posts,
        'search_query': search_query,
        'categories': Post.CATEGORY_CHOICES,
        'selected_category': category_filter,
    }

    return render(request, 'blog/home.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {
        'form': form,
        'page_title': 'Create a New Post',
    })
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {
        'form': form,
        'page_title': 'Edit Blog Post',
    })
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'blog/post_confirm_delete.html', {
        'post': post,
    })