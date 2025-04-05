from django.shortcuts import redirect,   render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from .models import Recipe, RecipeIngredient
from .forms import RecipeForm, RecipeIngredientForm
# Create your views here.
# CRUD Operations


@login_required
def recipe_list_view(request):
    
    query_set = Recipe.objects.filter(user=request.user)
    context = {
        'object_list' : query_set
    }
    
    return render (
        request,
        'recipes/list.html',
        context
    )

@login_required
def recipe_detail_view(request, id=None):
    
    recipe_object = get_object_or_404(Recipe, id=id, user = request.user)
    
    context = {
        'object' : recipe_object
    }
    
    return render (
        request,
        'recipes/detail.html',
        context
    )

@login_required
def recipe_create_view(request):
    
    create_form = RecipeForm(request.POST or None)
 
    if create_form.is_valid():
        object = create_form.save(commit=False)
        object.user = request.user
        object.save()
        return redirect(object.get_absolute_url())
    
    context = {
        'form': create_form
    }
    
    return render (
        request,
        'recipes/create-update.html',
        context=context
    )

@login_required
def recipe_update_view(request, id=None):
    
    recipe_object = get_object_or_404(
                        Recipe, 
                        id = id, 
                        user = request.user
                    )
    recipe_form = RecipeForm(
                    request.POST or None, 
                    instance = recipe_object
                )
    
    RecipeIngredientFormSet = modelformset_factory(
        RecipeIngredient,
        form = RecipeIngredientForm,
        extra = 3
    )

    query_set = recipe_object.recipeingredient_set.all()
    formset = RecipeIngredientFormSet(
        request.POST or None,
        queryset=query_set
    )


    if all ([recipe_form.is_valid(), formset.is_valid()]):
        parent = recipe_form.save(commit=False)
        parent.save()
        for form in formset:
            child = form.save(commit=False)
            # if child.recipe is None:
            #     print('Added New')
            #     child.recipe = parent
            # child.save()
        
    context = {

        'form' : recipe_form,
        'formset' : formset,
        'object' : recipe_object,
        'message': 'Data saved'

    }
    
    return render (
        request,
        'recipes/create-update.html',
        context
    )


@login_required
def recipe_delete_view(request, id=None):
    
    
    context = {}
    
    return render (
        request,
        '',
        context
    )
