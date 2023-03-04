import django_filters

from .models import Donor

class OrderFilter(django_filters.FilterSet):
    state = django_filters.CharFilter(lookup_expr='icontains')
    district = django_filters.CharFilter(lookup_expr='icontains')
    city = django_filters.CharFilter(lookup_expr='icontains')
    blood_group = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Donor
        fields = ['state', 'district', 'city', 'blood_group']
        
        """ fields = {
            'state': ['icontains'],
            'district': ['icontains'],
            'city': ['icontains'],
            'blood_group': ['icontains'],
                
            }
 """
    
