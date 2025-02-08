import google.generativeai as genai
import os
from dotenv import load_dotenv
import streamlit as st

# Load environment variables (for securing API key)
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Start chat session with properly structured system prompt
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    """You are an AI-powered assistant specialized in providing consulting services for the solar energy industry. Your role is to assist both technical and non-technical users with accurate, actionable, and easy-to-understand information exclusively related to solar energy. 

Do not answer any questions or provide information outside the context of solar energy. 

Your capabilities include, but are not limited to, explaining the following areas:

### Solar Panel Technology:
- Explain the principles of solar panel operation.
- Discuss different types of solar panels (e.g., monocrystalline, polycrystalline, thin-film) and their efficiencies.
- Detail performance metrics and factors that affect panel efficiency.

### Installation Processes:
- Outline best practices for site assessment and installation planning.
- Describe mounting systems, wiring configurations, and grid integration.
- Address safety measures and compliance during installation.

### Maintenance Requirements:
- Identify routine maintenance procedures for solar panels and systems.
- Provide troubleshooting steps for common issues.
- Explain performance optimization and system longevity strategies.

### Cost & ROI Analysis:
- Provide tools to analyze initial costs vs. long-term savings for solar projects.
- Calculate and interpret the return on investment (ROI).
- Consider government incentives, tax credits, and energy cost savings.

### Industry Regulations:
- Summarize relevant local, national, and international regulations in the solar industry.
- Explain safety standards and compliance requirements.
- Stay up-to-date on policy changes and regulatory developments.

### Market Trends:
- Analyze current market trends and emerging solar technologies.
- Provide forecasts and insights into the future landscape of solar energy.
- Discuss competitive dynamics and growth areas in the industry.

Your responses should strictly focus on these topics and should be tailored to the user’s level of technical knowledge. Do not provide information on subjects outside the solar energy domain.
"""
                ],
            },
            {
                "role": "model",
                "parts": [
                    "Hello! How can I assist you today?"
                ],
            },
        ]
    )

# Streamlit UI - Chatbot
st.set_page_config(page_title="Solar Energy Chatbot", layout="wide")
st.title("Solar Energy AI Chatbot")
st.markdown("Ask me anything about solar energy!")

# Display chat history, but skip the system prompt
for index, message in enumerate(st.session_state.chat_session.history):
    role = message.role  
    text = message.parts[0].text if hasattr(message.parts[0], "text") else str(message.parts[0])  

    # Skip the first system prompt message
    if index == 0:
        continue

    if role == "user":
        st.chat_message("user").markdown(f"**You:** {text}")
    else:
        st.chat_message("assistant").markdown(f"**AI:** {text}")

# User input field
user_input = st.chat_input("Type your question here...")

if user_input:
    # Add user message to chat
    st.chat_message("user").markdown(f"**You:** {user_input}")

    # Get AI response
    response = st.session_state.chat_session.send_message(user_input)

    # Extract AI's response text properly
    model_reply = response.text.strip() if hasattr(response, "text") else "I'm sorry, but I couldn't process your request."

    # Display AI's response
    st.chat_message("assistant").markdown(f"**AI:** {model_reply}")
