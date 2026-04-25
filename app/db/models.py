from sqlmodel import SQLModel, Field
from typing import Optional,Dict
from datetime import datetime
from sqlalchemy import Column,  DateTime,JSON,Text
from sqlalchemy.sql import func
from pydantic import BaseModel


class ScriptBase(SQLModel):
    """
    Common fields -- shared between create and response
    """
    topic: str = Field(
        max_length=500,
        index=True
    )
    tone: str = Field(
        max_length=100,
    )
    script: Dict = Field(
        sa_column=Column(JSON)
    )
    sources: Optional[str]= Field(
        default=None,
        sa_column=Column(Text)
    )
    quality_score: Optional[float] = None

    formatted_script: Optional[str] =  Field(
        default=None,
        sa_column=Column(Text)
    )
    hashtags: Optional[str] = Field(
        default=None,
        sa_column=Column(Text)
    )

class Script(ScriptBase, table=True):
    """
    Actual MySQL table
    """
    __tablename__ = "scripts"

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime, default=func.now(), onupdate=func.now())
    ) 

class ScriptCreate(ScriptBase):
    """
    POST request ke liye -- user yeh bhejega
    """
    pass

class ScriptResponse(ScriptBase):
    """
    Response ke liye -- yeh user ko milega
    """
    id: int
    created_at: datetime
    updated_at: datetime

class ScriptGenerateRequest(BaseModel):
    topic: str
    tone: str