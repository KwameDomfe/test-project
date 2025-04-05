from django.shortcuts import render

# Create your views here.
def Info_Index(request):
    
    obj = ['Tree', 5, 'box']
    
    context = {
        'object' :obj 
    }
    
    return render(
        request, 
        'info/index.html', 
        context
    )

def About(request):
    
    obj = ['Tree', 5, 'box'];
    obj1 = 'Sokode';
    obj2 = 5;
    
    context = {
        'object' :obj,
        'object1' :obj1,
        'object2' :obj2,
    }
    
    return render(
        request, 
        'info/about.html', 
        context
    ) 