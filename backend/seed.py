import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from api.models import Crop, Scheme, Buyer

def seed():
    # Clear existing data
    Crop.objects.all().delete()
    Scheme.objects.all().delete()
    Buyer.objects.all().delete()

    # Create Mock Crops for all over Karnataka
    Crop.objects.create(name='Sugarcane', current_price=315.00, location='Mandya APMC', trend='stable')
    Crop.objects.create(name='Coffee (Arabica)', current_price=18500.00, location='Madikeri (Kodagu)', trend='up')
    Crop.objects.create(name='Arecanut', current_price=45000.00, location='Shivamogga APMC', trend='down')
    Crop.objects.create(name='Tur Dal (Toor/Arhar)', current_price=9800.00, location='Kalaburagi APMC', trend='up')
    Crop.objects.create(name='Cotton', current_price=7100.00, location='Raichur APMC', trend='stable')
    Crop.objects.create(name='Onion', current_price=2200.00, location='Chitradurga APMC', trend='down')
    Crop.objects.create(name='Paddy (Sona Masuri)', current_price=2400.00, location='Koppal APMC', trend='stable')
    Crop.objects.create(name='Ragi', current_price=3500.00, location='Tumakuru APMC', trend='up')
    Crop.objects.create(name='Maize', current_price=2100.00, location='Davanagere APMC', trend='stable')
    Crop.objects.create(name='Coconut', current_price=35.00, location='Hassan APMC', trend='stable')

    # Create Mock Schemes for Karnataka
    Scheme.objects.create(
        title='Krishi Bhagya', 
        description='Karnataka govt scheme to improve rain-fed agriculture through water conservation (Krishi Honda).', 
        eligibility='Farmers in rain-fed areas of Karnataka.\n- Subsidy for Krishi Honda\n- Diesel pumpsets provided\n- Promotes water-efficient irrigation', 
        category='pre_crop',
        link='https://raitamitra.karnataka.gov.in/'
    )
    Scheme.objects.create(
        title='Chief Minister Raitha Vidya Nidhi', 
        description='Scholarship scheme for the children of farmers in Karnataka.', 
        eligibility='Children of farmers pursuing higher education.\n- Direct bank transfer (DBT)\n- Supports professional courses\n- Encourages higher education in rural areas', 
        category='pre_crop',
        link='https://ssp.postmatric.karnataka.gov.in/'
    )
    Scheme.objects.create(
        title='Surya Raitha Scheme', 
        description='Allows farmers to install solar water pumps and sell excess electricity back to BESCOM/CESC.', 
        eligibility='Farmers with grid-connected irrigation pumps in Karnataka.\n- Reduces power dependency\n- Generates extra income\n- Subsidized solar panels', 
        category='pre_crop',
        link='https://kredlinfo.in/'
    )
    Scheme.objects.create(
        title='Pradhan Mantri Fasal Bima Yojana (PMFBY)', 
        description='Comprehensive crop insurance to protect against non-preventable natural risks.', 
        eligibility='All farmers growing notified crops.\n- Covers yield losses due to natural calamities\n- Extremely low premium rates\n- Post-harvest losses covered', 
        category='crop_loss',
        link='https://pmfby.gov.in/'
    )
    Scheme.objects.create(
        title='Karnataka Bele Vime Yojane', 
        description='State-level crop insurance program integrated with Samrakshane portal.', 
        eligibility='Farmers in Karnataka facing severe crop loss due to drought or floods.\n- Quick claim settlement\n- Localized calamity coverage\n- Linked to Bhoomi records', 
        category='crop_loss',
        link='https://samrakshane.karnataka.gov.in/'
    )

    # Create Mock Buyers across Karnataka
    Buyer.objects.create(name='MySugar Factory', company='Mysore Sugar Company', crop_interest='Sugarcane', phone_number='08232-220143')
    Buyer.objects.create(name='Tata Coffee Ltd', company='Tata Consumer Products', crop_interest='Coffee', phone_number='08274-251411')
    Buyer.objects.create(name='CAMPCO', company='Central Arecanut & Cocoa Marketing Co-op', crop_interest='Arecanut, Cocoa', phone_number='0824-2422398')
    Buyer.objects.create(name='KMF (Nandini)', company='Karnataka Milk Federation', crop_interest='Dairy, Fodder', phone_number='1800-425-2071')
    Buyer.objects.create(name='Kalaburagi Dal Mills', company='KDM', crop_interest='Tur / Pulses', phone_number='08472-220000')

    print("Database successfully seeded with pan-Karnataka data!")

if __name__ == '__main__':
    seed()
