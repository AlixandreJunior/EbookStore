from django.db import models

class Category(models.Model):
    class Meta:
        app_label = "ebook"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Ebook(models.Model):
    class Meta:
        app_label = "ebook"
        verbose_name = "Ebook"
        verbose_name_plural = "Ebooks"

    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    category = models.ManyToManyField(Category)
    file = models.FileField(upload_to="ebooks/files/", blank=False, null=False) 
    cover = models.ImageField(upload_to="ebooks/covers/", blank=True, null=True)

    def __str__(self):
        return self.title