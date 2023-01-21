from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title


class SubCategory(models.Model):
     title1 = models.CharField(max_length=255)
     category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

     class Meta:
        verbose_name_plural = 'SubCategories'

     def __str__(self):
        return self.title1

class Item(models.Model):
    item_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory,related_name='subcategory', on_delete=models.CASCADE)
    price = models.IntegerField()
    units = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{} {}'.format(self.item_tag, self.name)

