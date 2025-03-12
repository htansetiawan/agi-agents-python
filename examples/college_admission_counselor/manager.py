from __future__ import annotations

import asyncio
import time

from rich.console import Console

from agents import Runner, custom_span, gen_trace_id, trace

from .agents.university_search_agent import UniversitySearchPlan, university_search_planner
from .agents.program_finder_agent import program_finder_agent, ProgramData
from .agents.common_data_agent_fixed import common_data_agent, UniversityStats
from .agents.personalized_plan_agent_fixed import personalized_plan_agent, PersonalizedPlan
from .agents.university_profile_agent import university_profile_agent, UniversityProfile
from .agents.booklet_generator_agent import booklet_generator_agent, AdmissionBooklet
from .printer import Printer


class AdmissionCounselorManager:
    def __init__(self):
        self.console = Console()
        self.printer = Printer(self.console)

    async def run(self, student_name: str, interests: str, target_schools: str = "") -> None:
        trace_id = gen_trace_id()
        with trace("Admission Counselor trace", trace_id=trace_id):
            self.printer.update_item(
                "trace_id",
                f"View trace: https://platform.openai.com/traces/{trace_id}",
                is_done=True,
                hide_checkmark=True,
            )

            self.printer.update_item(
                "starting",
                f"Starting personalized admission counseling for {student_name}...",
                is_done=True,
                hide_checkmark=True,
            )
            
            # Step 1: Plan university searches based on student interests
            search_plan = await self._plan_university_searches(interests, target_schools)
            
            # Step 2: Find programs at each university
            program_results = await self._find_programs(search_plan)
            
            # Step 3: Gather common data set statistics for each university
            university_stats = await self._gather_university_stats(search_plan.universities)
            
            # Step 4: Create personalized plans for the student
            personalized_plans = await self._create_personalized_plans(student_name, interests, program_results)
            
            # Step 5: Generate university profiles
            university_profiles = await self._generate_university_profiles(search_plan.universities)
            
            # Step 6: Generate the final admission booklet
            booklet = await self._generate_admission_booklet(
                student_name, 
                interests, 
                program_results, 
                university_stats, 
                personalized_plans, 
                university_profiles
            )

            final_summary = f"Personalized admission booklet for {student_name}\n\n{booklet.summary}"
            self.printer.update_item("final_booklet", final_summary, is_done=True)

            self.printer.end()

        print("\n\n=====ADMISSION BOOKLET=====\n\n")
        print(f"Booklet: {booklet.markdown_content}")
        print("\n\n=====NEXT STEPS=====\n\n")
        next_steps = "\n".join(booklet.next_steps)
        print(f"Next steps: {next_steps}")

    async def _plan_university_searches(self, interests: str, target_schools: str) -> UniversitySearchPlan:
        self.printer.update_item("planning", "Planning university searches...")
        input_text = f"Student interests: {interests}"
        if target_schools:
            input_text += f"\nTarget schools: {target_schools}"
        
        result = await Runner.run(
            university_search_planner,
            input_text,
        )
        self.printer.update_item(
            "planning",
            f"Will research {len(result.final_output.universities)} universities",
            is_done=True,
        )
        return result.final_output_as(UniversitySearchPlan)

    async def _find_programs(self, search_plan: UniversitySearchPlan) -> list[ProgramData]:
        with custom_span("Finding university programs"):
            self.printer.update_item("programs", "Searching for relevant programs...")
            num_completed = 0
            tasks = [
                asyncio.create_task(self._search_programs(university, search_plan.interests)) 
                for university in search_plan.universities
            ]
            results = []
            for task in asyncio.as_completed(tasks):
                result = await task
                if result is not None:
                    results.append(result)
                num_completed += 1
                self.printer.update_item(
                    "programs", f"Searching programs... {num_completed}/{len(tasks)} completed"
                )
            self.printer.mark_item_done("programs")
            return results

    async def _search_programs(self, university: str, interests: list[str]) -> ProgramData | None:
        input_text = f"University: {university}\nInterests: {', '.join(interests)}"
        try:
            result = await Runner.run(
                program_finder_agent,
                input_text,
            )
            return result.final_output_as(ProgramData)
        except Exception as e:
            print(f"Error searching programs for {university}: {str(e)}")
            return None

    async def _gather_university_stats(self, universities: list[str]) -> list[UniversityStats]:
        with custom_span("Gathering university statistics"):
            self.printer.update_item("stats", "Gathering university statistics...")
            num_completed = 0
            tasks = [
                asyncio.create_task(self._get_university_stats(university)) 
                for university in universities
            ]
            results = []
            for task in asyncio.as_completed(tasks):
                result = await task
                if result is not None:
                    results.append(result)
                num_completed += 1
                self.printer.update_item(
                    "stats", f"Gathering statistics... {num_completed}/{len(tasks)} completed"
                )
            self.printer.mark_item_done("stats")
            return results

    async def _get_university_stats(self, university: str) -> UniversityStats | None:
        input_text = f"University: {university}"
        try:
            result = await Runner.run(
                common_data_agent,
                input_text,
            )
            return result.final_output_as(UniversityStats)
        except Exception as e:
            print(f"Error getting stats for {university}: {str(e)}")
            return None

    async def _create_personalized_plans(
        self, student_name: str, interests: str, program_data: list[ProgramData]
    ) -> PersonalizedPlan:
        self.printer.update_item("planning", "Creating personalized plans...")
        input_text = (
            f"Student name: {student_name}\n"
            f"Interests: {interests}\n"
            f"Program data: {[p.model_dump() for p in program_data]}"
        )
        result = await Runner.run(
            personalized_plan_agent,
            input_text,
        )
        self.printer.update_item(
            "planning",
            "Personalized plans created",
            is_done=True,
        )
        return result.final_output_as(PersonalizedPlan)

    async def _generate_university_profiles(self, universities: list[str]) -> list[UniversityProfile]:
        with custom_span("Generating university profiles"):
            self.printer.update_item("profiles", "Generating university profiles...")
            num_completed = 0
            tasks = [
                asyncio.create_task(self._get_university_profile(university)) 
                for university in universities
            ]
            results = []
            for task in asyncio.as_completed(tasks):
                result = await task
                if result is not None:
                    results.append(result)
                num_completed += 1
                self.printer.update_item(
                    "profiles", f"Generating profiles... {num_completed}/{len(tasks)} completed"
                )
            self.printer.mark_item_done("profiles")
            return results

    async def _get_university_profile(self, university: str) -> UniversityProfile | None:
        input_text = f"University: {university}"
        try:
            result = await Runner.run(
                university_profile_agent,
                input_text,
            )
            return result.final_output_as(UniversityProfile)
        except Exception as e:
            print(f"Error getting profile for {university}: {str(e)}")
            return None

    async def _generate_admission_booklet(
        self,
        student_name: str,
        interests: str,
        program_data: list[ProgramData],
        university_stats: list[UniversityStats],
        personalized_plans: PersonalizedPlan,
        university_profiles: list[UniversityProfile],
    ) -> AdmissionBooklet:
        self.printer.update_item("booklet", "Generating admission booklet...")
        input_text = (
            f"Student name: {student_name}\n"
            f"Interests: {interests}\n"
            f"Program data: {[p.model_dump() for p in program_data]}\n"
            f"University stats: {[s.model_dump() for s in university_stats]}\n"
            f"Personalized plans: {personalized_plans.model_dump()}\n"
            f"University profiles: {[p.model_dump() for p in university_profiles]}"
        )
        
        result = Runner.run_streamed(
            booklet_generator_agent,
            input_text,
        )
        
        update_messages = [
            "Generating admission booklet...",
            "Creating introduction...",
            "Compiling university information...",
            "Formatting personalized plans...",
            "Adding statistics and requirements...",
            "Finalizing design and layout...",
            "Completing the booklet...",
        ]

        last_update = time.time()
        next_message = 0
        async for _ in result.stream_events():
            if time.time() - last_update > 5 and next_message < len(update_messages):
                self.printer.update_item("booklet", update_messages[next_message])
                next_message += 1
                last_update = time.time()

        self.printer.mark_item_done("booklet")
        return result.final_output_as(AdmissionBooklet)
