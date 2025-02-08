# Solar AI Assistant


An AI-powered chatbot that provides consulting services for the solar energy industry. The chatbot uses the Google Generative AI model and answers questions related to solar panel technology, installation processes, maintenance, cost analysis, industry regulations, and market trends.

## Features
- **AI-Powered Solar Energy Consultant**: Provides clear, concise, and accurate answers about solar energy topics.
- **User-Friendly Interface**: Built with Streamlit, allowing easy interaction with the chatbot.
- **Customizable Chat History**: Maintains a conversation history that adapts based on user input.
  
## Technologies Used
- **Google Generative AI**: Used to power the AI assistant's responses.
- **Streamlit**: Used to build the user interface.
- **python-dotenv**: Used to securely load environment variables (e.g., API keys).

## Setup and Installation

**##1. Prerequisites**
- Python 3.8 or later
- pip (Python package installer)

### Steps to Run the Project Locally

**Clone the repository**:
   ```bash
   git clone https://github.com/Piyush2510verma/SolarAI.git
   cd SolarAI
```
**Install Python Dependencies**
Create a virtual environment and install the necessary dependencies for the Python backend:

```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
pip install -r requirements.txt
```

**Set Up the .env File**

Create a .env file in the root of the project and add your Google API Key:
```bash
GOOGLE_API_KEY=your_google_api_key_here
```
**Run the Application Locally**
Run the Streamlit app locally:
```bash
streamlit run app.py
```

**2. Streamlit Application**

The main frontend of the application is built using Streamlit. It collects user inputs, sends them to the backend serverless function, and displays the AI-generated response. The app's main functions include:

Taking input from the user via a text box.
Sending the input to the backend serverless function.
Displaying the chatbot response in the UI.


**3. Example Use Cases**:

Use Case 1: General Inquiry
Scenario: A user asks about solar panel technology.
User Input: "How do solar panels work?"
AI Response: The chatbot explains the photovoltaic process and how solar panels generate electricity.

Use Case 2: Cost Analysis
Scenario: A user inquires about the return on investment for installing solar panels.
User Input: "What is the ROI for solar panel installation?"
AI Response: The chatbot provides an overview of ROI, factoring in costs, savings, and government incentives.

Use Case 3: Maintenance Tips
Scenario: A user asks for maintenance advice for their solar panels.
User Input: "How do I maintain my solar panels?"
AI Response: The chatbot explains routine cleaning, inspections, and common troubleshooting techniques.



**4. Future Improvement Suggestions**:

4.1 Enhanced User Experience
Natural Language Understanding: Improve the chatbot’s ability to understand and interpret complex or vague queries related to solar energy.
Multilingual Support: Add support for multiple languages to reach a wider audience.

4.2 Expand Knowledge Base
Integration with Real-Time Data: Integrate real-time data for solar panel efficiency, weather conditions, or local incentives to provide more dynamic responses.
User Customization: Allow users to input their location to get location-specific information about solar panel installations, policies, and savings.

4.3 Broader API Integration
Additional Solar APIs: Integrate other APIs (e.g., solar irradiance data, solar calculators) to provide more comprehensive insights.
Data Visualization: Provide visualizations (charts, graphs) of energy savings, ROI, etc., to enhance understanding.

**Conclusion**
The Solar Energy AI Chatbot provides an intelligent and interactive platform for users to access reliable information on solar energy. Through its use of Google's Generative AI API, the app delivers personalized and accurate responses tailored to users' needs. Future improvements can focus on expanding the knowledge base and improving the overall user experience.
