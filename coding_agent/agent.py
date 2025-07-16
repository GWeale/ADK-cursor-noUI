from google.adk.agents import Agent

# this is the main agent that ADK will discover
root_agent = Agent(
    name="coding_agent",
    model="gemini-2.0-flash",
    description="A helpful coding assistant agent that can help with programming tasks.",
    instruction="You are a helpful coding assistant. You can help users with programming questions, code review, debugging, and explaining programming concepts. Be clear, concise, and provide practical examples when helpful."
) 