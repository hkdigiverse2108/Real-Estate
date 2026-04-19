import os
import urllib.request
import ssl

# Create unverified context for https if needed
ssl._create_default_https_context = ssl._create_unverified_context

ASSETS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../frontend/public/assets"))

IMAGES = {
    # Property Heroes
    "hero-cullinan.jpg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2025/05/pexels-cottonbro-studio-6940929-scaled-aspect-ratio-480-360-scaled.jpg",
    "hero-pollards.jpg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2023/03/pexels-cottonbro-studio-7222179-1920x1280.jpg",
    "hero-eastley.jpg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2025/05/Eastley-End-House-xl-aspect-ratio-1-1-2.jpg",
    "hero-meadlake.jpg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2023/03/pexels-ksenia-chernaya-3965548-1920x1280.jpg",
    
    # Featured Images (Properties / Availability section)
    "prop-cullinan.jpg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2023/03/availability-cullinan.jpg",
    "prop-pollards.jpg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2023/03/availability-pollards.jpg",
    "prop-eastley.jpg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2023/03/availability-eastley.jpg",
    "prop-meadlake.jpg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2023/03/availability-meadlake.jpg",

    # Floorplans
    "no-1-pollards-court-fp.svg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2024/11/01-Pollards-Court_floor-plan.svg",
    "no-4-pollards-court-fp.svg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2024/11/04-Pollards-Court_floor-plan.svg",
    "no-1-cullinan-fp.svg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2024/11/01-Cullinan-House_floor-plan-1.svg",
    "no-2-cullinan-fp.svg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2024/11/02-Cullinan-House_floor-plan-1.svg",
    "no-4-cullinan-fp.svg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2024/11/04-Cullinan-House_floor-plan-1.svg",
    "no-5-cullinan-fp.svg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2024/11/05-Cullinan-House_floor-plan-1.svg",
    "no-6-cullinan-fp.svg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2024/11/06-Cullinan-House_floor-plan-1.svg",
    "no-7-cullinan-fp.svg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2024/11/07-Cullinan-House_floor-plan.svg",
    "no-11-cullinan-fp.svg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2024/11/11-Cullinan-House_floor-plan.svg",
    "no-13-cullinan-fp.svg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2024/11/13-Cullinan-House_floor-plan.svg",
    "no-14-cullinan-fp.svg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2024/11/14-Cullinan-House_floor-plan.svg",
    "no-15-cullinan-fp.svg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2024/11/15-Cullinan-House_floor-plan.svg",
    "no-16-cullinan-fp.svg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2024/11/16-Cullinan-House_floor-plan.svg",
    "no-18-cullinan-fp.svg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2024/11/18-Cullinan-House_floor-plan.svg",
    "no-19-cullinan-fp.svg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2024/11/19-Cullinan-House_floor-plan.svg",
    "no-21-cullinan-fp.svg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2024/11/21-Cullinan-House_floor-plan.svg",
    "no-22-cullinan-fp.svg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2024/11/22-Cullinan-House_floor-plan.svg",
    "no-4-eastley-end-house-fp.svg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2024/11/04-Eastley-End-House_floor-plan.svg",
    "no-2-meadlake-house-fp.svg": "https://thesandars.marmikkalthiya.com/wp-content/uploads/2024/11/Meadlake-House_floor-plan.svg",
}

def download_images():
    if not os.path.exists(ASSETS_DIR):
        os.makedirs(ASSETS_DIR)
        print(f"Created directory: {ASSETS_DIR}")

    for filename, url in IMAGES.items():
        filepath = os.path.join(ASSETS_DIR, filename)
        print(f"Downloading {filename}...")
        try:
            # Add a user-agent to avoid being blocked
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                out_file.write(response.read())
            print(f"Successfully downloaded to {filepath}")
        except Exception as e:
            print(f"Failed to download {filename}: {e}")

if __name__ == "__main__":
    download_images()
