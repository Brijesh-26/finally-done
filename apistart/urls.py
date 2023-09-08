from django.urls import path
from .views import create_pantry, update_key_value_store
from .views import get_basket_key_value
from .views import list_baskets_by_pantry
from .views import update_basket_key_value
from .views import delete_basket

urlpatterns = [
    path('baskets/<int:basket_id>/create-pantry/', create_pantry, name='create-pantry'),
    path('pantries/<int:pantry_id>/update-key-value-store/', update_key_value_store, name='update-key-value-store'),
    path('pantries/<int:pantry_id>/get-basket-key-value/<str:basket_key>/', get_basket_key_value, name='get-basket-key-value'),
    
    path('pantries/<int:pantry_id>/list-baskets/', list_baskets_by_pantry, name='list-baskets-by-pantry'),
    path('pantries/<int:pantry_id>/update-basket-key-value/<str:basket_key>/', update_basket_key_value, name='update-basket-key-value'),
path('pantries/<int:pantry_id>/delete-basket/<str:basket_key>/', delete_basket, name='delete-basket'),
]
