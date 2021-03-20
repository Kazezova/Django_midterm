from django.shortcuts import render, get_object_or_404
from rest_framework import generics, mixins, viewsets, status
from main.models import Book, Journal
from main.serializers import BookSerializer, JournalSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class BookViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset

    def check_user(self, request):
        user = request.user
        return user.is_staff is True

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        if self.check_user(request):
            book = Book.objects.create(
                name=request.data['name'],
                price=request.data['price'],
                description=request.data['description'],
                created_at=request.data['created_at'],
                genre=request.data['genre'],
                num_pages=request.data['num_pages'],
            )
            book.save()
            return Response({'success': 'Книга успешно создана.'})
        return Response({'error': 'У вас нет доступа к редактированию.'}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        book = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def update(self, request, pk=None):
        if self.check_user(request):
            book = get_object_or_404(self.get_queryset(), pk=pk)
            book.name = request.data['name']
            book.price = request.data['price']
            book.description = request.data['description']
            book.created_at = request.data['created_at']
            book.genre = request.data['genre']
            book.save()
            serializer = JournalSerializer(book)
            return Response(serializer.data)
        return Response({'error': 'У вас нет доступа к редактированию.'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        if self.check_user(request):
            book = get_object_or_404(self.get_queryset(), pk=pk)
            book.delete()
            return Response({'success': 'Удаление прошло успешно.'})
        return Response({'error': 'У вас нет доступа к удалению.'}, status=status.HTTP_404_NOT_FOUND)


class JournalViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = JournalSerializer

    def get_queryset(self):
        queryset = Journal.objects.all()
        return queryset

    def check_user(self, request):
        user = request.user
        return user.is_staff is True

    def list(self, request):
        print(self.check_user(request))
        queryset = self.get_queryset()
        serializer = JournalSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        if self.check_user(request):
            journal = Book.objects.create(
                name=request.data['name'],
                price=request.data['price'],
                description=request.data['description'],
                created_at=request.data['created_at'],
                type=request.data['type'],
                publisher=request.data['publisher'],
            )
            journal.save()
            return Response({'success': 'Журнал успешно создан.'})
        return Response({'error': 'У вас нет доступа к редактированию.'}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        journal = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = JournalSerializer(journal)
        return Response(serializer.data)

    def update(self, request, pk=None):
        if self.check_user(request):
            journal = get_object_or_404(self.get_queryset(), pk=pk)
            journal.name = request.data['name']
            journal.price = request.data['price']
            journal.description = request.data['description']
            journal.created_at = request.data['created_at']
            journal.type = request.data['type']
            journal.save()
            serializer = JournalSerializer(journal)
            return Response(serializer.data)
        return Response({'error': 'У вас нет доступа к редактированию.'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        if self.check_user(request):
            journal = get_object_or_404(self.get_queryset(), pk=pk)
            journal.delete()
            return Response({'success': 'Удаление прошло успешно.'})
        return Response({'error': 'У вас нет доступа к редактированию.'}, status=status.HTTP_404_NOT_FOUND)
