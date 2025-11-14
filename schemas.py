"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Lead schema for cleaning services lead form
class Lead(BaseModel):
    """
    Cleaning service leads
    Collection name: "lead"
    """
    name: str = Field(..., description="Full name of the customer", min_length=2)
    email: EmailStr = Field(..., description="Customer email")
    phone: str = Field(..., description="Phone number")
    address: str = Field(..., description="Service address")
    city: Optional[str] = Field(None, description="City")
    service_type: Literal[
        "Standard Cleaning",
        "Deep Cleaning",
        "Move In/Out",
        "Office Cleaning",
        "Post-Construction",
        "Carpet Cleaning"
    ] = Field(..., description="Type of service requested")
    bedrooms: Optional[int] = Field(None, ge=0, le=10, description="Number of bedrooms")
    bathrooms: Optional[int] = Field(None, ge=0, le=10, description="Number of bathrooms")
    preferred_date: Optional[str] = Field(None, description="Preferred service date (YYYY-MM-DD)")
    message: Optional[str] = Field(None, description="Additional details or instructions")
