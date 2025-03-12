from pydantic import BaseModel, Field
from typing import List, Dict

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


class UniversityProfile(BaseModel):
    university_name: str = Field(
        description="The name of the university"
    )
    founding_and_history: str = Field(
        description="Brief history of the university including when it was founded and key historical moments"
    )
    notable_alumni: List[Dict[str, str]] = Field(
        description="Notable alumni with their achievements and contributions"
    )
    campus_culture: str = Field(
        description="Description of the campus culture, values, and atmosphere"
    )
    traditions: List[str] = Field(
        description="Unique traditions and events that define the university experience"
    )
    location_benefits: str = Field(
        description="Benefits of the university's location including surrounding city, region, etc."
    )
    student_life: Dict[str, str] = Field(
        description="Information about student life including clubs, organizations, activities, etc."
    )
    housing_and_dining: str = Field(
        description="Overview of housing options and dining facilities"
    )
    athletics_and_recreation: str = Field(
        description="Information about athletics programs, recreational facilities, and sports culture"
    )
    unique_features: List[str] = Field(
        description="Distinctive features that set this university apart from others"
    )
    mission_and_values: str = Field(
        description="The university's mission statement and core values"
    )


university_profile_agent = Agent(
    name="UniversityProfileAgent",
    instructions=INSTRUCTIONS,
    tools=[WebSearchTool()],
    model_settings=ModelSettings(tool_choice="required"),
    output_type=UniversityProfile,
)
