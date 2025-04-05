from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from .models import Article

from .forms import ArticleForm

# Create your views here.
def articles_index(request):
    
    articles_object = Article.objects.all()
    
    context = {
        'articles_object' :articles_object,
        
    }
    
    return render(
        request, 
        'articles/index.html', 
        context
    )

def article_detail(request, article_slug=None):
    
    article_object = None
    
    if article_slug is not None:
        
        try:
            article_object = Article.objects.get(slug=article_slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_object = Article.objects.filter(slug=article_slug).first()
        except:
            raise Http404
            
    context = {
        'articleObject' :article_object,
    }
    
    return render(
        request, 
        'articles/detail.html', 
        context
    )

def articles_search(request): 
    query= request.GET.get('query') 
        
    query_set = Article.objects.search(query=query)

    context = {
        # 'object' : article_object,
        'object_list' : query_set
    }
    
    return render(
        request, 
        'articles/search.html', 
        context
    )

@login_required
def article_create(request): 
    
    articleForm = ArticleForm(request.POST or None)

    context = {
        'form' : articleForm
    }
    
    if  articleForm.is_valid():
        article_object = articleForm.save()
        context['object'] = article_object
        context ['created'] = True
        # return redirect('articles:article-detail', article_slug = article_object.slug)
        return redirect(article_object.get_absolute_url()) 
    print(context)
    return render(
        request, 
        'articles/create.html', 
        context
    ) 
 