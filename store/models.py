from django.db import models


class Category(models.Model):
    """
        Categoriya Modeli
    """
    image = models.ImageField(upload_to='categories/', help_text="Kategoriya rasmi")
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, help_text="Kategoriya otasi")

    def __str__(self):
        return F"Category - {self.name}"


class Product(models.Model):
    """
        Product Modeli 
    """
    name = models.CharField(max_length=255, help_text="Mahsulot nomi")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text="Mahsulot kategoriyasi")
    price = models.FloatField(help_text="Mahsulot narxi")
    installment_payment_12 = models.FloatField(help_text="12 oyda davomida qancha summadan to'lashi")
    installment_payment_24 = models.FloatField(help_text="24 oyda davomida qancha summadan to'lashi")
    attributes = models.JSONField(help_text="Mahsulot tavfsilotlari")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    """
        ProductImage modeli - rasmlar uchun
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product-images/', help_text="Mahsulot rasmi")


class Promotion(models.Model):
    """
        Promotion modeli - aksiya uchun
    """
    image = models.ImageField(upload_to='promotions/', help_text="Banner rasmi")
    title = models.CharField(max_length=255, help_text="Aksiya sarlavhasi")
    description = models.TextField(help_text='Aksiya tavfsilotlari')
    is_active = models.BooleanField(default=True, help_text="Aksiya aktivligi")
    start = models.DateField(help_text="Aksiya boshlanish sanasi")
    end = models.DateField(help_text="Aksiya tugash sanasi")
    products = models.ManyToManyField(Product, through='ProductInPromotion')

    def __str__(self):
        return f"Aksiya - {self.title}"


class ProductInPromotion(models.Model):
    """
        ProductInPromotion modeli aksiyaga tushgan mahsulotlar
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
