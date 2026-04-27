import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from api.models import Crop, CropPriceHistory
from datetime import timedelta
from django.utils import timezone

crops_data = [
    {"name": "Ragi (Finger Millet)", "price_range": (3000, 4000), "location": "Mandya, Tumakuru"},
    {"name": "Jowar (Sorghum)", "price_range": (2500, 3200), "location": "Vijayapura, Kalaburagi"},
    {"name": "Paddy (Rice)", "price_range": (2000, 2800), "location": "Raichur, Shivamogga"},
    {"name": "Tur Dal (Pigeon Pea)", "price_range": (8000, 11000), "location": "Kalaburagi, Bidar"},
    {"name": "Sugarcane", "price_range": (2500, 3500), "location": "Mandya, Belagavi"},
    {"name": "Coffee (Arabica)", "price_range": (18000, 22000), "location": "Kodagu, Chikkamagaluru"},
    {"name": "Arecanut", "price_range": (40000, 50000), "location": "Shivamogga, Dakshina Kannada"},
    {"name": "Cotton", "price_range": (6000, 8000), "location": "Raichur, Dharwad"},
    {"name": "Coconut", "price_range": (1500, 2500), "location": "Tumakuru, Hassan"},
    {"name": "Groundnut", "price_range": (5000, 7000), "location": "Chitradurga, Tumakuru"},
    {"name": "Maize (Corn)", "price_range": (2000, 2500), "location": "Davanagere, Haveri"},
    {"name": "Sunflower", "price_range": (4500, 6000), "location": "Koppal, Raichur"},
    {"name": "Bajra (Pearl Millet)", "price_range": (2200, 2800), "location": "Bagalkote, Vijayapura"},
    {"name": "Black Gram", "price_range": (7000, 9000), "location": "Bidar, Kalaburagi"},
    {"name": "Green Gram", "price_range": (6500, 8500), "location": "Gadag, Dharwad"},
    {"name": "Cardamom", "price_range": (150000, 200000), "location": "Kodagu, Hassan"},
    {"name": "Black Pepper", "price_range": (45000, 55000), "location": "Kodagu, Chikkamagaluru"},
    {"name": "Onion", "price_range": (1500, 3000), "location": "Chitradurga, Gadag"},
    {"name": "Tomato", "price_range": (800, 2000), "location": "Kolar, Bengaluru Rural"},
    {"name": "Pomegranate", "price_range": (8000, 15000), "location": "Koppal, Bagalkote"},
    {"name": "Fig (Anjeer)", "price_range": (5000, 8000), "location": "Ballari, Koppal"},
    {"name": "Rose (Flowers)", "price_range": (10000, 15000), "location": "Bengaluru Urban, Bengaluru Rural"},
    {"name": "Turmeric", "price_range": (6000, 9000), "location": "Chamarajanagar, Mysuru"},
    {"name": "Grapes", "price_range": (3000, 5000), "location": "Chikkaballapur, Bengaluru Rural"},
    {"name": "Tobacco", "price_range": (10000, 13000), "location": "Mysuru, Hassan"},
    {"name": "Silk Cocoon", "price_range": (30000, 45000), "location": "Ramanagara, Chikkaballapur"},
    {"name": "Cashew", "price_range": (60000, 80000), "location": "Udupi, Dakshina Kannada"},
    {"name": "Pineapple", "price_range": (2000, 4000), "location": "Uttara Kannada, Shivamogga"},
    {"name": "Tur Dal (Pigeon Pea)", "price_range": (8000, 11000), "location": "Yadgir, Kalaburagi"}
]

def seed():
    Crop.objects.all().delete()
    print("Deleted old crops.")
    
    today = timezone.now().date()
    
    for c in crops_data:
        price = random.randint(c["price_range"][0], c["price_range"][1])
        trend = random.choice(['up', 'down', 'stable'])
        crop = Crop.objects.create(
            name=c["name"],
            current_price=price,
            location=c["location"],
            trend=trend
        )
        
        # Generate 14 days of history
        current_history_price = price
        history_objects = []
        for i in range(14):
            hist_date = today - timedelta(days=13 - i)
            # Add some random fluctuation
            variation = random.randint(-50, 50)
            current_history_price = max(100, current_history_price + variation)
            history_objects.append(
                CropPriceHistory(crop=crop, price=current_history_price, date=hist_date)
            )
        
        CropPriceHistory.objects.bulk_create(history_objects)
        
        # update current_price to the last history price
        crop.current_price = history_objects[-1].price
        
        # basic trend logic based on last 2 days
        if history_objects[-1].price > history_objects[-2].price:
            crop.trend = 'up'
        elif history_objects[-1].price < history_objects[-2].price:
            crop.trend = 'down'
        else:
            crop.trend = 'stable'
            
        crop.save()
        
    print(f"Successfully seeded {len(crops_data)} crops from Karnataka with 14-day history!")

if __name__ == '__main__':
    seed()
