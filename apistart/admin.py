from django.contrib import admin
from .models import Basket, Pantry

# Define a custom admin class for the Pantry model
class PantryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'basket')
    list_filter = ('basket',)
    search_fields = ('name', 'description')
    readonly_fields = ('key_value_store',)  # Make the key-value store read-only in the admin

# Register the Pantry model with the custom admin class
admin.site.register(Pantry, PantryAdmin)

# Register the Basket model as well
admin.site.register(Basket)
