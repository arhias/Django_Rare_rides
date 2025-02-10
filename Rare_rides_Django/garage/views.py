from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Car
from django.shortcuts import render
def car_list(request):
    query = request.GET.get('q', '')
    selected_brand = request.GET.get('brand', '')
    selected_year = request.GET.get('year', '')
    selected_type = request.GET.get('type', '')  
    sort_by = request.GET.get('sort', 'model')  

    all_brands = Car.objects.values_list('brand', flat=True).distinct()
    all_types = Car.objects.values_list('car_type', flat=True).distinct()  

    cars = Car.objects.all()

    if query:
        cars = cars.filter(Q(brand__icontains=query) | Q(model__icontains=query))
    if selected_brand:
        cars = cars.filter(brand=selected_brand)
    if selected_year:
        cars = cars.filter(year=selected_year)
    if selected_type:
        cars = cars.filter(car_type=selected_type)  

    if sort_by in ['model', 'year', '-year', 'price', '-price']:
        cars = cars.order_by(sort_by)

    paginator = Paginator(cars, 8)  
    page_number = request.GET.get('page')
    cars_paginated = paginator.get_page(page_number)

    return render(request, 'garage/car_list.html', {
        'cars': cars_paginated,
        'query': query,
        'selected_brand': selected_brand,
        'selected_year': selected_year,
        'selected_type': selected_type,
        'all_brands': all_brands,
        'all_types': all_types,
        'sort_by': sort_by,
    })

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'garage/car_detail.html', {'car': car})
def car_brands(request):
    all_brands = Car.objects.values_list('brand', flat=True).distinct()
    return render(request, 'garage/car_brands.html', {'all_brands': all_brands})