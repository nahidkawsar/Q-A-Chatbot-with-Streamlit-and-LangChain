# Q&A Chatbot with Streamlit and LangChain

This project is a simple Q&A chatbot built using Streamlit, LangChain, and various language models like Groq and OpenAI's GPT. The chatbot mimics the speaking style of selected personalities to provide a humorous and engaging experience.

---

## Features
- Supports multiple language models, including Groq and OpenAI models.
- Allows users to select a personality role for the chatbot.
- Adjustable parameters like temperature and max tokens.
- Easy-to-use interface for asking questions and generating responses.

---

## Prerequisites

1. **Python**: Ensure you have Python 3.8 or later installed.
2. **Streamlit**: Install Streamlit and required Python libraries.

---

## Installation Steps

1. **Download the Files**
   - Copy the `main.py` and `requirements.txt` files into your project directory.

2. **Install Dependencies**
   Ensure you have `pip` installed and run the following command:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   Execute the Streamlit app:
   ```bash
   streamlit run main.py
   ```

---

## How It Works

### 1. **Streamlit Interface**
   - **Title and Sidebar Configuration**:
     - Users select a language model (`gemma2-9b-it`, `llama-3.3-70b-versatile`, etc.) and a personality role (e.g., "হিরো আলম", "Salman Khan").
     - Adjustable sliders for `temperature` and `max_tokens` allow customization of the response generation process.
     - Users can enter their API key directly in the sidebar input field.

   - **Main Input Area**:
     - Users can type their questions in the text input box.
     - The chatbot generates a response based on the selected model and personality role.

### 2. **Dynamic Prompt Creation**
   - The system prompt is dynamically updated based on the selected role to mimic the chosen personality's speaking style.
   - A `ChatPromptTemplate` is used to format the prompt and pass it to the language model.

### 3. **Language Model Integration**
   - Depending on the selected model:
     - **Groq Models**: The app uses the `ChatGroq` class with the Groq API key entered by the user.
     - **OpenAI Models**: The app uses the `ChatOpenAI` class with the API key provided by the user.

### 4. **Response Generation**
   - The chatbot generates responses using the chosen model and prompt.
   - Responses are displayed in the Streamlit interface, prefixed with the selected personality's name.

---

## Example Workflow

1. **Launch the App**:
   Run `streamlit run main.py`.

2. **Configure Settings**:
   - Enter your API key in the sidebar.
   - Select a model (e.g., `gemma2-9b-it`).
   - Choose a personality role (e.g., "Salman Khan").
   - Adjust `temperature` and `max_tokens` as needed.

3. **Ask a Question**:
   - Type a question in the text input box (e.g., "What is the weather today?").
   - The chatbot generates a humorous response in the style of the selected personality.

4. **View the Response**:
   - The response appears below the input box, prefixed with the personality's name.

---

## Files in the Project

1. **`main.py`**:
   Contains the Streamlit app code.

2. **`requirements.txt`**:
   Lists all the required Python libraries for the project.

---

## Troubleshooting

1. **Missing API Key**:
   Ensure you have entered the correct API key in the Streamlit sidebar.

2. **Library Errors**:
   Run `pip install -r requirements.txt` to ensure all dependencies are installed.

3. **Model Errors**:
   Verify the model name and API key compatibility with the selected service (Groq or OpenAI).

---

## Future Improvements

- Add support for more models and personality roles.
- Enable multi-language support.
- Improve error handling and debugging messages.

---

## Acknowledgments

- **LangChain**: For simplifying prompt engineering and model integration.
- **Streamlit**: For providing an intuitive interface for the chatbot.
- **OpenAI and Groq**: For their advanced language models.

---

## Contact

For any queries or collaboration opportunities, feel free to connect with me on [LinkedIn](https://linkedin.com/in/h-m-nahid-kawsar-232a86266).

---

Enjoy your chatbot experience!

