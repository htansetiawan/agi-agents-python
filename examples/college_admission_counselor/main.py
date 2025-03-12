import asyncio

from .manager_fixed import AdmissionCounselorManager

async def main() -> None:
    print("Welcome to the College Admission Counselor!")
    # student_name = input("Student name: ")
    # interests = input("Academic interests (comma separated): ")
    # target_schools = input("Target schools (comma separated, leave blank for auto-recommendation): ")

    student_name = "Eidee Laurel Tan"
    interests = "Economics,PPE,Music(violin)"
    target_schools = "Oxford,Harvard,Yale,MIT,UPenn,Princeton,University of Washington,University of Melbourne,National University of Singapore"
    
    manager = AdmissionCounselorManager()
    await manager.run(student_name, interests, target_schools)

if __name__ == "__main__":
    asyncio.run(main())
