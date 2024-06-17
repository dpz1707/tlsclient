import tls_client

def get_status_code(url):
    
    session = tls_client.Session(
        client_identifier="chrome_108",  
        ja3_string=None, 
        random_tls_extension_order=True, 
    )
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        response = session.get(url, headers=headers)
        
        print(f"Status code: {response.status_code}")
        
        print(response.text[:500])  #
        
        return response.status_code
    
    except Exception as e:
        print(f"An error occurred: {e}")

url = 'https://za.investing.com/equities/microsoft-corp'
get_status_code(url)
