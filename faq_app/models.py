from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)  # Hindi
    question_bn = models.TextField(blank=True, null=True)  # Bengali
    answer_hi = RichTextField(blank=True, null=True)  # Hindi
    answer_bn = RichTextField(blank=True, null=True)  # Bengali

    def translate_text(self, text, dest_language):
        translator = Translator()
        try:
            translation = translator.translate(text, dest=dest_language)
            return translation.text
        except:
            return text  # Fallback to original text if translation fails

    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = self.translate_text(self.question, 'hi')
        if not self.question_bn:
            self.question_bn = self.translate_text(self.question, 'bn')
        if not self.answer_hi:
            self.answer_hi = self.translate_text(self.answer, 'hi')
        if not self.answer_bn:
            self.answer_bn = self.translate_text(self.answer, 'bn')
        super().save(*args, **kwargs)

    def get_translated_question(self, lang):
        if lang == 'hi':
            return self.question_hi
        elif lang == 'bn':
            return self.question_bn
        return self.question

    def get_translated_answer(self, lang):
        if lang == 'hi':
            return self.answer_hi
        elif lang == 'bn':
            return self.answer_bn
        return self.answer

    def __str__(self):
        return self.question