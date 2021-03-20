from django.urls import path, include
from main.views import BookViewSet, JournalViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('books', BookViewSet, basename='main')
router.register('journals', JournalViewSet, basename='main')

journal_detail = JournalViewSet.as_view({
    'post': 'create',
    'get': 'retrieve',
    'put': 'update',
    'delete': 'delete',
})

book_detail = BookViewSet.as_view({
    'post': 'create',
    'get': 'retrieve',
    'put': 'update',
    'delete': 'delete',
})
urlpatterns = [
    path('journals/<int:pk>', journal_detail),
    path('books/<int:pk>', book_detail)
]
urlpatterns += router.urls
