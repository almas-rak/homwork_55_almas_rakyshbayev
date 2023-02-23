from django.db import models
from django.utils import timezone


# Create your models here.
class TODO(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершено')
    ]
    title = models.CharField(max_length=64, null=False, verbose_name='Заголовок')
    description = models.TextField(max_length=2000, default='', verbose_name='Описание')
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    date_of_completion = models.DateField(blank=True, null=True, default=None, verbose_name='Дата завершения')
    is_deleted = models.BooleanField(default=False)
    at_deleted = models.DateTimeField(null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.at_deleted = timezone.now()
        self.save()

    def __str__(self):
        return self.title
