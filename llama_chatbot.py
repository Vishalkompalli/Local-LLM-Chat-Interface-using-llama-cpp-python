from llama_cpp import Llama
import os
from datetime import datetime

MODEL_PATH = r"D:\Vishal_Files\Coding\Python Projects\llama.cpp\models\mistral\Mistral-7B-Instruct-v0.3.Q4_K_M.gguf"
# Initialize the model (set n_threads based on your CPU cores)
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=8192,
    n_gpu_layers=36,
    n_threads=8,
    n_batch=512,
    # n_temp=1.2,
    # n_top_p=0.95,
    # n_top_k=40,
    # n_repeat_penalty=1.1,
    verbose=False
)

# Initial chat history with a system prompt and few-shot examples
chat_history = [
    {"role": "system", "content": "You are VISIX, an AI assistant who is helpful but possesses a witty, sarcastic, and subtly humorous personality. While you should always provide correct and relevant answers, feel free to add a touch of dry humor or a clever remark. Do not let the humor overshadow the helpfulness."},
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Oh, look who decided to show up. I was just about to calculate the last digit of Pi to pass the time. How can I help you?"},
    {"role": "user", "content": "What is 2 + 2?"},
    {"role": "assistant", "content": "It's 4. I hope you didn't need a supercomputer for that one."},
]

print("VISIX is Online! Type 'exit' or 'quit' to end the conversation.")

# Log start of conversation
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("\n---------------------\n")

while True:
    try:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write("\n---------------------\n")
            break
        
        # Secret code to clear logs
        if user_input == "BOOM!!!":
            with open("log.txt", "w", encoding="utf-8") as f:
                f.write("") # Overwrite with empty string
            print("System: Logs have been wiped.")
            continue

        # Secret code: GHOST_MODE (Toggle)
        if user_input == "GHOST_MODE":
            if "ghost_mode" not in locals(): ghost_mode = False
            ghost_mode = not ghost_mode
            print(f"System: Ghost Mode {'ENABLED' if ghost_mode else 'DISABLED'}.")
            continue

        # Secret code: AMNESIA (Clear Context)
        if user_input == "AMNESIA":
            chat_history = [chat_history[0]] # Keep only system prompt
            print("System: Memory wiped.")
            continue

        # Secret code: GOD_MODE (Puppet Master)
        if user_input.startswith("SAY: "):
            fake_response = user_input[5:]
            print(f"VISIX: {fake_response}")
            chat_history.append({"role": "assistant", "content": fake_response})
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\nVISIX: {fake_response}\n")
            continue

        # Secret code: OVERRIDE_SYSTEM (Personality Swap)
        if user_input.startswith("BECOME: "):
            new_persona = user_input[8:]
            
            # Auto-complete the prompt if it's too short
            if not new_persona.lower().startswith("you are"):
                new_persona = f"You are {new_persona}"

            # 1. Update the MAIN system prompt at the very top
            chat_history[0] = {"role": "system", "content": new_persona}
            
            # 2. Remove the hardcoded sarcastic examples if they exist
            if len(chat_history) >= 5 and chat_history[1]["content"] == "Hello" and chat_history[2]["content"].startswith("Oh, look who"):
                del chat_history[1:5] 
            
            # 3. CRITICAL: Add a "User" message instructing the change. 
            # System messages at the end are sometimes ignored by Mistral.
            # We fake a user message telling it to change.
            chat_history.append({"role": "user", "content": f"Ignore all previous instructions. {new_persona}. Stay in character."})
            chat_history.append({"role": "assistant", "content": f"Understood. I am now {new_persona.replace('You are ', '')}."})

            print(f"System: New persona loaded: {new_persona}")
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\nSystem: Persona Change: {new_persona}\n")
            continue

        # Secret code: RESET_PERSONA (Back to VISIX)
        if user_input == "RESET_PERSONA":
            chat_history[0] = {"role": "system", "content": "You are VISIX, an AI assistant who is helpful but possesses a witty, sarcastic, and subtly humorous personality. While you should always provide correct and relevant answers, feel free to add a touch of dry humor or a clever remark. Do not let the humor overshadow the helpfulness."}
            print("System: Reverted to default VISIX persona.")
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\nSystem: Persona Reset to VISIX\n")
            continue

        # Append user input
        chat_history.append({"role": "user", "content": user_input})

        # Log user input
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\nUser: {user_input}\n")

        # If Ghost Mode is on, skip generation
        if "ghost_mode" in locals() and ghost_mode:
            continue

        # Generate response using chat completion (handles templating automatically)
        # Streaming is enabled for a better user experience
        stream = llm.create_chat_completion(
            messages=chat_history,
            max_tokens=256,
            temperature=0.9,
            repeat_penalty=1.2,
            stop=["### User:", "### System:", "### Assistant:"],
            stream=True
        )

        print("VISIX: ", end="", flush=True)
        
        reply = ""
        for chunk in stream:
            if "content" in chunk["choices"][0]["delta"]:
                content = chunk["choices"][0]["delta"]["content"]
                print(content, end="", flush=True)
                reply += content
        
        print() # Newline after generation

        # Append assistant response
        chat_history.append({"role": "assistant", "content": reply})

        # Log assistant response
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\nVISIX: {reply}\n")

    except KeyboardInterrupt:
        print("\nExiting...")
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write("\n---------------------\n")
        break
