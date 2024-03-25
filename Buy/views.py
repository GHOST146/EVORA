from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Property
from Homepage.forms import PropertySearchFormBuy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import locale
import random


def Buy(request):
    if request.method == "POST":  # Check if the form is submitted
        form = PropertySearchFormBuy(request.POST, request.FILES)
        if form.is_valid() and 'search-btn' in request.POST:
            filter_params = form.cleaned_data.copy()
            if filter_params['search_text'] == "":
               filter_params['search_text'] = "None"
            return redirect('Buy',**filter_params)
    else:
        form = PropertySearchFormBuy()

    # Create a base queryset
    queryset = Property.objects.all()

    queryset = queryset.order_by('price')

    # Apply filters based on GET parameters

    for obj in queryset:
        if obj.size != 0:
            obj.price_per_unit = round(obj.price / obj.size,2)
        else:
            obj.price_per_unit = None  # Handle division by zero gracefully
    

    paginator = Paginator(queryset, 10)  # Display 10 objects per page
    page_number = request.GET.get('page')

    try:
        objects_list = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects_list = paginator.page(paginator.num_pages)

    context = {
        'objects_list': objects_list,
        'form': form,
    }

    return render(request, 'Buy2/Buy.html', context)

def BuyRequest(request,search_text,property_type,min_price,max_price,bedrooms):
    if request.method == "POST":  # Check if the form is submitted
        form = PropertySearchFormBuy(request.POST, request.FILES)
        if form.is_valid() and 'search-btn' in request.POST:
            filter_params = form.cleaned_data.copy()
            if filter_params['search_text'] == "":
               filter_params['search_text'] = "None"
            return redirect('Buy',**filter_params)
    else: 
        if search_text == "None":
            search_text = ""
        form = PropertySearchFormBuy(initial={'search_text' : search_text, 'property_type' : property_type, 'min_price' : min_price, 'max_price': max_price, 'bedrooms' : bedrooms})

    # Create a base queryset
    queryset = Property.objects.all()

    # Apply filters based on GET parameters
    if search_text and search_text != 'None':
        queryset = queryset.filter(state__icontains=search_text)
    if property_type and property_type != 'All':
        queryset = queryset.filter(residence_type=property_type)
    if min_price and min_price != '0':
        queryset = queryset.filter(price__gte=min_price)
    if max_price and max_price != '0':
        queryset = queryset.filter(price__lte=max_price)
    if bedrooms and bedrooms != '0' and bedrooms != 5:
        queryset = queryset.filter(number_of_bedrooms=bedrooms)
    elif bedrooms == 5:
        queryset = queryset.filter(number_of_bedrooms__gte=bedrooms)

    # Apply ordering
    queryset = queryset.order_by('price')

    for obj in queryset:
        if obj.size != 0:
            obj.price_per_unit = round(obj.price / obj.size,2)
        else:
            obj.price_per_unit = None  # Handle division by zero gracefully
    


    paginator = Paginator(queryset, 10)  # Display 10 objects per page
    page_number = request.GET.get('page')

    try:
        objects_list = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects_list = paginator.page(paginator.num_pages)\
        
    context = {
        'objects_list': objects_list,
        'form': form,
    }

    return render(request, 'Buy2/Buy.html', context)