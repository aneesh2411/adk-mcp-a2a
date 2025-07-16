import os

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from mcp import StdioServerParameters
from elevenlabs_agent.prompt import ELEVENLABS_PROMPT
from utils.custom_adk_patches import CustomMCPToolset

from dotenv import load_dotenv
load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

def create_elevenlabs_agent() -> Agent:
    return Agent(
        name="elevenlabs_agent_mcp",
        model=LiteLlm(
            model="anthropic/claude-3-5-sonnet-20241022", 
            api_key=os.getenv("ANTHROPIC_API_KEY")
        ),  
        description="Specialized agent for converting text to speech using ElevenLabs via MCPToolset.",
        instruction=ELEVENLABS_PROMPT,
        tools=[
            CustomMCPToolset(
                connection_params=StdioServerParameters(
                    command='uvx',
                    args=['elevenlabs-mcp'], 
                    env={"ELEVENLABS_API_KEY": ELEVENLABS_API_KEY}
                )
            )
        ]
    ) 


root_agent = create_elevenlabs_agent()
