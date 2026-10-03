from brain import generate as mlx_generate
from ollama_brain import generate as ollama_generate


def generate(context, backend="mlx"):
    if backend == "mlx":
        return mlx_generate(context)

    if backend == "ollama":
        return ollama_generate(context)

    raise ValueError(f"Unknown backend: {backend}")


if __name__ == "__main__":
    context = "Explain in one short sentence what memory means for an AI companion."

    print("\n--- MLX Brain ---")
    result = generate(context, backend="mlx")
    print(result.text)
    print(f"Model: {result.model}")
    print(f"Backend: {result.backend}")

    print("\n--- Ollama Brain ---")
    result = generate(context, backend="ollama")
    print(result.text)
    print(f"Model: {result.model}")
    print(f"Backend: {result.backend}")
