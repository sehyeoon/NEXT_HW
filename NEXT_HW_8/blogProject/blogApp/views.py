from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.
def list(request):
        # Get counts for each category
    hobby_articles_count = Article.objects.filter(category='취미').count()
    food_articles_count = Article.objects.filter(category='음식').count()
    programming_articles_count = Article.objects.filter(category='프로그래밍').count()

    # Debugging messages
    print("Hobby Articles Count:", hobby_articles_count)
    print("Food Articles Count:", food_articles_count)
    print("Programming Articles Count:", programming_articles_count)

    # Fetch all articles
    articles = Article.objects.all()

    # Pass the counts and articles to the template
    return render(request, 'list.html', {
        'articles': articles,
        'hobby_articles_count': hobby_articles_count,
        'food_articles_count': food_articles_count,
        'programming_articles_count': programming_articles_count,
    })


def new(request):
    if request.method == 'POST':
        
        print(request.POST)
        
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('list')
    
    return render(request, 'new.html')

def detail(request, article_id):
    article = Article.objects.get(id = article_id)
    return render(request, 'detail.html', {'article': article})


    
def category(request, category_name):
    articles = Article.objects.filter(category=category_name)
    context = {
        'category_name': category_name,
        'articles': articles
    }
    return render(request, 'category.html', context)

def new_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # 폼에서 전송된 데이터를 저장하고 해당 글의 카테고리에 따라 적절한 카테고리 페이지로 리디렉션합니다.
            new_article = form.save()
            return redirect('category', category_name=new_article.category)
    else:
        form = ArticleForm()
    return render(request, 'new_article.html', {'form': form})