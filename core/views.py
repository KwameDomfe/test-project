from django.shortcuts import render
from apps.articles.models import Article
import random
# Create your views here.
def Index(request):
    
    random_id = random.randint (1,2)
    article_Object = Article.objects.get(id = random_id)
    my_list = [102, 23, 654,45,457]
    article_qs = Article.objects.all()
    
    context = {
        'article' :article_Object,
        'my_list' : my_list,
        'articles' :article_qs,
    }
    
    return render(
        request, 
        'index.html', 
        context
    )