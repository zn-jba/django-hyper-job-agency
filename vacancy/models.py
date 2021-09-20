from django.contrib.auth.models import User
from django.db import models


class Vacancy(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)

    def __str__(self) -> str:
        return self.author.username

    class Meta:
        verbose_name_plural = "Vacancies"
