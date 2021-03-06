from django.db import models


class Task(models.Model):
    task = models.CharField(max_length=150, verbose_name='Дело', db_index=True)
    is_complete = models.BooleanField(verbose_name='Выполнено?', default=False)
    published_at = models.DateField(auto_now_add=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.task

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ['published_at']


