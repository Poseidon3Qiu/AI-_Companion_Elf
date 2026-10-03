from mlx_vlm import load, generate as mlx_generate
from brain_result import BrainResult

MODEL_NAME = "mlx-community/Qwen3.5-9B-4bit"

# 加载 Local Brain
model = None
processor = None


def generate(context):
    global model, processor

    if model is None:
        print("Loading MLX Brain...")
        model, processor = load(MODEL_NAME)

    response = mlx_generate(
        model,
        processor,
        prompt=context,
        max_tokens=100,
        enable_thinking=False,
    )

    return BrainResult(
        text=response.text,
        model=MODEL_NAME,
        backend="mlx",
        prompt_tokens=response.prompt_tokens,
        generation_tokens=response.generation_tokens,
        prompt_tps=response.prompt_tps,
        generation_tps=response.generation_tps,
        peak_memory=response.peak_memory,
        finish_reason=response.finish_reason,
    )


if __name__ == "__main__":
    result = generate("Hello. Introduce yourself in one short sentence.")

    print("\n--- Local Brain Response ---")
    print(result.text)

    print("\n--- Brain Result ---")
    print(f"Model: {result.model}")
    print(f"Backend: {result.backend}")
    print(f"Prompt tokens: {result.prompt_tokens}")
    print(f"Generated tokens: {result.generation_tokens}")
    print(f"Prompt speed: {result.prompt_tps:.2f} tokens/s")
    print(f"Generation speed: {result.generation_tps:.2f} tokens/s")
    print(f"Peak memory: {result.peak_memory:.2f} GB")
    print(f"Finish reason: {result.finish_reason}")
