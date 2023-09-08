from django.db import models

class Basket(models.Model):
    name = models.CharField(max_length=255)
    ttl = models.PositiveIntegerField()

class Pantry(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='pantries')
    key_value_store = models.JSONField(default=dict)  # Key-value store for the pantry

    def __str__(self):
        return self.name
