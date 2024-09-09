from django.urls import path
from .views import chunk_text, fast_reading_view

app_name = 'chunker'

urlpatterns = [
    path('', fast_reading_view, name='fast_reading'),
    path('chunk/', chunk_text, name='chunk_text'),
]
