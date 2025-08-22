# test_api.py
# Test API calls to debug 422 errors

import requests
import json

def test_api_endpoints():
    """Test API endpoints"""
    
    base_url = "http://localhost:8000"
    
    # Test 1: Root endpoint
    print("🧪 Test 1: Root endpoint...")
    try:
        response = requests.get(f"{base_url}/")
        print(f"✅ Status: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 2: Health endpoint
    print("\n🧪 Test 2: Health endpoint...")
    try:
        response = requests.get(f"{base_url}/health")
        print(f"✅ Status: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 3: Create user
    print("\n🧪 Test 3: Create user...")
    user_data = {
        "username": "testuser2",
        "email": "test2@example.com",
        "password": "password123",
        "first_name": "Test",
        "last_name": "User"
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/users/",
            headers={"Content-Type": "application/json"},
            json=user_data
        )
        print(f"Status: {response.status_code}")
        
        if response.status_code == 201:
            print(f"✅ User created successfully!")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Error creating user")
            print(f"   Response: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("Make sure your server is running on http://localhost:8000")
    print("Run 'python main.py' in another terminal first")
    print()
    test_api_endpoints()