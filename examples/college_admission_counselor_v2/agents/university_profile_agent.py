from typing import List, Dict
from pydantic import BaseModel, Field

from agents import Agent, WebSearchTool
from agents.model_settings import ModelSettings

INSTRUCTIONS = (
    "You are a university profiling specialist. Given a university name, create a comprehensive profile "
    "that captures the essence of the institution. Include the university's history, notable alumni, "
    "campus culture, values, traditions, location advantages, student life, housing options, dining, "
    "athletics, and other distinctive features. Focus on creating content that resembles high-quality "
    "marketing materials that top universities produce. Be factual but also highlight what makes this "
    "university special and unique. The profile should help a prospective student understand what it "
    "would be like to attend this university."
)


class Alumni(BaseModel):
    name: str = Field(description="Name of the notable alumni")
    achievement: str = Field(description="Their notable achievement or contribution")


class UniversityProfile(BaseModel):
    university_name: str = Field(description="The name of the university")
    history: str = Field(description="Brief history of the university")
    notable_alumni: List[Alumni] = Field(description="Notable alumni with their achievements")
    campus_culture: str = Field(description="Description of the campus culture and values")
    traditions: List[str] = Field(description="Unique traditions and events")
    location: str = Field(description="Benefits of the university's location")
    student_life: str = Field(description="Information about student life")
    housing: str = Field(description="Overview of housing options")
    dining: str = Field(description="Overview of dining facilities")
    athletics: str = Field(description="Information about athletics programs")
    unique_features: List[str] = Field(description="Distinctive features of this university")
    mission: str = Field(description="The university's mission statement and core values")


university_profile_agent = Agent(
    name="UniversityProfileAgent",
    instructions=INSTRUCTIONS,
    tools=[WebSearchTool()],
    model_settings=ModelSettings(tool_choice="required"),
    output_type=UniversityProfile,
)
