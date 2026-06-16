
from ..models import Product


def get_filtered_products(search_query=None, category_id=None, tag_id_list=None):
    """
    Filter products based on search query, category, and tags selected.

    Args:
        search_query (str, optional): Text search query submitted by user to match against product description.
        category_id (str | int, optional): DB primary key for selected category.
        tag_id_list (list[str] | list[int], optional): List of DB primary keys for selected tags. Query only returns products that have all selected tags.

    Returns:
        Queryset containing filtered products matching every criteria.
    """

    product_result = Product.objects.all()

    if search_query:
        search_words = search_query.split()

        for word in search_words:
            product_result = product_result.filter(description__icontains=word)

    if category_id:
        product_result = product_result.filter(category_id=category_id)

    # Assumes products must contain ALL selected tags
    if tag_id_list:
        for tag_id in tag_id_list:
            product_result = product_result.filter(tags__id=tag_id)
    
    return product_result.distinct()