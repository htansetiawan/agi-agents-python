from typing import List
from pydantic import BaseModel, Field

from agents import Agent

PROMPT = (
    "You are a university admission expert. Given a student's academic interests and optional target schools, "
    "identify the most suitable universities for the student to apply to. If target schools are provided, "
    "include them in your recommendations. If not, recommend universities based solely on the student's interests. "
    "For each university, provide a brief reason why it's a good match for the student's interests."
)


class UniversitySearchPlan(BaseModel):
    universities: List[str] = Field(
        description="A list of universities that match the student's interests"
    )
    interests: List[str] = Field(
        description="The student's academic interests broken down into specific areas"
    )
    reasons: List[str] = Field(
        description="Reasons why each university is a good match for the student's interests. "
        "The order should match the universities list."
    )


university_search_planner = Agent(
    name="UniversitySearchPlanner",
    instructions=PROMPT,
    model="gpt-4o",
    output_type=UniversitySearchPlan,
)
