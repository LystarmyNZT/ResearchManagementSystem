from django.db import models
from django.contrib.auth.models import User

class ResearchArticles(models.Model):
    Rtitle=models.CharField(max_length=100)
    Rauthor=models.ForeignKey(User,related_name="Article",on_delete=models.CASCADE)
    Rinstitution=models.CharField(max_length=100)
    Rintroduction=models.TextField()
    Rpublish=models.DateTimeField(auto_now_add=True)
    Rcategory=models.CharField(max_length=100)
    Rfund=models.IntegerField(default=0)
    Rrank=models.CharField(max_length=100)
    Rjournal=models.CharField(max_length=100)
    class Meta:
       ordering=("-Rpublish",)