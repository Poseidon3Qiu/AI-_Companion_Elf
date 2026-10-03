from dataclasses import dataclass
from typing import Optional


@dataclass
class BrainResult:
    text: str
    model: str
    backend: str

    prompt_tokens: Optional[int] = None
    generation_tokens: Optional[int] = None

    prompt_tps: Optional[float] = None
    generation_tps: Optional[float] = None

    peak_memory: Optional[float] = None
    finish_reason: Optional[str] = None
