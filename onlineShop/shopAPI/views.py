from django.shortcuts import render
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Comment, Good, Category
from .serializers import CommentSerializer, GoodSerializer, CategorySerializer

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_filter = ['name']
    filterset_fields = ['category', 'price', 'stock_availability', 'name']  # The rating filter must be added!
    ordering_fields = ['price']  # Which field for goods ordering should be chosen?
    # permission_classes = [IsAuthenticatedOrReadOnly]    # Are other authentication classes necessary?
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]  # Is TokemAuthentication well suited for an online-shop?


class RegistrationViewSet(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({'message': 'Username already exists!'},
                            status=status.HTTP_409_CONFLICT)

        user = User.objects.create_user(username=username, password=password)
        token = Token.objects.create(user=user)
        user.save()
        token.save()

        return Response({'token': token.key}, status=status.HTTP_201_CREATED)


class LoginViewSet(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not User.objects.filter(username=username).exists:
            return Response({'message': 'Username does not exist!'},
                            status=status.HTTP_404_NOT_FOUND)

        user = User.objects.get(username=username)

        if not user.check_password(password):
            return Response({'message': 'Wrong password!'},
                            status=status.HTTP_401_UNAUTHORIZED)

        token = Token.objects.get(user=user)

        return Response({'token': token.key}, status=status.HTTP_200_OK)
