import django_filters
from .models import Event, Location
from django import forms

class EventFilter(django_filters.FilterSet):
    start_date_from = django_filters.DateTimeFilter(
        field_name='start_date',
        lookup_expr='gte',
        label="Дата начала с"
    )
    start_date_to = django_filters.DateTimeFilter(
        field_name='start_date',
        lookup_expr='lte',
        label="Дата начало до"
    )

    end_date_from = django_filters.DateTimeFilter(
        field_name='end_date',
        lookup_expr='gte',
        label="Дата завершения с"
    )
    end_date_to = django_filters.DateTimeFilter(
        field_name='end_date',
        lookup_expr='lte',
        label="Дата заверешния до"
    )

    top_from = django_filters.NumberFilter(
        field_name='top',
        lookup_expr='gte',
        label="Рейтинг с"
    )
    top_to = django_filters.NumberFilter(
        field_name='top',
        lookup_expr='lte',
        label="Рейтинг до"
    )

    search_name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label="Поиск по названию события"
    )
    search_loc = django_filters.CharFilter(
        field_name='id_location__name',
        lookup_expr='icontains',
        label="Поиск по локации"
    )
    search_location = django_filters.ModelMultipleChoiceFilter(
        field_name='id_location__name',
        queryset=Location.objects.all(),
        widget = forms.SelectMultiple,
        label="Выбор локации"
    )
    ordering = django_filters.OrderingFilter(
        fields=(
            ('name', 'name'),
            ('-name', '-name'),
            ('start_date', 'start_date'),
            ('-start_date', '-start_date'),
            ('end_date', 'end_date'),
            ('-end_date', '-end_date'),
        ),
        field_labels={
            'name': 'Название А-Я',
            '-name': 'Название Я-А',
            'start_date': 'Дата начала (старые)',
            '-start_date': 'Дата начала (новые)',
            'end_date': 'Дата окончания (скоро)',
            '-end_date': 'Дата окончания(не скоро)',
        },
        label="Сортировка"
    )
    
    class Meta:
        model = Event
        fields = []
    #class Meta:
        #model = Event
        #fields = {
          #  'start_date': ['gte', 'lte'], 
            #'end_date': ['gte', 'lte'],
           # }