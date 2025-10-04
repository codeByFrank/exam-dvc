import requests
import sys
import os
import argparse

def download_data(url, output_path):
    """
    Download CSV data from URL and save to specified path.
    """
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    print(f"Downloading data from: {url}")
    
    try:
        # Download file
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        
        # Save to file
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        print(f"Data successfully downloaded to: {output_path}")
        
        # Get file size
        file_size = os.path.getsize(output_path)
        print(f"File size: {file_size / 1024:.2f} KB")
        
    except requests.exceptions.RequestException as e:
        print(f"Error downloading data: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download dataset from URL')
    parser.add_argument('--url', required=True, help='URL to download data from')
    parser.add_argument('--out', required=True, help='Output path for downloaded file')
    
    args = parser.parse_args()
    download_data(args.url, args.out)