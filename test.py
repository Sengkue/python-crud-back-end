# test.py
# Simple test to verify basic installation

try:
    from fastapi import FastAPI # type: ignore
    print("✅ FastAPI imported successfully")
    
    import uvicorn # type: ignore
    print("✅ Uvicorn imported successfully")
    
    import sqlalchemy
    print("✅ SQLAlchemy imported successfully")
    
    import psycopg2
    print("✅ psycopg2 imported successfully")
    
    from dotenv import load_dotenv
    print("✅ python-dotenv imported successfully")
    
    print("\n🎉 All basic dependencies are working!")
    print("You can now run the main application.")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Please install the missing package.")

# Test basic FastAPI app
try:
    app = FastAPI()
    
    @app.get("/")
    def read_root():
        return {"message": "FastAPI is working!"}
    
    print("✅ FastAPI app created successfully")
    print("Run with: uvicorn test:app --reload")
    
except Exception as e:
    print(f"❌ Error creating FastAPI app: {e}")