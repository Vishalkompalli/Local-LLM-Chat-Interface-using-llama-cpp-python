from llama_cpp import Llama
import os 

MODEL_PATH = r"E:\My things\Coding\Python Projects\llama.cpp\models\mistral\mistral-7b-instruct-v0.1.Q4_K_M.gguf"
# Initialize the model (set n_threads based on your CPU cores)
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=8,
    verbose=False
)

# Initial chat history with a system prompt
chat_history = [
    {"role": "system", "content": "You are a helpful assistant. Keep replies short and relevant."}
]

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["exit", "quit"]:
        break

    # Append user input
    chat_history.append({"role": "user", "content": user_input})

    # Format prompt
    prompt = ""
    for msg in chat_history:
        role = msg['role'].capitalize()
        prompt += f"\n### {role}:\n{msg['content']}"
    prompt += "\n### Assistant:\n"

    # Generate response
    response = llm(prompt, max_tokens=256, stop=["### User:", "### System:", "### Assistant:"])
    reply = response["choices"][0]["text"].strip()

    print(f"Assistant: {reply}")

    # Append assistant response
    chat_history.append({"role": "assistant", "content": reply})
