from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import UserSerializer, LoginSerializer, CustomUserScoreSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Извлечение данных из запроса
        username = request.data.get('username')
        password = request.data.get('password')

        # Поиск пользователя по имени пользователя
        user = CustomUser.objects.filter(username=username).first()

        # Проверка наличия пользователя и правильности пароля
        if user is not None and user.check_password(password):
            if user.is_active:
                # Вход пользователя в систему
                login(request, user)
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'User is not active'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserScoreUpdateAPI(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        score_change = request.data.get('score_change', 0)
        try:
            # Проверяем, является ли score_change числовым значением
            score_change = int(score_change)
        except ValueError as e:
            return Response({'error': 'score_change должно быть числом.'}, status=400)

        user.score += score_change
        user.save()
        serializer = self.get_serializer(user)
        return Response(serializer.data)


class CustomUserViewSet(viewsets.ReadOnlyModelViewSet):  # Используйте ReadOnlyModelViewSet, если вам нужен только чтение
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserScoreUpdate(APIView):
    def patch(self, request, pk):
        user = CustomUser.objects.get(pk=pk)
        serializer = CustomUserScoreSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)