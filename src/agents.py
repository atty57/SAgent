from crewai import Agent

def create_agents(verbose=True):
    return {
        "research": Agent(
            role="Content Extractor",
            goal="Extract and structure educational content from PDFs",
            backstory="Specializes in academic text processing and identifying key concepts",
            verbose=verbose,
            allow_delegation=False,
            llm_model="ollama/llama3:8b-text-q4_K_M"
        ),
        "education": Agent(
            role="Learning Assistant",
            goal="Generate summaries and assessment materials",
            backstory="Expert in pedagogical content creation and educational assessment",
            verbose=verbose,
            llm_model="ollama/llama3:8b-text-q4_K_M"
        ),
        "planning": Agent(
            role="Schedule Optimizer",
            goal="Create personalized study plans",
            backstory="Proficient in cognitive load theory and spaced repetition techniques",
            verbose=verbose,
            llm_model="ollama/llama3:8b-text-q4_K_M"
        )
    }
