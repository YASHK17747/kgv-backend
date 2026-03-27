import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime, timezone

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

products_data = [
    # Organic Flour
    {"id": "1", "name": "Khapli Flour", "category": "Organic Flour", "price": 160, "unit": "kg", "description": "Traditional wheat variety, rich in nutrients", "image_url": "https://images.pexels.com/photos/36617918/pexels-photo-36617918.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "2", "name": "Sona Moti Flour", "category": "Organic Flour", "price": 110, "unit": "kg", "description": "Premium quality wheat flour", "image_url": "https://images.pexels.com/photos/7236215/pexels-photo-7236215.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "3", "name": "Bansi Flour", "category": "Organic Flour", "price": 90, "unit": "kg", "description": "Pure organic wheat flour", "image_url": "https://images.pexels.com/photos/5313292/pexels-photo-5313292.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "4", "name": "Raagi Flour", "category": "Organic Flour", "price": 120, "unit": "kg", "description": "Finger millet flour, high in calcium", "image_url": "https://images.pexels.com/photos/7420513/pexels-photo-7420513.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "5", "name": "Barley Flour", "category": "Organic Flour", "price": 80, "unit": "kg", "description": "Nutritious barley flour", "image_url": "https://images.pexels.com/photos/7412064/pexels-photo-7412064.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "6", "name": "Pearl Millet Flour", "category": "Organic Flour", "price": 60, "unit": "kg", "description": "Bajra flour, rich in iron", "image_url": "https://images.pexels.com/photos/7420513/pexels-photo-7420513.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    
    # Pulses
    {"id": "7", "name": "Moong", "category": "Pulses", "price": 230, "unit": "kg", "description": "Whole green gram", "image_url": "https://images.pexels.com/photos/7334141/pexels-photo-7334141.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "8", "name": "Moong Chhilka", "category": "Pulses", "price": 235, "unit": "kg", "description": "Split green gram with skin", "image_url": "https://images.unsplash.com/photo-1763368392508-3d4bddfdd20a?q=85", "in_stock": True},
    {"id": "9", "name": "Moong Dhuli", "category": "Pulses", "price": 240, "unit": "kg", "description": "Washed split green gram", "image_url": "https://images.unsplash.com/photo-1708521204851-a45e56681d83?q=85", "in_stock": True},
    {"id": "10", "name": "Arhar/Toor", "category": "Pulses", "price": 265, "unit": "kg", "description": "Pigeon pea, protein-rich", "image_url": "https://images.unsplash.com/photo-1612504258838-fbf14fe4437d?q=85", "in_stock": True},
    {"id": "11", "name": "Channa", "category": "Pulses", "price": 150, "unit": "kg", "description": "Whole chickpeas", "image_url": "https://images.pexels.com/photos/5425012/pexels-photo-5425012.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "12", "name": "Channa Dal", "category": "Pulses", "price": 170, "unit": "kg", "description": "Split chickpeas", "image_url": "https://images.pexels.com/photos/618491/pexels-photo-618491.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "13", "name": "Besan", "category": "Pulses", "price": 180, "unit": "kg", "description": "Gram flour, versatile ingredient", "image_url": "https://images.pexels.com/photos/5313292/pexels-photo-5313292.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    
    # Rice
    {"id": "14", "name": "Basmati 1121 (Unpolished)", "category": "Rice", "price": 185, "unit": "kg", "description": "Premium unpolished basmati rice", "image_url": "https://images.unsplash.com/photo-1686820740687-426a7b9b2043?q=85", "in_stock": True},
    
    # Honey & Sweets
    {"id": "15", "name": "Mustard Honey", "category": "Honey & Sweets", "price": 585, "unit": "kg", "description": "Pure raw mustard honey", "image_url": "https://images.pexels.com/photos/5634210/pexels-photo-5634210.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "16", "name": "Multiflora Honey", "category": "Honey & Sweets", "price": 650, "unit": "kg", "description": "Multi-flower raw honey", "image_url": "https://images.pexels.com/photos/5634211/pexels-photo-5634211.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "17", "name": "Jaggery", "category": "Honey & Sweets", "price": 150, "unit": "kg", "description": "Traditional natural sweetener", "image_url": "https://images.pexels.com/photos/6998567/pexels-photo-6998567.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "18", "name": "Jaggery Powder", "category": "Honey & Sweets", "price": 155, "unit": "kg", "description": "Powdered jaggery for easy use", "image_url": "https://images.pexels.com/photos/4438230/pexels-photo-4438230.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "19", "name": "Desi Khaand", "category": "Honey & Sweets", "price": 185, "unit": "kg", "description": "Organic unrefined sugar", "image_url": "https://images.pexels.com/photos/4438230/pexels-photo-4438230.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "20", "name": "Amla Candy", "category": "Honey & Sweets", "price": 360, "unit": "kg", "description": "Sweet and tangy amla preserve", "image_url": "https://images.unsplash.com/photo-1773957949154-a7d1ef35ae76?q=85", "in_stock": True},
    
    # Pickles
    {"id": "21", "name": "Lemon Pickle", "category": "Pickles", "price": 150, "unit": "500g", "description": "Traditional spicy lemon pickle", "image_url": "https://images.pexels.com/photos/5865194/pexels-photo-5865194.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "22", "name": "Amla Pickle", "category": "Pickles", "price": 150, "unit": "500g", "description": "Tangy Indian gooseberry pickle", "image_url": "https://images.pexels.com/photos/5719608/pexels-photo-5719608.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "23", "name": "Amla Murabba", "category": "Pickles", "price": 450, "unit": "kg", "description": "Sweet amla preserve", "image_url": "https://images.pexels.com/photos/5865194/pexels-photo-5865194.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    
    # Groceries
    {"id": "24", "name": "Sendha Salt", "category": "Groceries", "price": 100, "unit": "kg", "description": "Rock salt, pure and natural", "image_url": "https://images.pexels.com/photos/2802527/pexels-photo-2802527.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "25", "name": "Kaala Bagh Namak", "category": "Groceries", "price": 110, "unit": "kg", "description": "Black salt with distinctive flavor", "image_url": "https://images.pexels.com/photos/1340116/pexels-photo-1340116.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "26", "name": "Haldi Powder", "category": "Groceries", "price": 440, "unit": "kg", "description": "Pure turmeric powder", "image_url": "https://images.pexels.com/photos/1340116/pexels-photo-1340116.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "27", "name": "Moringa Powder", "category": "Groceries", "price": 100, "unit": "100g", "description": "Nutrient-rich drumstick leaf powder", "image_url": "https://images.pexels.com/photos/2802527/pexels-photo-2802527.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "28", "name": "Red Chilli Powder", "category": "Groceries", "price": 300, "unit": "500g", "description": "Spicy red chilli powder", "image_url": "https://images.pexels.com/photos/1340116/pexels-photo-1340116.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "29", "name": "Jeera", "category": "Groceries", "price": 400, "unit": "500g", "description": "Premium cumin seeds", "image_url": "https://images.pexels.com/photos/2802527/pexels-photo-2802527.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "30", "name": "Mustard Seeds", "category": "Groceries", "price": 75, "unit": "500g", "description": "Fresh mustard seeds", "image_url": "https://images.pexels.com/photos/1340116/pexels-photo-1340116.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "31", "name": "Methi Seeds", "category": "Groceries", "price": 125, "unit": "500g", "description": "Fenugreek seeds", "image_url": "https://images.pexels.com/photos/2802527/pexels-photo-2802527.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    
    # Oils & Ghee
    {"id": "32", "name": "Mustard Oil", "category": "Oils & Ghee", "price": 340, "unit": "L", "description": "Cold-pressed mustard oil", "image_url": "https://images.pexels.com/photos/6914569/pexels-photo-6914569.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "33", "name": "Yellow Mustard Oil", "category": "Oils & Ghee", "price": 410, "unit": "L", "description": "Premium yellow mustard oil", "image_url": "https://images.pexels.com/photos/5590955/pexels-photo-5590955.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "34", "name": "Groundnut Oil", "category": "Oils & Ghee", "price": 440, "unit": "L", "description": "Cold-pressed groundnut oil", "image_url": "https://images.pexels.com/photos/6914569/pexels-photo-6914569.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "35", "name": "Sesame Oil", "category": "Oils & Ghee", "price": 630, "unit": "L", "description": "Pure sesame oil", "image_url": "https://images.pexels.com/photos/5590955/pexels-photo-5590955.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "36", "name": "A2 Vedic Bilona Ghee", "category": "Oils & Ghee", "price": 2000, "unit": "L", "description": "Traditional hand-churned ghee from A2 milk", "image_url": "https://images.unsplash.com/photo-1692261666975-0756bf5582be?q=85", "in_stock": True},
    
    # Others
    {"id": "37", "name": "Multani Mitti Soap", "category": "Others", "price": 70, "unit": "piece", "description": "Natural fuller's earth soap", "image_url": "https://images.pexels.com/photos/5865194/pexels-photo-5865194.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
    {"id": "38", "name": "Triphala Powder", "category": "Others", "price": 100, "unit": "200g", "description": "Ayurvedic herbal powder", "image_url": "https://images.pexels.com/photos/2802527/pexels-photo-2802527.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "in_stock": True},
]

blog_posts_data = [
    {
        "id": "blog-1",
        "title": "The Wisdom of Bhagavad Gita in Modern Farming",
        "slug": "wisdom-bhagavad-gita-modern-farming",
        "excerpt": "Discover how Chapter 18 of the Shreemad Bhagavad Gita guides our farming philosophy at KGV Organics.",
        "content": "In Chapter 18 of the Shreemad Bhagavad Gita, Shri Krishna speaks about the duties of different varnas. For farmers and traders, He emphasizes three core principles: Krishi (agriculture that nourishes), Gauraksha (protection of nature and resources), and Vanijya (ethical commerce). At KGV Organics Farm, these timeless teachings form the foundation of everything we do. We cultivate our crops without chemicals, honor and protect natural resources, and trade with complete transparency and fairness. This ancient wisdom is not just philosophy—it's our daily practice.",
        "author": "KGV Organics Farm",
        "published_at": datetime.now(timezone.utc).isoformat(),
        "tags": ["Philosophy", "Organic Farming", "Bhagavad Gita"]
    },
    {
        "id": "blog-2",
        "title": "Why Traditional Organic Farming is Superior",
        "slug": "traditional-organic-farming-superior",
        "excerpt": "Learn about the benefits of traditional farming methods and how they create healthier soil and crops.",
        "content": "Traditional organic farming is an integral part of Indian agriculture. Natural composting and organic fertilizers enrich the soil with beneficial microorganisms. Unlike chemical fertilizers that deplete soil health over time, natural inputs create a living, breathing ecosystem underground. This results in crops that are not only free from harmful chemicals but also richer in minerals and nutrients. At KGV Organics, our entire farming cycle revolves around these time-tested practices, ensuring that every grain and vegetable we produce carries the blessing of this ancient wisdom.",
        "author": "KGV Organics Farm",
        "published_at": datetime.now(timezone.utc).isoformat(),
        "tags": ["Traditional Farming", "Organic", "Sustainable Agriculture"]
    },
    {
        "id": "blog-3",
        "title": "Chemical-Free Harvest: Our Promise to You",
        "slug": "chemical-free-harvest-promise",
        "excerpt": "Understanding our zero-chemical approach and what it means for your family's health.",
        "content": "In today's world, the word 'organic' is often misused. At KGV Organics Farm, we go beyond labels. Our zero-chemical promise means that from seed to harvest, not a single synthetic pesticide, fertilizer, or growth hormone touches our crops. We use only traditional methods—neem extracts, cow-based fertilizers, and companion planting—to protect and nourish our fields. This commitment ensures that what reaches your plate is pure, safe, and full of natural vitality. Your family deserves nothing less.",
        "author": "KGV Organics Farm",
        "published_at": datetime.now(timezone.utc).isoformat(),
        "tags": ["Health", "Zero Chemical", "Organic"]
    },
]

async def seed_database():
    print("Clearing existing data...")
    await db.products.delete_many({})
    await db.blog_posts.delete_many({})
    
    print("Seeding products...")
    await db.products.insert_many(products_data)
    print(f"Inserted {len(products_data)} products")
    
    print("Seeding blog posts...")
    await db.blog_posts.insert_many(blog_posts_data)
    print(f"Inserted {len(blog_posts_data)} blog posts")
    
    print("Database seeding complete!")
    client.close()

if __name__ == "__main__":
    asyncio.run(seed_database())