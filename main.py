# main.py
from fastapi import FastAPI, HTTPException # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from contextlib import asynccontextmanager
from config.database import engine, Base
from routes.user_routes import router as user_router
import uvicorn # type: ignore

# Create tables
def create_tables():
    """Create database tables"""
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully!")
    except Exception as e:
        print(f"❌ Error creating tables: {e}")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 Starting up...")
    create_tables()
    yield
    # Shutdown
    print("🛑 Shutting down...")

# Create FastAPI app
app = FastAPI(
    title="FindLove User API",
    description="A complete CRUD API for user management with PostgreSQL",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(user_router)

# Root endpoint
@app.get("/")
def read_root():
    return {
        "message": "Welcome to FindLove User API",
        "version": "1.0.0",
        "endpoints": {
            "users": "/api/users",
            "docs": "/docs",
            "redoc": "/redoc"
        }
    }

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "API is running"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )