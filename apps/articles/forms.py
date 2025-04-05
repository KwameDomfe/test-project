from django import forms 

from .models import Article


class ArticleForm (forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'slug', 'contents','published']  

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        query_set = Article.objects.filter(title__icontains=title)

        if query_set.exists():
            self.add_error('title', f'\"{title}" is already in use. Please pick another title' )
        return data
    
class ArticleFormO(forms.Form):
    title = forms.CharField()
    contents = forms.CharField()