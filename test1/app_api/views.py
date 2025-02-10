from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, pagination
from django.shortcuts import get_object_or_404
from .models import Account
from .serializers import AccountSerializer
from django.db.models import Q

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CreateAccountView(APIView):
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Tài khoản đã được tạo thành công!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Tạo tài khoản thất bại!",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class GetAllAccountsView(APIView):
    def get(self, request):
        accounts = Account.objects.all().order_by('-registerID')
        
        search_query = request.query_params.get('search', '').strip()
        
        if search_query:
            accounts = accounts.filter(
                Q(login__icontains=search_query) |
                Q(phone__icontains=search_query)
            )
        
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(accounts, request)
        serializer = AccountSerializer(result_page, many=True)

        return paginator.get_paginated_response({
            "message": "Danh sách tài khoản đã được lấy thành công!",
            "results": serializer.data
        })


class GetAccountView(APIView):
    def get(self, request, pk):
        account = get_object_or_404(Account, pk=pk)
        serializer = AccountSerializer(account)
        return Response({
            "message": "Lấy thông tin tài khoản thành công!",
            "data": serializer.data
        })


class UpdateAccountView(APIView):
    def put(self, request, pk):
        account = get_object_or_404(Account, pk=pk)
        serializer = AccountSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Cập nhật tài khoản thành công!",
                "data": serializer.data
            })
        return Response({
            "message": "Cập nhật tài khoản thất bại!",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class DeleteAccountView(APIView):
    def delete(self, request, pk):
        account = get_object_or_404(Account, pk=pk)
        account.delete()
        return Response({
            "message": "Xóa tài khoản thành công!"
        }, status=status.HTTP_204_NO_CONTENT)
