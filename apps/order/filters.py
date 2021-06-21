from django_filters import rest_framework as filters

from .models import Order


class OrderFilter(filters.FilterSet):
    profile = filters.NumberFilter(field_name="profile__pk")
    session = filters.NumberFilter(field_name="session__pk")
    course = filters.NumberFilter(field_name="session__course__pk")

    class Meta:
        model = Order
        fields = ["profile", "course", "session"]
