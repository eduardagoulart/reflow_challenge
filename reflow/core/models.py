from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(primary_key=True)
    skills = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CompleteDescription(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.candidate.name
