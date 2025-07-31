from rest_framework import routers
from django.urls import path, include
from daily_verse_app import api_views

router = routers.DefaultRouter()
# You can register viewsets here if needed

urlpatterns = [
    path('verse/daily/', api_views.DailyVerseAPIView.as_view(), name='daily-verse'),
    path('verse/<str:translation>/<str:book>/<int:chapter>/<int:verse>/', api_views.SpecificVerseAPIView.as_view(), name='specific-verse'),
    path('chapter/<str:translation>/<str:book>/<int:chapter>/', api_views.ChapterAPIView.as_view(), name='chapter'),
    path('books/', api_views.BooksAPIView.as_view(), name='books'),
    path('books/<str:book>/chapters/', api_views.BookChaptersAPIView.as_view(), name='book-chapters'),
    path('search/', api_views.SearchVerseAPIView.as_view(), name='search-verse'),
    path('commentaries/', api_views.CommentariesAPIView.as_view(), name='commentaries'),
    path('commentaries/<int:commentary_id>/<str:book>/<int:chapter>/<int:verse>/', api_views.CommentaryDetailAPIView.as_view(), name='commentary-detail'),
    path('verse/daily/archive/', api_views.DailyVerseArchiveAPIView.as_view(), name='daily-verse-archive'),
    path('verse/random/', api_views.RandomVerseAPIView.as_view(), name='random-verse'),
    path('health/', api_views.HealthAPIView.as_view(), name='health'),
    path('', include(router.urls)),
]
