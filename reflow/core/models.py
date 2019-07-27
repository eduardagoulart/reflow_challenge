from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(primary_key=True)
    skills = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    github = models.URLField()
    portifolio = models.URLField(blank=True)
    experiencia = models.TextField(blank=True)
    resume = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name