"""
Database Models for Events

Defines the Event model for tracking user accomplishments,
challenges, and milestones in the Heavenly Archive system.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base
import enum


class EventCategory(str, enum.Enum):
    """Event categories inspired by celestial hierarchy"""
    VIRTUE = "virtue"  # Good deeds and accomplishments
    TRIAL = "trial"  # Challenges and difficulties
    VICTORY = "victory"  # Major wins and successes
    LEGENDARY = "legendary"  # Epic achievements
    DIVINE = "divine"  # Extraordinary milestones
    MORTAL = "mortal"  # Daily activities


class EventImportance(str, enum.Enum):
    """Importance levels for events"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
    LEGENDARY = "legendary"


class Event(Base):
    """Event model for tracking user activities and achievements"""
    
    __tablename__ = "events"
    
    # Primary Key
    id = Column(Integer, primary_key=True, index=True)
    
    # Basic Information
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    category = Column(Enum(EventCategory), nullable=False, index=True)
    importance = Column(Enum(EventImportance), default=EventImportance.MEDIUM)
    
    # Metadata
    tags = Column(Text, nullable=True)  # Comma-separated tags
    location = Column(String(255), nullable=True)
    related_url = Column(String(512), nullable=True)
    
    # Timestamps
    event_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    # user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    # user = relationship("User", back_populates="events")
    
    def __repr__(self):
        return f"<Event(id={self.id}, title='{self.title}', category='{self.category.value}')>"
    
    def to_dict(self):
        """Convert event to dictionary"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category.value,
            "importance": self.importance.value,
            "tags": self.tags.split(",") if self.tags else [],
            "location": self.location,
            "related_url": self.related_url,
            "event_date": self.event_date.isoformat() if self.event_date else None,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
