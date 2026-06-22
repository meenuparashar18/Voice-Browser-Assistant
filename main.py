import asyncio
import os
import streamlit as st
import speech_recognition as sr
from textwrap import dedent

from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.llm.augmented_llm_openai import OpenAIAugmentedLLM
from mcp_agent.workflows.llm.augmented_llm import RequestParams

# Page config
st.set_page_config(page_title="Voice Browser MCP Agent", page_icon="🌐", layout="wide")

# Title and description
st.markdown("<h1 class='main-header'>🌐 Voice Browser MCP Agent</h1>", unsafe_allow_html=True)
st.markdown("Interact with a powerful web browsing agent using your voice or text!")

# Setup sidebar with example commands
with st.sidebar:
    st.markdown("### Example Commands")
    st.markdown("**Navigation**")
    st.markdown("- Go to google.com")
    st.markdown("**Interactions**")
    st.markdown("- Click on search bar and type MERN stack")
    st.markdown("---")
    st.caption("Note: Uses Playwright & Ollama to control a real browser.")

# Speech to Text Function
def listen_to_mic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening... Bolna shuru karo!")
        try:
            # 5 seconds tak aawaz sunega
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
            st.success("🤖 Got it! Processing your voice...")
            text = r.recognize_google(audio, language='en-US')
            return text
        except sr.WaitTimeoutError:
            st.error("Aapne kuch nahi bola. Try again!")
            return ""
        except sr.UnknownValueError:
            st.error("Oops! Mujhe aawaz samajh nahi aayi. Dubara bolo.")
            return ""
        except Exception as e:
            st.error(f"Mic Error: {str(e)}")
            return ""

# Initialize session state for query text
if 'query_text' not in st.session_state:
    st.session_state.query_text = ""

# Voice input button
if st.button("🎙️ Speak Command (Bolkar Command Do)"):
    voice_result = listen_to_mic()
    if voice_result:
        st.session_state.query_text = voice_result

# Text area linked to session state
query = st.text_area("Your Command (Aap yahan type bhi kar sakte hain)", 
                     value=st.session_state.query_text,
                     placeholder="Ask the agent to navigate to websites...")

# Initialize app and agent
if 'initialized' not in st.session_state:
    st.session_state.initialized = False
    st.session_state.mcp_app = MCPApp(name="streamlit_mcp_agent")
    st.session_state.mcp_context = None
    st.session_state.mcp_agent_app = None
    st.session_state.browser_agent = None
    st.session_state.llm = None
    st.session_state.loop = asyncio.new_event_loop()
    asyncio.set_event_loop(st.session_state.loop)
    st.session_state.is_processing = False


async def setup_agent():
    if not st.session_state.initialized:
        try:
            st.session_state.mcp_context = st.session_state.mcp_app.run()
            st.session_state.mcp_agent_app = await st.session_state.mcp_context.__aenter__()
            
            st.session_state.browser_agent = Agent(
                name="browser",
                instruction="""You are a helpful web browsing assistant that can interact with websites using playwright.
                    - Navigate to websites and perform browser actions (click, scroll, type)
                    - Extract information from web pages 
                    - Take screenshots of page elements when useful
                    - Provide concise summaries of web content using markdown
                    - Follow multi-step browsing sequences to complete tasks
                    
                Respond back with a status update on completing the commands.""",
                server_names=["playwright"],
            )
            
            await st.session_state.browser_agent.initialize()
            st.session_state.llm = await st.session_state.browser_agent.attach_llm(OpenAIAugmentedLLM)
            
            st.session_state.initialized = True
        except Exception as e:
            return f"Error during initialization: {str(e)}"
    return None

# Main function to run agent
async def run_mcp_agent(message):
    if not os.getenv("OPENAI_API_KEY") and not os.path.exists(
        os.path.join(os.path.dirname(__file__), "mcp_agent.secrets.yaml")
    ):
        return "Error: no LLM credentials found. Check your mcp_agent.secrets.yaml file."

    try:
        error = await setup_agent()
        if error:
            return error
        
        result = await st.session_state.llm.generate_str(
            message=message, 
            request_params=RequestParams(use_history=True, maxTokens=10000)
        )
        return result
    except Exception as e:
        return f"Error: {str(e)}"

if 'is_processing' not in st.session_state:
    st.session_state.is_processing = False
if 'last_result' not in st.session_state:
    st.session_state.last_result = None

def start_run():
    st.session_state.is_processing = True

# Run Command Button
st.button(
    "🚀 Run Command",
    type="primary",
    use_container_width=True,
    disabled=st.session_state.is_processing,
    on_click=start_run,
)

if st.session_state.is_processing:
    with st.spinner("Processing your request..."):
        result = st.session_state.loop.run_until_complete(run_mcp_agent(query))
    st.session_state.last_result = result
    st.session_state.is_processing = False
    st.rerun()

if st.session_state.last_result:
    st.markdown("### Response")
    st.markdown(st.session_state.last_result)

# Footer
st.markdown("---")
st.write("Built with Streamlit, Playwright, and Ollama ❤️")