#!/usr/bin/env python3
"""
Fetch Panchang data and save to panchang/ directory
Used by GitHub Actions to update daily
"""

import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os


def fetch_panchang_data():
    """Fetch panchang data from drikpanchang.com"""
    
    BASE_URL = "https://www.drikpanchang.com/panchang/month-panchang.html"
    
    print(f"[{datetime.now().isoformat()}] Fetching panchang data...")
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(BASE_URL, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        content_div = soup.find('body')
        text_content = content_div.get_text(separator='\n') if content_div else ""
        
        panchang_dict = {}
        lines = text_content.split('\n')
        
        for line in lines:
            line = line.strip()
            if ':' in line and line and not line.startswith('http'):
                parts = line.split(':', 1)
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip()
                    if key and value and len(key) < 50:
                        panchang_dict[key] = value
        
        return panchang_dict
    
    except Exception as e:
        print(f"Error fetching panchang data: {e}")
        return {}


def save_to_json(data):
    """Save panchang data to JSON files in panchang/ directory"""
    
    # Ensure panchang directory exists
    os.makedirs('panchang', exist_ok=True)
    
    output_data = {
        "status": "success",
        "last_updated": datetime.now().isoformat(),
        "data": data,
        "count": len(data)
    }
    
    # Save to panchang/panchang.json
    panchang_path = os.path.join('panchang', 'panchang.json')
    with open(panchang_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Saved {len(data)} panchang elements to {panchang_path}")
    
    # Also save a voice-friendly version
    voice_data = {
        "status": "success",
        "last_updated": datetime.now().isoformat(),
        "voice_text": format_for_voice(data),
        "data": data
    }
    
    voice_path = os.path.join('panchang', 'panchang_voice.json')
    with open(voice_path, 'w', encoding='utf-8') as f:
        json.dump(voice_data, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Saved voice-friendly version to {voice_path}")


def format_for_voice(data):
    """Format panchang data for voice output"""
    
    elements = ["Tithi", "Nakshatra", "Yoga", "Sunrise", "Sunset"]
    voice_parts = []
    
    for element in elements:
        value = next((v for k, v in data.items() if k.lower() == element.lower()), None)
        if value:
            voice_parts.append(f"{element} is {value}")
    
    voice_text = "Today's Panchang: " + ", ".join(voice_parts)
    return voice_text


def main():
    print("\n" + "="*60)
    print("PANCHANG DATA FETCHER")
    print("="*60 + "\n")
    
    data = fetch_panchang_data()
    
    if data:
        save_to_json(data)
        print(f"\n✓ Successfully fetched and saved {len(data)} panchang elements")
        print(f"✓ Last updated: {datetime.now().isoformat()}")
        print("\n" + "="*60 + "\n")
        return 0
    else:
        print("\n✗ Failed to fetch panchang data")
        print("="*60 + "\n")
        return 1


if __name__ == "__main__":
    exit(main())
