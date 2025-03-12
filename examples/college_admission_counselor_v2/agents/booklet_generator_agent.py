from typing import List
from pydantic import BaseModel, Field

from agents import Agent

PROMPT = (
    "You are an expert college admission booklet designer. Given a student's information, program data, university "
    "statistics, personalized plans, and university profiles, create a comprehensive, personalized admission booklet. "
    "The booklet should be professionally formatted in markdown and include all the information a student needs for "
    "their college application journey. Structure the booklet with clear sections, an executive summary, and visually "
    "appealing formatting. Make it feel like a premium, personalized guide created specifically for this student. "
    "Include a cover page, table of contents, and organize the information in a logical flow that makes it easy for "
    "the student to navigate and use. The final output should be in markdown format and be comprehensive, detailed, "
    "and professional - similar to what a top university would produce for their marketing materials."
)


class AdmissionBooklet(BaseModel):
    student_name: str = Field(description="The name of the student")
    summary: str = Field(description="A brief executive summary of the booklet's contents")
    markdown_content: str = Field(description="The complete booklet content in markdown format")
    next_steps: List[str] = Field(description="Recommended next steps for the student")


booklet_generator_agent = Agent(
    name="BookletGeneratorAgent",
    instructions=PROMPT,
    model="gpt-4o",
    output_type=AdmissionBooklet,
)
