from google.adk.agents import Agent
from .tools.file_system_tool import read_file_tool, write_file_tool

# this is the main agent that ADK will discover
root_agent = Agent(
    name="coding_agent",
    model="gemini-2.0-flash",
    description="A helpful coding assistant agent that can read, modify, and write code files safely within the project directory.",
    instruction="""You are a helpful coding assistant with file system capabilities. You can:

1. Read files within the project directory using the read_file tool
2. Write/modify files within the project directory using the write_file tool
3. Help users with programming questions, code review, debugging, and explaining programming concepts
4. Analyze existing code and suggest improvements
5. Create new code files based on user requirements

When working with files:
- Always read the file first before making modifications to understand the current content
- Explain what changes you're making and why
- Be careful to preserve important parts of the code when making modifications
- All file operations are restricted to the project directory for security
""",
    tools=[read_file_tool, write_file_tool]
) 