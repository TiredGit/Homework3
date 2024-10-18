import django_filters
import App.models
from App.models import ProductCategory
from django.db.models import Q


class Product(django_filters.FilterSet):
    price_range = django_filters.RangeFilter(field_name='price', label='Цена от и до')
    available = django_filters.BooleanFilter(method='filter_available', label='У товара есть изображение?')
    term = django_filters.CharFilter(method='filter_term', label='')
    category = django_filters.ModelChoiceFilter(queryset=ProductCategory.objects.all(), label='Категория')
    new = django_filters.CharFilter(method='filter_new', label='Цена ниже заданной и/или имя категории')
    class Meta:
        model = App.models.Product
        fields = ['price_range', 'available', 'term', 'category', 'new']

    def filter_available(self, queryset, name, value):
        if value is None:
            return queryset
        if value:
            return queryset.filter(product_picture__isnull=False)
        return queryset.filter(product_picture__isnull=True)

    def filter_term(self, queryset, name, value):
        criteria = Q()
        for term in value.split():
            criteria &= Q(product_name__icontains=term) | Q(description__icontains=term)

        return queryset.filter(criteria).distinct()

    def filter_new(self, queryset, name, value):
        criteria = Q()
        for new in value.split():
            if new.isdigit():
                criteria &= Q(price__lt=new)
            else:
                criteria &= Q(category__category_name__icontains=new)

        return queryset.filter(criteria).distinct()