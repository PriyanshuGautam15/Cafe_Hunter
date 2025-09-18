import os
import requests
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')


@app.route('/search', methods=['POST'])
def search_cafes():
    try:
        data = request.json
        location = data.get('location')
        vibe = data.get('vibe')
        locality = data.get('locality', '')

        search_query = f"cafe {vibe} {locality} in {location}, India"

        serp_url = "https://serpapi.com/search.json"
        params = {
            "engine": "google_maps",
            "q": search_query,
            "hl": "en",
            "gl": "in",
            "api_key": SERPAPI_API_KEY
        }
        serp_response = requests.get(serp_url, params=params)
        serp_response.raise_for_status()
        serp_data = serp_response.json()

        cafes = []
        if 'local_results' in serp_data:
            for cafe_data in serp_data['local_results']:
                cafe = {
                    'name': cafe_data.get('title'),
                    'address': cafe_data.get('address'),
                    'image_url': cafe_data.get('thumbnail'),
                    'rating': cafe_data.get('rating'),
                    'reviews': cafe_data.get('reviews'),
                    'place_id': cafe_data.get('place_id'),
                }
                cafes.append(cafe)

        return jsonify({'cafes': cafes})

    except requests.exceptions.HTTPError as e:
        print(f"SerpApi request failed: {e.response.status_code} {e.response.reason}")
        return jsonify({'error': f"SerpApi Error: {e.response.reason}"}), e.response.status_code
    except Exception as e:
        print(f"An unexpected error occurred with SerpApi: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500


@app.route('/details', methods=['POST'])
def get_cafe_details():
    try:
        data = request.json
        place_id = data.get('placeId')

        serp_url = "https://serpapi.com/search.json"
        params = {
            "engine": "google_maps_reviews",
            "place_id": place_id,
            "hl": "en",
            "gl": "in",
            "api_key": SERPAPI_API_KEY
        }
        serp_response = requests.get(serp_url, params=params)
        serp_response.raise_for_status()
        serp_data = serp_response.json()

        # Consolidate all the necessary details from the API response
        cafe_details = {
            'name': serp_data.get('place_info', {}).get('title', 'Unnamed Cafe'),
            'address': serp_data.get('place_info', {}).get('address', 'Address not available.'),
            'rating': serp_data.get('place_info', {}).get('rating', 'N/A'),
            'review_count': serp_data.get('place_info', {}).get('reviews', 0),
            'reviews': serp_data.get('reviews', []),
            'image_url': serp_data.get('place_info', {}).get('thumbnail', ''),
            'website': serp_data.get('place_info', {}).get('website', ''),
            'phone': serp_data.get('place_info', {}).get('phone', ''),
            'overview': serp_data.get('place_info', {}).get('description', 'No overview available.'),
        }

        return jsonify({'cafe': cafe_details})

    except requests.exceptions.HTTPError as e:
        print(f"SerpApi request failed: {e.response.status_code} {e.response.reason}")
        return jsonify({'error': f"SerpApi Error: {e.response.reason}"}), e.response.status_code
    except Exception as e:
        print(f"An unexpected error occurred with SerpApi: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500


@app.route('/images', methods=['POST'])
def get_cafe_images():
    try:
        data = request.json
        cafe_name = data.get('cafeName')
        location = data.get('location')

        serp_url = "https://serpapi.com/search.json"
        params = {
            "engine": "google_images",
            "q": f"{cafe_name} interior {location}",
            "ijn": "0",
            "gl": "in",
            "api_key": SERPAPI_API_KEY
        }
        serp_response = requests.get(serp_url, params=params)
        serp_response.raise_for_status()
        serp_data = serp_response.json()

        images = []
        if 'images_results' in serp_data:
            images = [img.get('original') for img in serp_data['images_results'] if img.get('original')]

        return jsonify({'images': images[:10]})

    except requests.exceptions.HTTPError as e:
        print(f"SerpApi Images request failed: {e.response.status_code} {e.response.reason}")
        return jsonify({'error': f"SerpApi Images Error: {e.response.reason}"}), e.response.status_code
    except Exception as e:
        print(f"An unexpected error occurred with SerpApi Images: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500


@app.route('/menu', methods=['POST'])
def get_cafe_menu():
    try:
        data = request.json
        cafe_name = data.get('cafeName')
        location = data.get('location')

        serp_url = "https://serpapi.com/search.json"
        params = {
            "engine": "google_menu_highlights",
            "q": f"menu {cafe_name} in {location}",
            "hl": "en",
            "gl": "in",
            "api_key": SERPAPI_API_KEY
        }
        serp_response = requests.get(serp_url, params=params)
        serp_response.raise_for_status()
        serp_data = serp_response.json()

        menu_highlights = []
        if 'menu_highlights' in serp_data:
            menu_highlights = serp_data['menu_highlights']

        return jsonify({'menu_highlights': menu_highlights})

    except requests.exceptions.HTTPError as e:
        print(f"SerpApi Menu request failed: {e.response.status_code} {e.response.reason}")
        return jsonify({'error': f"SerpApi Menu Error: {e.response.reason}"}), e.response.status_code
    except Exception as e:
        print(f"An unexpected error occurred with SerpApi Menu: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500


if __name__ == '__main__':
    app.run(debug=True)
