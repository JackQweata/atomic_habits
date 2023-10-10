from rest_framework.pagination import PageNumberPagination


class ListHabitsPagination(PageNumberPagination):
    page_size = 5
    