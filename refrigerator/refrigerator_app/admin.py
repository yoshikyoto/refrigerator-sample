from django.contrib import admin
from refrigerator_app.models import FoodCategory, Food, Stock, User


admin.site.register(FoodCategory)
admin.site.register(Food)
admin.site.register(Stock)
admin.site.register(User)
