from django.test import TestCase
from .models import Category, Tag, Product
from .services import product_search

class ProductSearchTestCase(TestCase):

    def setUp(self):
        self.fittings_category = Category.objects.create(name="Fittings")
        self.conduits_category = Category.objects.create(name="Conduits")

        self.steel_tag = Tag.objects.create(name="Steel")
        self.pvc_tag = Tag.objects.create(name="PVC")
        self.half_inch_tag = Tag.objects.create(name='1/2"')

        # Test Product 1
        self.product1 = Product.objects.create(
            description='1/2" EMT Connector, Compression, Steel',
            category=self.fittings_category,
        )
        self.product1.tags.add(self.steel_tag)
        self.product1.tags.add(self.half_inch_tag)
        
        # Test Product 2
        self.product2 = Product.objects.create(
            description='4" PVC Coated Conduit',
            category=self.conduits_category,
        )
        self.product2.tags.add(self.pvc_tag)
        
        # Test Product 3
        self.product3 = Product.objects.create(
            description='1/2" EMT Coupling, Compression, Steel',
            category=self.fittings_category,
        )
        self.product3.tags.add(self.steel_tag)
        self.product3.tags.add(self.half_inch_tag)


    def test_GivenProductSearch_WhenNoFilters_ThenReturnsAllProducts(self):
        search_result = product_search.get_filtered_products()

        self.assertEqual(search_result.count(), 3)
        self.assertIn(self.product1, search_result)
        self.assertIn(self.product2, search_result)
        self.assertIn(self.product3, search_result)
    

    def test_GivenProductSearch_WhenCategoryFilter_ThenReturnsExpectedProduct(self):
        search_result = product_search.get_filtered_products(
            category_id=str(self.conduits_category.id)
        )

        self.assertEqual(search_result.count(), 1)
        self.assertNotIn(self.product1, search_result)
        self.assertIn(self.product2, search_result)
        self.assertNotIn(self.product3, search_result)    


    def test_GivenProductSearch_WhenMultipleTagsFilter_ThenReturnsExpectedProduct(self):
        search_result = product_search.get_filtered_products(
            tag_id_list=[str(self.steel_tag.id), str(self.half_inch_tag.id)]
        )

        self.assertEqual(search_result.count(), 2)
        self.assertIn(self.product1, search_result)
        self.assertNotIn(self.product2, search_result)
        self.assertIn(self.product3, search_result)


    def test_GivenProductSearch_WhenAllFiltersUsed_ThenReturnsExpectedProduct(self):
        search_result = product_search.get_filtered_products(
            search_query="coupling",
            category_id=str(self.fittings_category.id),
            tag_id_list=[str(self.steel_tag.id), str(self.half_inch_tag.id)]
        )

        self.assertEqual(search_result.count(), 1)
        self.assertNotIn(self.product1, search_result)
        self.assertNotIn(self.product2, search_result)
        self.assertIn(self.product3, search_result)

    
    def test_GivenProductSearch_WhenNonExistentFilters_ThenReturnsNoProducts(self):
        search_result = product_search.get_filtered_products(
            search_query="fakequery",
            category_id=str(self.fittings_category.id),
            tag_id_list=[str(self.steel_tag.id), str(self.half_inch_tag.id)]
        )

        self.assertEqual(search_result.count(), 0)
        self.assertNotIn(self.product1, search_result)
        self.assertNotIn(self.product2, search_result)
        self.assertNotIn(self.product3, search_result)


    def test_GivenProductSearch_WhenQueryWithWhiteSpace_ThenReturnsNoProducts(self):
        search_result = product_search.get_filtered_products(
            search_query="     coupling     \t",
            category_id=str(self.fittings_category.id),
            tag_id_list=[str(self.steel_tag.id), str(self.half_inch_tag.id)]
        )

        self.assertEqual(search_result.count(), 1)
        self.assertNotIn(self.product1, search_result)
        self.assertNotIn(self.product2, search_result)
        self.assertIn(self.product3, search_result)

