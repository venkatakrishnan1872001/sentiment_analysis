
# # your_app/pagination.py
from rest_framework.pagination import PageNumberPagination

from rest_framework.pagination import LimitOffsetPagination

from rest_framework.response import Response

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10  # Set your desired page size here
    page_size_query_param = 'page_size'
    max_page_size = 100



class MyCustomPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

    def get_limit(self, request):
        # Extract limit from query parameters, or use a default value
        limit = int(request.query_params.get('limit', self.default_limit))
        print("#limit",limit)
        return limit

    # def get_offset(self, request):
    #     # Extract offset (starting point) from query parameters, or use a default value
    #     offset = int(request.query_params.get('limit', 0))  # Default offset is 0
    #     print("offset*********",offset)
    #     return offset

