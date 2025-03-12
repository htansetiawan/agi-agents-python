# College Admission Counselor

This example demonstrates an agentic flow that helps admission counselors provide students with personalized college admission booklets. The system uses multiple specialized agents to gather information, analyze data, and generate a comprehensive, personalized guide for students.

## Overview

The College Admission Counselor creates personalized booklets by:

1. Searching for universities that match a student's academic interests
2. Finding relevant programs at each university
3. Gathering admission statistics and requirements from Common Data Sets
4. Creating personalized plans including testing calendars, recommended books, activities, etc.
5. Generating detailed university profiles with history, culture, and unique features
6. Compiling all information into a professionally formatted admission booklet

## Agents

The system uses six specialized agents working together:

1. **University Search Agent**: Identifies universities that match the student's interests
2. **Program Finder Agent**: Researches specific academic programs at each university
3. **Common Data Agent**: Gathers admission statistics and requirements
4. **Personalized Plan Agent**: Creates customized plans for testing, activities, etc.
5. **University Profile Agent**: Generates detailed profiles of each university
6. **Booklet Generator Agent**: Compiles all information into a cohesive, personalized booklet

## How to Use

1. Run the main script:
   ```
   python -m examples.college_admission_counselor.main
   ```

2. Enter the student's information when prompted:
   - Student name
   - Academic interests (comma separated)
   - Target schools (optional, comma separated)

3. The system will:
   - Display progress in real-time
   - Generate a comprehensive admission booklet
   - Present the final booklet in markdown format
   - Provide recommended next steps

## Output

The final output is a professionally formatted admission booklet that includes:

- Executive summary
- University profiles with history, culture, and unique features
- Program details tailored to the student's interests
- Admission statistics and requirements
- Personalized plans for testing, activities, and application timeline
- Recommended books, events, internships, and competitions
- Next steps for the application process

This example demonstrates how multiple specialized agents can work together to create a comprehensive, personalized solution that would typically require significant manual effort from admission counselors.
