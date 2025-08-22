# create_tables.py
# Manual script to create database tables

from config.database import engine, Base
from models.user import User
import traceback

def create_tables():
    """Create all database tables"""
    try:
        print("🔄 Creating database tables...")
        
        # Drop all tables first (optional - uncomment if you want fresh tables)
        # Base.metadata.drop_all(bind=engine)
        # print("🗑️ Dropped existing tables")
        
        # Create all tables
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully!")
        
        # Verify table creation
        from sqlalchemy import inspect
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print(f"📋 Created tables: {tables}")
        
        if 'users' in tables:
            print("✅ Users table created successfully!")
            # Get table columns
            columns = inspector.get_columns('users')
            print("📝 Users table columns:")
            for col in columns:
                print(f"   - {col['name']}: {col['type']}")
        else:
            print("❌ Users table was not created!")
            
    except Exception as e:
        print(f"❌ Error creating tables: {e}")
        print("Full error:")
        traceback.print_exc()

if __name__ == "__main__":
    create_tables()