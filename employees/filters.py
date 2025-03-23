import django_filters
from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name = 'designation', lookup_expr='iexact')
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    """
    # Here we are refering Primary key above two are models attributs but this is primary key but out goal is yo fetch data using emp_id
    """
    # id = django_filters.RangeFilter(field_name='id') 
    #Range filter only works on integer field using primary key it wont works on characeter field
    # id = django_filters.RangeFilter(field_name='id') 

    #filter_by_id_range it can be anything it is custom

    id_min = django_filters.CharFilter(method = 'filter_by_id_range', label='From EMP ID ')
    id_max = django_filters.CharFilter(method = 'filter_by_id_range', label='To EMP ID')

    class Meta:
        model = Employee
        fields = ['designation', 'emp_name','id_min','id_max']

    def filter_by_id_range(self,queryset, name, value):
        if name == 'id_min':
            return queryset.filter(emp_id__gte=value)
        elif name == 'id_max':
            return queryset.filter(emp_id__lte=value)
        return queryset