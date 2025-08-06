# Local LLM Chat Interface using llama.cpp-python

A simple Python chat interface for running large language models (LLMs) locally using llama.cpp via Python bindings. This repository helps you interact with LLMs on your local machine through a convenient terminal chatbot.

**Features**  
Local Inference: Run Llama-based models without relying on cloud services or external APIs.  

Python Interface: Chat with the model interactively using a native Python script.  

Customization: Easily configure models, adjust prompts, and tweak settings in the script.  

**Prerequisites**  
Python 3.8+  
llama.cpp (with Python bindings)(https://github.com/abetlen/llama-cpp-python)  
Supported Llama-based model in .bin, .gguf, or similar format(https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF)  

**Setup**  
Clone the repository:  
git clone https://github.com/Vishalkompalli/Local-LLM-Chat-Interface-using-llama-cpp-python.git  
cd Local-LLM-Chat-Interface-using-llama-cpp-python  

**Install dependencies:**  
(Install Python dependencies as needed and set up llama-cpp-python.)  
Download a compatible Llama model.  
Follow llama.cpp model download instructions for guidance.  

Run the chatbot:  
python llama_chatbot.py  
You may need to modify the script to specify your model path and settings.  

**Usage**  
After running the script, type your message in the terminal and watch the model respond.  
Press Ctrl+C to exit the chat.  

For advanced configuration, update parameters in llama_chatbot.py (e.g., model path, prompt template, context length, etc.)        
	               
| File Overview       | File	Description |  
|---------------------|-------------------|
| llama_chatbot.py    | Main Python script to run chat|
| README.md           |Project documentation|


**Contributing**  
Contributions, issues, and feature requests are welcome! Please fork the repository and make a pull request.  

**License**  
This project is open source and provided as-is for research and personal use. Refer to the license file (if available) or clarify your use cases as needed.  

**Acknowledgements**  
Built upon llama.cpp.  
https://github.com/abetlen  
https://huggingface.co/  

Inspired by the open-source LLM community.  

For any questions or support, please raise an issue in the repository.  
