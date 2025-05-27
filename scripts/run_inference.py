from llama_cpp import Llama

# Load GGUF model
llm = Llama(
    model_path="./models/mistral-gguf/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=6,     # Adjust based on your CPU
    verbose=True
)

# Define test prompt
prompt = """
You are a clinical AI model. Given the following report, classify NSCLC status as one of:
- Definite
- Likely
- Unlikely
- Uncertain

Also give a brief justification.

Patient Report:
Patient presents with persistent cough, weight loss, and nodular lesion on CT.

Respond with:
{"NSCLC_Status": "", "Justification": ""}
"""

# Run inference
response = llm(prompt, stop=["}"], echo=False, temperature=0.5, top_p=0.9)
print("Model Output:\n", response["choices"][0]["text"])
