from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import contact  # Import your contact router
from api import phone_numbers  # Import your phone numbers router

app = FastAPI()

# Allow frontend (React dev server) to communicate with the backend
origins = [
    "http://localhost:3000",  # React default dev server
    # "https://your-production-domain.com",  # Add production domain here later
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include the API routers
app.include_router(contact.router, prefix="/api", tags=["contacts"])
app.include_router(phone_numbers.router, prefix="/api", tags=["phone_numbers"])

# Optional: health check route
@app.get("/")
async def root():
    return {"message": "API is running"}
