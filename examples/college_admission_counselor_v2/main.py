import asyncio

from .manager import AdmissionCounselorManager


async def main() -> None:
    print("Welcome to the College Admission Counselor!")
    student_name = input("Student name: ")
    interests = input("Academic interests (comma separated): ")
    target_schools = input("Target schools (comma separated, leave blank for auto-recommendation): ")
    
    manager = AdmissionCounselorManager()
    await manager.run(student_name, interests, target_schools)


if __name__ == "__main__":
    asyncio.run(main())
