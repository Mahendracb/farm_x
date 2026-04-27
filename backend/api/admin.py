from django.contrib import admin
from .models import Crop, CropPriceHistory, Scheme, Buyer

admin.site.register(Crop)
admin.site.register(CropPriceHistory)
admin.site.register(Scheme)
admin.site.register(Buyer)
