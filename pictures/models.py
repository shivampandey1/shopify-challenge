from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __string__(self):
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null =True, blank=True)
    picture = models.ImageField(null=False, blank=False)
    desc = models.CharField(max_length=100, null=False, blank=False)

    def __string__(self):
        return self.desc
