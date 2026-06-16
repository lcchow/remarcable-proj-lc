from django.shortcuts import render

from .services import product_search
from .models import Category, Tag

PRODUCT_CATALOG_TEMPLATE = 'product_catalog/index.html'

def product_catalog_view(request):
    params = request.GET
    search_query = params.get('q')
    category = params.get('category')
    tag_id_list = params.getlist('tag')

    product_result = product_search.get_filtered_products(search_query, category, tag_id_list)

    context = {
        'products': product_result,
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
        'search_query': search_query,
        'selected_category': int(category) if category else None,
        'selected_tags': [int(tag_id) for tag_id in tag_id_list]
    }

    return render(request, PRODUCT_CATALOG_TEMPLATE, context)
