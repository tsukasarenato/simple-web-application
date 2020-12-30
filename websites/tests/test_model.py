from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import Websites, Categories, Products, Groups, Options


class InitialDataTest(TestCase):
    """
    Register necessary initial data for the tests
    """
    @classmethod
    def setUpTestData(cls):
        cls.website = Websites.objects.create(url='url', title="_title")
        cls.category = Categories.objects.create(websites=cls.website, title="_title")
        cls.product = Products.objects.create(websites=cls.website, categories=cls.category, title="_title", price=1)
        cls.group = Groups.objects.create(websites=cls.website, products=cls.product, title="_title")
        cls.option = Options.objects.create(websites=cls.website, groups=cls.group, title="_title")


class ProductsModelTest(InitialDataTest):

    def test_unique_constraints(self):
        """
        Register two products with same website and title (slug)
        """

        with self.assertRaises(Exception):
            Products.objects.create(websites=self.website, categories=self.category, title="_title", price=1)

    def test_fail_in_check_price_without_price(self):
        """
        Register a product with price_type in (1,2,3) and price=None
        """

        with self.assertRaises(ValidationError):
            Products.objects.create(websites=self.website, categories=self.category, title="title", price_type='1')

        with self.assertRaises(ValidationError):
            Products.objects.create(websites=self.website, categories=self.category, title="title", price_type='2')

    def test_fail_in_check_price_with_price(self):
        """
        Register a product with price_type in (4,5) and price=1
        """

        with self.assertRaises(ValidationError):
            Products.objects.create(websites=self.website, categories=self.category, title="title", price_type='3',
                                    price=1)

    def test_success_in_check_price_with_price(self):
        """
        Register a product with price_type in (1,2,3) and price=1, price_type = 1 was registered in setUp
        """

        Products.objects.create(websites=self.website, categories=self.category, title="title2", price_type='2',
                                price=1, position=2)

        self.assertQuerysetEqual(Products.objects.all().order_by('position'),
                                 ['<Products: _title>', '<Products: title2>'])

    def test_success_in_check_price_without_price(self):
        """
        Register a product with price_type in (4,5) and price=None
        """

        Products.objects.create(websites=self.website, categories=self.category, title="title2", price_type='3',
                                position=1)

        self.assertQuerysetEqual(Products.objects.all().order_by('position'),
                                 ['<Products: _title>', '<Products: title2>'])

    def test_fail_in_check_promotional_price_without_price(self):
        """
        Register a product without price, but with promotional price
        """

        with self.assertRaises(ValidationError):
            Products.objects.create(websites=self.website, categories=self.category, title="title", price_type='4',
                                    promotional_price=1)

    def test_fail_in_check_promotional_price_with_price(self):
        """
        Register a product with promotional price greater than price
        """

        with self.assertRaises(ValidationError):
            Products.objects.create(websites=self.website, categories=self.category, title="title", price=1,
                                    promotional_price=2)

    def test_success_in_check_promotional_price(self):
        """
        Register a product with promotional price
        """

        Products.objects.create(websites=self.website, categories=self.category, title="title", price=2,
                                promotional_price=1)

        self.assertQuerysetEqual(Products.objects.all().order_by('position'),
                                 ['<Products: _title>', '<Products: title>'])

    def test_if_price_type_is_str(self):
        """
        Register a product with price type using integer
        """

        with self.assertRaises(ValidationError):
            Products.objects.create(websites=self.website, categories=self.category, title="title", price_type=1,
                                    price=2)


class GroupsModelTest(InitialDataTest):

    def test_unique_constraints(self):
        """
        Register two products with same website and title (slug)
        """

        with self.assertRaises(Exception):
            Groups.objects.create(websites=self.website, products=self.product, title="_title")

    def test_check_min_and_max(self):
        """
        Register a group with minimum value greater than maximum value
        """

        with self.assertRaises(ValidationError):
            Groups.objects.create(websites=self.website, products=self.product, title="title", minimum=2, maximum=1)


class OptionsModelTest(InitialDataTest):

    def test_unique_constraints(self):
        """
        Register two products with same website and title (slug)
        """

        with self.assertRaises(Exception):
            Options.objects.create(websites=self.website, groups=self.group, title="_title")

    def test_check_max_and_max(self):
        """
        Register a group with minimum value greater than maximum value
        """

        with self.assertRaises(ValidationError):
            Options.objects.create(websites=self.website, groups=self.group, title="title", maximum=2)
