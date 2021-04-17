from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Category(models.Model):
    class Meta:
        ordering = ['-ordering']

    name = models.CharField(max_length=100, verbose_name="category_name", blank=False)
    ordering = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Offer(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    description = models.TextField(max_length=20000)
    price = models.DecimalField(verbose_name='price', max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


@receiver(post_save, sender=Offer)
def save_offer(instance, **kwargs):
    instance.category.ordering += 1
    instance.category.save()


@receiver(post_delete, sender=Offer)
def save_offer(instance, **kwargs):
    instance.category.ordering -= 1
    instance.category.save()
