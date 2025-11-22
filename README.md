# VISIX - Local LLM Chat Interface

VISIX is a lightweight, local chatbot interface powered by 'llama-cpp-python'. Designed to run Large Language Models (LLMs) entirely on your machine, VISIX comes with a distinct personality—witty, sarcastic, and helpful.

## Features

- **Local Inference**: Run powerful LLMs like Mistral locally without internet dependency.
- **Distinct Persona**: VISIX isn't just a bot; it's a sarcastic assistant with a dry sense of humor.
- **Interactive Shell**: A clean terminal-based chat interface.
- **Streaming Responses**: Real-time text generation.
- **Logging**: Automatically logs conversations to 'log.txt'.

## Prerequisites

- Python 3.8+
- 'llama-cpp-python'
- A GGUF model file (e.g., Mistral-7B-Instruct)

## Installation

1. **Clone the repository:**
   git clone https://github.com/Vishalkompalli/Local-LLM-Chat-Interface-using-llama-cpp-python.git
   cd Local-LLM-Chat-Interface-using-llama-cpp-python

2. **Install dependencies:**
   Ensure you have a C++ compiler installed for 'llama-cpp-python'.
   pip install llama-cpp-python
   *Note: Refer to the [llama-cpp-python documentation](https://github.com/abetlen/llama-cpp-python) for hardware-specific installation (CUDA, Metal, etc.).*

3. **Download a Model:**
   Download a GGUF model (e.g., from [TheBloke on Hugging Face](https://huggingface.co/TheBloke)) and place it in a known directory.

4. **Configuration:**
   Open 'llama_chatbot.py' and update the 'MODEL_PATH' variable to point to your downloaded model file.
   MODEL_PATH = r"path\to\your\model.gguf"

## Usage

Run the chatbot:
python llama_chatbot.py

Type your message and press Enter. Type 'exit' or 'quit' to end the session.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is open-source.

## Acknowledgements

- [llama.cpp](https://github.com/ggerganov/llama.cpp)
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
