from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    trend = models.CharField(max_length=20, choices=[('up', 'Up'), ('down', 'Down'), ('stable', 'Stable')], default='stable')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - ₹{self.current_price}"

class CropPriceHistory(models.Model):
    crop = models.ForeignKey(Crop, related_name='price_history', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    class Meta:
        unique_together = ('crop', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.crop.name} - {self.date} - ₹{self.price}"

class Scheme(models.Model):
    CATEGORY_CHOICES = [
        ('pre_crop', 'Pre-Crop Scheme'),
        ('crop_loss', 'Crop Loss Support'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    eligibility = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='pre_crop')
    link = models.URLField()
    
    def __str__(self):
        return self.title

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    crop_interest = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
