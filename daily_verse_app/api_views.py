from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from django.conf import settings
from .models import Verse, ShownVerse
from .verse_manager import VerseManager
from datetime import date

BASE_API_URL = "https://bible.helloao.org/api/v1"

class DailyVerseAPIView(APIView):
    def get(self, request):
        translation = request.GET.get('translation', 'kjv')
        theme = request.GET.get('theme')
        # Use VerseManager or fetch from API
        manager = VerseManager(translation=translation)
        verse = manager.get_daily_verse()
        return Response(verse)

class SpecificVerseAPIView(APIView):
    def get(self, request, translation, book, chapter, verse):
        url = f"{BASE_API_URL}/verse/{translation}/{book}/{chapter}/{verse}/"
        resp = requests.get(url)
        if resp.status_code == 200:
            return Response(resp.json())
        return Response({'detail': 'Not found'}, status=404)

class ChapterAPIView(APIView):
    def get(self, request, translation, book, chapter):
        url = f"{BASE_API_URL}/chapter/{translation}/{book}/{chapter}/"
        resp = requests.get(url)
        if resp.status_code == 200:
            return Response(resp.json())
        return Response({'detail': 'Not found'}, status=404)

class BooksAPIView(APIView):
    def get(self, request):
        url = f"{BASE_API_URL}/books/"
        resp = requests.get(url)
        if resp.status_code == 200:
            return Response(resp.json())
        return Response({'detail': 'Not found'}, status=404)

class BookChaptersAPIView(APIView):
    def get(self, request, book):
        url = f"{BASE_API_URL}/books/{book}/chapters/"
        resp = requests.get(url)
        if resp.status_code == 200:
            return Response(resp.json())
        return Response({'detail': 'Not found'}, status=404)

class SearchVerseAPIView(APIView):
    def get(self, request):
        q = request.GET.get('q')
        translation = request.GET.get('translation', 'kjv')
        url = f"{BASE_API_URL}/search/"
        params = {'q': q, 'translation': translation}
        resp = requests.get(url, params=params)
        if resp.status_code == 200:
            return Response(resp.json())
        return Response({'detail': 'Not found'}, status=404)

class CommentariesAPIView(APIView):
    def get(self, request):
        url = f"{BASE_API_URL}/commentaries/"
        resp = requests.get(url)
        if resp.status_code == 200:
            return Response(resp.json())
        return Response({'detail': 'Not found'}, status=404)

class CommentaryDetailAPIView(APIView):
    def get(self, request, commentary_id, book, chapter, verse):
        url = f"{BASE_API_URL}/commentaries/{commentary_id}/{book}/{chapter}/{verse}/"
        resp = requests.get(url)
        if resp.status_code == 200:
            return Response(resp.json())
        return Response({'detail': 'Not found'}, status=404)

class DailyVerseArchiveAPIView(APIView):
    def get(self, request):
        month = request.GET.get('month')
        year = request.GET.get('year')
        filters = {}
        if month:
            filters['date_shown__month'] = month
        if year:
            filters['date_shown__year'] = year
        queryset = ShownVerse.objects.filter(**filters).order_by('-date_shown')
        data = [
            {
                'reference': sv.verse.reference,
                'text': sv.verse.text,
                'translation': sv.translation,
                'book': sv.book,
                'date_shown': sv.date_shown
            }
            for sv in queryset
        ]
        return Response(data)

class RandomVerseAPIView(APIView):
    def get(self, request):
        translation = request.GET.get('translation', 'kjv')
        url = f"{BASE_API_URL}/verse/random/"
        params = {'translation': translation}
        resp = requests.get(url, params=params)
        if resp.status_code == 200:
            return Response(resp.json())
        return Response({'detail': 'Not found'}, status=404)

class HealthAPIView(APIView):
    def get(self, request):
        return Response({'status': 'ok'})
