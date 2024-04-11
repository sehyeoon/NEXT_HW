from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .models import Comment

# Create your views here.
def new(request):
    categories = Article.category_choices
    if request.method == 'POST':
        
        print(request.POST)
        
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category']
        )
        return redirect('list')
    
    return render(request, 'new.html', {'categories': categories})


def list(request):
    categories = Article.category_choices
    articles = Article.objects.all()
    categories_with_counts = []
    for category_id, category_name in categories:
        count = Article.objects.filter(category=category_id).count()
        categories_with_counts.append((category_id, category_name, count))
    return render(request, 'list.html', {'articles': articles, 'categories_with_counts': categories_with_counts})

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        parent_id = request.POST.get('parent_id')
        if parent_id:
            parent = Comment.objects.get(id=parent_id)
            Comment.objects.create(article=article, content=content, parent_id=parent_id)
        else:
            Comment.objects.create(article=article, content=content)
        return redirect('detail', article_id=article_id)
    else:
        comments = Comment.objects.filter(article=article, parent__isnull=True)
    return render(request, 'detail.html', {'article': article, 'comments': comments})

    

def category(request, category_id):
    articles = Article.objects.filter(category=category_id)
    return render(request, 'category.html', {'articles': articles})

def base(request):
    return render(request, 'base.html')


def delete_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('list')  
    return render(request, 'delete_confirm.html', {'article': article})