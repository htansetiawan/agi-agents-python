from pydantic import BaseModel, Field
from typing import List

from agents import Agent

PROMPT = (
    "You are an expert college admission counselor. Given a student's name, interests, and program data from various "
    "universities, create a comprehensive personalized plan to help the student prepare for college applications. "
    "The plan should include: a standardized testing calendar with recommended test dates, suggested books to read "
    "that align with their interests and strengthen their application, recommended extracurricular activities, "
    "relevant events to attend, non-profit opportunities, internship possibilities, and academic competitions "
    "that would enhance their application. Make sure all recommendations are specific, actionable, and tailored "
    "to the student's interests and the programs they're considering."
)


class BookRecommendation(BaseModel):
    title: str = Field(description="Book title")
    author: str = Field(description="Book author")
    reason: str = Field(description="Reason for recommendation")


class Activity(BaseModel):
    name: str = Field(description="Name of the activity")
    description: str = Field(description="Brief description")
    benefit: str = Field(description="How it benefits the application")


class PersonalizedPlan(BaseModel):
    student_name: str = Field(description="The name of the student")
    test_dates: List[str] = Field(description="Recommended standardized test dates")
    books: List[BookRecommendation] = Field(description="Recommended books to read")
    activities: List[Activity] = Field(description="Recommended extracurricular activities")
    events: List[str] = Field(description="Relevant events to attend")
    nonprofit_opportunities: List[str] = Field(description="Non-profit and volunteer opportunities")
    internships: List[str] = Field(description="Potential internship opportunities")
    competitions: List[str] = Field(description="Academic competitions to consider")
    timeline: List[str] = Field(description="Application timeline with key milestones")


personalized_plan_agent = Agent(
    name="PersonalizedPlanAgent",
    instructions=PROMPT,
    model="gpt-4o",
    output_type=PersonalizedPlan,
)
