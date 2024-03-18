# AI Chatbot Using Ollama and Streamlit

## Overview
This project leverages the power of the Ollama "mistral" model to create a versatile AI chatbot. Built with Streamlit, this chatbot offers an interactive and engaging user interface where users can select different personas for the chatbot, including Normal, Pirate, and Mafia Boss modes. 

## Model
The chatbot is powered by the "mistral" model from Ollama, a framework known for its sophisticated natural language understanding and generation capabilities. The model allows the chatbot to provide responses that are contextually relevant and linguistically rich.

## Technology
- **Ollama**: For the AI model handling the chat responses.
- **Streamlit**: To create an interactive web application for the chatbot.

## Getting Started

### Prerequisites
- Python 3.x
- Pip
- Virtual environment (recommended)

### Setup Instructions
1. Clone this repository to your local machine to get started:
```bash
git clone https://github.com/j19z/ai-chatbot-ollama.git
```
2. Create and Activate a Virtual Environment (optional but recommended):
```bash
python -m venv venv
```
**For Windows**
```bash
venv\Scripts\activate
```
**For Unix or MacOS**
```bash
source venv/bin/activate
```
3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Download and install [Ollama](https://ollama.com/). 
You can run Ollama from you terminal (if this is the first time Ollama will automatically download the model)
```bash
ollama run mistral
```
Note: Read Ollama's documentation, there are a lot of models you could use. 

5. Read Ollama's documentation regarding Modelfiles, for both "mafia" and "pirate" to work you need to make the changes on "modelfile" and run for each one on terminal the following:
```bash
ollama create mafia -f ./Modelfile
```
and...
```bash
ollama create pirate -f ./Modelfile
```

6. Navigate to the project directory and run the application with Streamlit.
```bash
streamlit run app.py
```

## Usage
Upon running the application, you'll be presented with a dropdown menu to select the chatbot's persona. After selecting a persona, you can start interacting with the chatbot by typing your messages into the chat input box. The chatbot, utilizing the selected persona and the "mistral" model, will generate and display responses.

## Note on Deployment
Due to the reliance on Ollama and the requirement for specific configurations, this chatbot is designed to run locally. Currently, it cannot be hosted on Streamlit Cloud as it requires direct access to the Ollama API, which is not feasible within the Streamlit Cloud environment.

## Limitations
The chatbot's response capabilities are bound by the "mistral" model's limitations and the specific configurations set for Ollama.
All API requests are made directly to a locally configured Ollama server.

## Contributing
Contributions, suggestions, and bug reports are welcome! Feel free to fork the repository, make changes, and submit pull requests with your improvements.