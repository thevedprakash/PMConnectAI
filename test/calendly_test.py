import requests
from test.config import ConfigTest as Config


def generate_calendly_invitation_link():
    headers = {
        'Authorization': Config.CALENDLY_API_KEY,
        'Content-Type': 'application/json'
    }
    url = 'https://api.calendly.com/scheduling_links'
    payload = {
        "max_event_count": 1,
        "owner": f"https://api.calendly.com/event_types/{Config.CALENDLY_EVENT_UUID}",
        "owner_type": "EventType"
    }
    
    print("Headers:", headers)
    print("Payload:", payload)
    print("URL:", url)
    
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        data = response.json()
        return data['resource']['booking_url']
    else:
        print(f"Failed to create Calendly link: {response.status_code}, {response.text}")
        return None

# Test the function
if __name__ == "__main__":
    link = generate_calendly_invitation_link()
    if link:
        print(f"Calendly invitation link created: {link}")
    else:
        print("Failed to create Calendly invitation link.")