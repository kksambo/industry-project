import os
from fastapi import FastAPI, HTTPException, Depends, Form
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI
app = FastAPI()

# Database setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Traveller model
class Traveller(Base):
    __tablename__ = "travellers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)
    securityQuestion = Column(String, index=True)
    securityAnswer = Column(String, index=True)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (adjust in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Pydantic models for creating a traveller and login
class TravellerCreate(BaseModel):
    name: str
    surname: str
    email: str
    password: str
    securityQuestion: str
    securityAnswer: str

class TravellerLogin(BaseModel):
    email: str
    password: str

class ChangePassword(BaseModel):
    email: str
    securityQuestion: str
    securityAnswer: str
    newPassword: str   


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to create a new traveller
@app.post("/travellers/", response_model=None)
def create_item(traveller: TravellerCreate, db: Session = Depends(get_db)):
    new_traveller = Traveller(
        name=traveller.name,
        surname=traveller.surname,
        email=traveller.email,
        password=traveller.password,  
        securityQuestion=traveller.securityQuestion,
        securityAnswer=traveller.securityAnswer
    )
    db.add(new_traveller)
    db.commit()
    db.refresh(new_traveller)
    return new_traveller

# Route for changing password
@app.post("/changePassword/", response_model=None)
def change_password(change_password: ChangePassword, db: Session = Depends(get_db)):
    traveller = db.query(Traveller).filter(Traveller.email == change_password.email).first()
    if not traveller:
        raise HTTPException(status_code=404, detail="Traveller not found")
    
    if traveller.securityQuestion != change_password.securityQuestion or traveller.securityAnswer != change_password.securityAnswer:
        raise HTTPException(status_code=401, detail="Invalid security question or answer")
    
    traveller.password = change_password.newPassword
    db.commit()
    db.refresh(traveller)
    return {"message": "Password changed successfully"}



# Route for traveller login
@app.post("/login/", response_model=None)
def login(travellerLogin: TravellerLogin, db: Session = Depends(get_db)):
    traveller = db.query(Traveller).filter(Traveller.email == travellerLogin.email).first()
    if not traveller or traveller.password != travellerLogin.password:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return traveller

# Pydantic model for receiving trip request data
class TripRequest(BaseModel):
    destination: str
    place_description: str

# Function to generate trip details using the Gemini API
def generate_trip_details(destination: str, place_description: str) -> dict:
    prompt = f"""
    I want to travel to {destination}. The type of place I would like to visit is described as: "{place_description}".
    give me the following details: Estimated budget, Transportation Options, Accomodation, 
    Weather Forecast, Safety tips give one line answer per section, separated by mapula.
    
    """

    # Configure the Gemini API
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    if not GEMINI_API_KEY:
        raise ValueError("No GEMINI_API_KEY found. Please set it in a .env file.")
    
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")  # Updated model name

    try:
        # Generate trip information using Gemini
        response = model.generate_content([prompt])

        # Assuming the response contains line breaks between different pieces of information
        details = response.text.strip().split("\n")

        # Parsing each section of the response and organizing the details
        trip_info = {
            "budget": details[0].strip() if len(details) > 0 else "No budget info available",
            "transport_options": details[1].strip() if len(details) > 1 else "No transport options available",
            "accommodation": details[2].strip() if len(details) > 2 else "No accommodation info available",
            "weather": details[3].strip() if len(details) > 3 else "No weather info available",
            "safety_tips": details[4].strip() if len(details) > 4 else "No safety tips available"
        }

        return details

    except Exception as e:
        # Print the detailed error for debugging
        print("Error occurred while generating trip details:", str(e))
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

# Endpoint to get trip details using Pydantic model
@app.post("/get_trip_details/")
async def get_trip_details(
    trip_request: TripRequest, db: Session = Depends(get_db)
):
    try:
        # Generate the trip information from Gemini
        trip_info = generate_trip_details(trip_request.destination, trip_request.place_description)
        return trip_info
    except Exception as e:
        print(f"Error occurred: {str(e)}")  # Log error details
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

# Route to get a traveller by ID
@app.get("/traveller/{traveller_id}", response_model=None)
def read_item(traveller_id: int, db: Session = Depends(get_db)):
    traveller = db.query(Traveller).filter(Traveller.id == traveller_id).first()
    if not traveller:
        raise HTTPException(status_code=404, detail="Traveller not found")
    return traveller

# Run the app with uvicorn:
# uvicorn main:app --reload
