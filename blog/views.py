# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from django.core.paginator import Paginator
# from .models import BlogPost, Comment, Category
# from .forms import BlogPostForm, CommentForm

# def blog_list(request):
#     posts = BlogPost.objects.all()
#     paginator = Paginator(posts, 5)  # 5 posts per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'blog/blog_list.html', {'page_obj': page_obj})

# def blog_detail(request, pk):
#     post = get_object_or_404(BlogPost, pk=pk)
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.post = post
#             comment.author = request.user
#             comment.save()
#             return redirect('blog_detail', pk=pk)
#     else:
#         comment_form = CommentForm()
#     return render(request, 'blog/blog_detail.html', {'post': post, 'comment_form': comment_form})

# @login_required
# def blog_create(request):
#     if request.method == 'POST':
#         form = BlogPostForm(request.POST)
#         if form.is_valid():
#             blog_post = form.save(commit=False)
#             blog_post.author = request.user
#             blog_post.save()
#             form.save_m2m()
#             return redirect('blog_list')
#     else:
#         form = BlogPostForm()
#     return render(request, 'blog/blog_form.html', {'form': form})

# @login_required
# def blog_edit(request, pk):
#     post = get_object_or_404(BlogPost, pk=pk)
#     if post.author != request.user:
#         return redirect('blog_detail', pk=pk)
#     if request.method == 'POST':
#         form = BlogPostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('blog_detail', pk=pk)
#     else:
#         form = BlogPostForm(instance=post)
#     return render(request, 'blog/blog_form.html', {'form': form})

# @login_required
# def blog_delete(request, pk):
#     post = get_object_or_404(BlogPost, pk=pk)
#     if post.author != request.user:
#         return redirect('blog_detail', pk=pk)
#     post.delete()
#     return redirect('blog_list')


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import BlogPost, Comment, Category
from .forms import BlogPostForm, CommentForm

def blog_list(request):
    posts = BlogPost.objects.all()
    paginator = Paginator(posts, 5)  # 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/blog_list.html', {'page_obj': page_obj})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog_detail', pk=pk)
    else:
        comment_form = CommentForm()
    return render(request, 'blog/blog_detail.html', {'post': post, 'comment_form': comment_form})

@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            form.save_m2m()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/blog_form.html', {'form': form})

@login_required
def blog_edit(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if post.author != request.user:
        return redirect('blog_detail', pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', pk=pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/blog_form.html', {'form': form})

@login_required
def blog_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if post.author != request.user:
        return redirect('blog_detail', pk=pk)
    post.delete()
    return redirect('blog_list')
