from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer
from django.core.cache import cache

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        cached_data = cache.get(cache_key)
        if cached_data:
            return cached_data
        faqs = FAQ.objects.all()
        for faq in faqs:
            faq.question = faq.get_translated_question(lang)
            faq.answer = faq.get_translated_answer(lang)
        cache.set(cache_key, faqs, timeout=60*15)  # Cache for 15 minutes
        return faqs

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        # Ensure the response data is a list
        if not isinstance(response.data, list):
            response.data = [response.data]
        return response