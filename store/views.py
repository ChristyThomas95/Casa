from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Design

# Create your views here.


def store(request):
    designs = Design.objects.order_by('-created_at')
    paginator = Paginator(designs, 4)
    page = request.GET.get('page')
    paged_designs = paginator.get_page(page)
    
    model_search = Design.objects.values_list('model', flat=True).distinct()
    city_search = Design.objects.values_list('city', flat=True).distinct()
    floors_search = Design.objects.values_list('floors', flat=True).distinct()
    
    context ={
        'designs': paged_designs,
        'model_search':model_search,
        'city_search':city_search,
        'floors_search':floors_search,
        
    }
    return render(request, 'store/store.html',context)


def design_detail(request, id):
    single_design = get_object_or_404(Design, pk=id)
    
    context = {
        'single_design': single_design,
    }
     
    return render(request, 'store/design_detail.html',context)


def search(request):
    designs = Design.objects.order_by('-created_at')
    
     
    model_search = Design.objects.values_list('model', flat=True).distinct()
    city_search = Design.objects.values_list('city', flat=True).distinct()
    floors_search = Design.objects.values_list('floors', flat=True).distinct()
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            designs = designs.filter(description__icontains=keyword)
    
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            designs = designs.filter(model__icontains=model)  
            
    if 'city' in request.GET:
        model = request.GET['city']
        if city:
            city = designs.filter(city__icontains=city)   
            
    if 'flooors' in request.GET:
        model = request.GET['floors']
        if floors:
            floors= designs.filter(floors__icontains=floors)                  
                  
    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            designs.filter(price__gte=min_price, price__lte=max_price)
    
    
    
    context = {
        'designs': designs,
        'model_search':model_search,
        'city_search':city_search,
        'floors_search':floors_search,
    }
    return render(request, 'store/search.html',context)