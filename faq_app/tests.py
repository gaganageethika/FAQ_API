from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from django.core.cache import cache
from .models import FAQ

# Test cases for the FAQ model
class FAQModelTest(TestCase):
    def test_faq_creation(self):
        faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework."
        )
        self.assertEqual(faq.question, "What is Django?")
        self.assertEqual(faq.answer, "Django is a web framework.")

    def test_translation_fields_populated(self):
        faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework."
        )
        self.assertIsNotNone(faq.question_hi)  # Hindi translation
        self.assertIsNotNone(faq.question_bn)  # Bengali translation
        self.assertIsNotNone(faq.answer_hi)    # Hindi translation
        self.assertIsNotNone(faq.answer_bn)    # Bengali translation

# Test cases for the FAQ API views
class FAQViewSetTest(APITestCase):
    def setUp(self):
        # Clear the database and cache before each test
        FAQ.objects.all().delete()
        cache.clear()
        # Create a single FAQ for testing
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework."
        )

    def test_fetch_faqs_english(self):
        url = reverse('faq-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)  # Ensure only one FAQ is returned
        self.assertEqual(response.data[0]['question'], "What is Django?")
        self.assertEqual(response.data[0]['answer'], "Django is a web framework.")

    def test_fetch_faqs_hindi(self):
        url = reverse('faq-list') + '?lang=hi'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)  # Ensure only one FAQ is returned
        self.assertNotEqual(response.data[0]['question'], "What is Django?")  # Should be translated
        self.assertNotEqual(response.data[0]['answer'], "Django is a web framework.")  # Should be translated

    def test_fetch_faqs_bengali(self):
        url = reverse('faq-list') + '?lang=bn'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)  # Ensure only one FAQ is returned
        self.assertNotEqual(response.data[0]['question'], "What is Django?")  # Should be translated
        self.assertNotEqual(response.data[0]['answer'], "Django is a web framework.")  # Should be translated

    def test_empty_faq_list(self):
        # Clear the database before testing
        FAQ.objects.all().delete()
        url = reverse('faq-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)  # Ensure no FAQs are returned

    def test_invalid_language_parameter(self):
        url = reverse('faq-list') + '?lang=invalid'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)  # Ensure only one FAQ is returned
        self.assertEqual(response.data[0]['question'], "What is Django?")  # Fallback to English
        self.assertEqual(response.data[0]['answer'], "Django is a web framework.")  # Fallback to English

# Test cases for caching
class FAQCacheTest(TestCase):
    def test_cache_population(self):
        # Clear the database and cache before testing
        FAQ.objects.all().delete()
        cache.clear()

        faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework."
        )
        lang = 'hi'
        cache_key = f'faqs_{lang}'
        cached_data = cache.get(cache_key)
        self.assertIsNone(cached_data)  # Cache should be empty initially

        # Fetch FAQs to populate the cache
        url = reverse('faq-list') + f'?lang={lang}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Check if the cache is populated
        cached_data = cache.get(cache_key)
        self.assertIsNotNone(cached_data)
        self.assertEqual(cached_data[0].question, faq.get_translated_question(lang))
        self.assertEqual(cached_data[0].answer, faq.get_translated_answer(lang))