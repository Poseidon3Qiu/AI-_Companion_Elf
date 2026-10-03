import subprocess
from brain_result import BrainResult

MODEL_NAME = "llama3.1:8b"


def generate(context):
    result = subprocess.run(
        ["ollama", "run", MODEL_NAME, context],
        capture_output=True,
        text=True,
        check=True,
    )

    return BrainResult(
        text=result.stdout.strip(),
        model=MODEL_NAME,
        backend="ollama",
    )


if __name__ == "__main__":
    result = generate("Hello. Introduce yourself in one short sentence.")

    print("\n--- Ollama Brain Response ---")
    print(result.text)

    print("\n--- Brain Result ---")
    print(f"Model: {result.model}")
    print(f"Backend: {result.backend}")
    print(f"Prompt tokens: {result.prompt_tokens}")
    print(f"Generated tokens: {result.generation_tokens}")
    print(f"Generation speed: {result.generation_tps}")
    print(f"Peak memory: {result.peak_memory}")
    print(f"Finish reason: {result.finish_reason}")
