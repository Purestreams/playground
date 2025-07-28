import os
import requests

# --- Configuration ---
BASE_URL = "https://www.kodeclubs.com/"
ASSETS = {
    "index.html": "",
    "main.js": "assets/js/",
    "three.module.min.js": "assets/js/libs/",
    "gsap.min.js": "assets/js/libs/",
    "kodeclubs-logo.glb": "assets/models/"
}
OUTPUT_DIR = "kodeclubs_scene"

# --- Main Script ---
def download_file(url, local_path):
    """Downloads a file from a URL to a local path."""
    try:
        print(f"Downloading {url}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        
        with open(local_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Saved to {local_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")

def main():
    """Main function to download all assets."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created directory: {OUTPUT_DIR}")

    for filename, remote_path in ASSETS.items():
        url = f"{BASE_URL}{remote_path}{filename}"
        local_path = os.path.join(OUTPUT_DIR, remote_path, filename)
        download_file(url, local_path)
        
    print("\nDownload complete.")
    print(f"To view the scene, you may need to run a local web server in the '{OUTPUT_DIR}' directory.")
    print("For example, using Python: python -m http.server")


if __name__ == "__main__":
    main()