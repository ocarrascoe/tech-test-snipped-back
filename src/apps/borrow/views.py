from rest_framework.response import Response
from rest_framework.views import APIView

from apps.borrow.use_cases import BorrowUseCases


class BorrowDetailView(APIView):
    # Create new book
    def post(self, request, format=None):
        response = BorrowUseCases().create_borrow(user_id=request.data['user_id'],
                                                  book_id=request.data['book_id'])
        return Response(response['data'], status=response['status'])

class BorrowBookView(APIView):
    # Create new book
    def post(self, request, format=None):
        response = BorrowUseCases().return_book(book_id=request.data)
        return Response(response['data'], status=response['status'])