This project is an AI chatbot built using:

LangChain for orchestrating the prompt and LLM

Ollama for running the LLM (e.g., LLaMA3)

Langfuse for tracing, monitoring, prompt management, and evaluation

Streamlit for a simple web-based UI

dotenv to manage environment variables

What This Project Does

This chatbot takes user input, passes it through a LangChain chain using a prompt stored in Langfuse’s prompt hub, runs it with an Ollama local model like llama3.1, and logs all relevant details to Langfuse.

With Langfuse, you get:

Traceable LLM sessions

Prompt management and versioning

Real-time user/session debugging

Evaluation metrics like response quality

Demo Screenshot
Chat Bot Screenshot
<img width="2477" height="568" alt="image" src="https://github.com/user-attachments/assets/0c13323e-8708-479a-89f2-a64b4b202cee" />
Langfuse Dashboard Screenshot
<img width="2156" height="1358" alt="image" src="https://github.com/user-attachments/assets/dd30c15a-2e5d-4506-8884-9c3a90ba8ffa" />


Project Structure
├── app.py                  # Main Streamlit chatbot app
├── .env                    # Stores Langfuse environment variables
├── llm_setup.py            # Main Streamlit chatbot app
├── monitoring.py           # Stores Langfuse environment variables (not committed)
├── config.py               # Stores Langfuse environment variables (not committed)
├── requirements.txt        # Python dependencies
└── README.md               # This documentation

How It Works – Step by Step
1. User enters a message into the chatbot via Streamlit UI.

2. A decorated function @observe from Langfuse wraps the interaction to trace everything.

3. The code fetches the prompt from Langfuse prompt hub using the name Helpassistant.

4. A LangChain LLMChain is created using the prompt and the Ollama model (llama3.1).

5.The input is passed through the chain to get a response from the model.

6. Metadata and metrics (like user ID, session flags, and quality scores) are logged to Langfuse.

7. If tracing is active, a trace link is shown in the Streamlit app for review/debugging.

Environment Setup
Make sure you have the following in your .env file:

LANGFUSE_PUBLIC_KEY=your_public_key
LANGFUSE_SECRET_KEY=your_secret_key
LANGFUSE_HOST=https://cloud.langfuse.com 

Installation and Running the App
1. Clone the repository
   git clone https://github.com/yourusername/langfuse-chatbot.git
   cd langfuse-chatbot

2. Set up virtual environment (optional)
   python -m venv venv
   Ovenv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Set up .env
   Create a file .env in the root folder with the keys from Langfuse.

5. Run Ollama (LLaMA3)
   Make sure you have Ollama installed and run the model:
   ollama run llama3.1 or any other model like mistral or anything we can run

6. Run the app
   streamlit run app.py
   
Key Features
1.Real-time LLM interaction with Streamlit
2.Prompt fetching directly from Langfuse’s prompt hub
3.Traces every interaction for debugging & improvement
4.Adds metrics like response quality for later evaluation
5.Securely stores API keys using .env

Tech Stack

| Technology | Purpose                       |
| ---------- | ----------------------------- |
| Python     | Core programming language     |
| Streamlit  | UI for the chatbot            |
| LangChain  | Orchestrates prompts + models |
| Ollama     | Local LLM runtime             |
| Langfuse   | Tracing, prompt mgmt, eval    |
| dotenv     | Environment config management |

Improvements
1.Add feedback buttons (👍 / 👎) and log score to Langfuse
2.Cache prompt versions locally for offline use
3.Add ability to switch between models
4.Add input validation and error handling

Author
Created by Allan Abraham Maret












