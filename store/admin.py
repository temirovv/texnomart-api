from django.contrib.admin import register, ModelAdmin, TabularInline

from .models import Category, Product, ProductImage, Promotion, ProductInPromotion


@register(Category)
class CategoryAdmin(ModelAdmin):
    pass


class ProductImageTabularInline(TabularInline):
    model = ProductImage


@register(Product)
class ProductAdmin(ModelAdmin):
    inlines = ProductImageTabularInline, 


@register(Promotion)
class PromotionAdmin(ModelAdmin):
    pass


