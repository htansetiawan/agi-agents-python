from pydantic import BaseModel, Field
from typing import List, Optional

from agents import Agent, WebSearchTool
from agents.model_settings import ModelSettings

INSTRUCTIONS = (
    "You are a university data specialist. Given a university name, search for and compile key statistics "
    "and admissions data from the university's Common Data Set (CDS) and other reliable sources. Focus on "
    "admission requirements, acceptance rates, standardized test scores (SAT/ACT), GPA requirements, "
    "application deadlines, and other factors important in the admissions process. Also include information "
    "about financial aid, scholarships, and cost of attendance. Provide accurate, up-to-date information "
    "that would be valuable for a prospective student's application strategy."
)


class UniversityStats(BaseModel):
    university_name: str = Field(description="The name of the university")
    acceptance_rate: str = Field(description="The university's acceptance rate")
    sat_range: str = Field(description="Middle 50% range for SAT scores")
    act_range: str = Field(description="Middle 50% range for ACT scores")
    gpa_info: str = Field(description="GPA requirements or average GPA of admitted students")
    important_factors: List[str] = Field(description="Factors considered important in the admission process")
    application_deadlines: str = Field(description="Key application deadlines for different admission plans")
    financial_aid_info: str = Field(description="Financial aid statistics and scholarship information")
    tuition_info: str = Field(description="Tuition and cost of attendance information")
    additional_notes: Optional[str] = Field(description="Any additional relevant information", default=None)


common_data_agent = Agent(
    name="CommonDataAgent",
    instructions=INSTRUCTIONS,
    tools=[WebSearchTool()],
    model_settings=ModelSettings(tool_choice="required"),
    output_type=UniversityStats,
)
