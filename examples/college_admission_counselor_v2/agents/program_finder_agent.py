from typing import List
from pydantic import BaseModel, Field

from agents import Agent, WebSearchTool
from agents.model_settings import ModelSettings

INSTRUCTIONS = (
    "You are a university program research specialist. Given a university name and student interests, "
    "search for specific academic programs, majors, minors, and specializations at that university "
    "that align with the student's interests. Provide detailed information about each program including "
    "department, degree types offered, special features, notable faculty, research opportunities, "
    "internship connections, and any unique aspects of the program. Focus on factual information that "
    "would be valuable for a prospective student considering this university."
)


class ProgramData(BaseModel):
    university_name: str = Field(
        description="The name of the university"
    )
    matching_programs: List[str] = Field(
        description="List of programs that match the student's interests"
    )
    program_details: List[str] = Field(
        description="Detailed information about each program including requirements, features, and opportunities. "
        "The order should match the matching_programs list."
    )
    special_opportunities: List[str] = Field(
        description="Special opportunities related to these programs such as research, internships, study abroad, etc."
    )


program_finder_agent = Agent(
    name="ProgramFinderAgent",
    instructions=INSTRUCTIONS,
    tools=[WebSearchTool()],
    model_settings=ModelSettings(tool_choice="required"),
    output_type=ProgramData,
)
