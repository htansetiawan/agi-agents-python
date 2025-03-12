from typing import List, Dict
from pydantic import BaseModel, Field

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


class Event(BaseModel):
    name: str = Field(description="Name of the event")
    date: str = Field(description="Date or timeframe if known")
    description: str = Field(description="Brief description")


class Opportunity(BaseModel):
    name: str = Field(description="Name of the opportunity")
    description: str = Field(description="Brief description")
    relevance: str = Field(description="Relevance to student's interests")


class Competition(BaseModel):
    name: str = Field(description="Name of the competition")
    deadline: str = Field(description="Deadline if known")
    description: str = Field(description="Brief description")


class TimelineItem(BaseModel):
    date: str = Field(description="Date or timeframe")
    task: str = Field(description="Task to complete")


class PersonalizedPlan(BaseModel):
    student_name: str = Field(description="The name of the student")
    test_dates: List[Dict[str, str]] = Field(description="Recommended standardized test dates")
    books: List[BookRecommendation] = Field(description="Recommended books to read")
    activities: List[Activity] = Field(description="Recommended extracurricular activities")
    events: List[Event] = Field(description="Relevant events to attend")
    nonprofit_opportunities: List[Opportunity] = Field(description="Non-profit opportunities")
    internships: List[Opportunity] = Field(description="Potential internship opportunities")
    competitions: List[Competition] = Field(description="Academic competitions to consider")
    timeline: List[TimelineItem] = Field(description="Application timeline")


personalized_plan_agent = Agent(
    name="PersonalizedPlanAgent",
    instructions=PROMPT,
    model="gpt-4o",
    output_type=PersonalizedPlan,
)
