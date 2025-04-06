from crewai import Task

def create_tasks(pdf_content, agents):
    research_task = Task(
        description=f"Extract key concepts and organize into structured content: {pdf_content['structured_content']}",
        expected_output="Markdown with headings and key points",
        agent=agents["research"]
    )

    study_task = Task(
        description="Create summaries, quiz questions and definitions for the structured content",
        expected_output="Study guide with summaries and quiz",
        agent=agents["education"],
        context=[research_task]
    )

    planning_task = Task(
        description="Create a study schedule using spaced repetition for the study guide",
        expected_output="A detailed calendar study plan",
        agent=agents["planning"],
        context=[study_task]
    )

    return [research_task, study_task, planning_task]
