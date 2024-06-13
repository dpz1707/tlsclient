import tls_client

def get_status_code(url):
    # Create a session
    session = tls_client.Session(
        client_identifier="chrome_108",  # Emulate Chrome browser
        ja3_string=None,  # Leave as default unless specific JA3 fingerprinting is required
        random_tls_extension_order=True,  # Randomize TLS extension order to mimic browser behavior
    )
    
    # Define headers to mimic a real browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    # Send GET request
    try:
        response = session.get(url, headers=headers)
        
        # Check status code
        print(f"Status code: {response.status_code}")
        
        # Print a portion of the content for verification
        print(response.text[:500])  # Print first 500 characters of the response
        
        return response.status_code
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
url = 'https://za.investing.com/equities/microsoft-corp'
get_status_code(url)
