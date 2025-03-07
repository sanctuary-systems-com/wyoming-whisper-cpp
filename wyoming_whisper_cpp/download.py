"""Utility for downloading models."""
import subprocess
from pathlib import Path
from typing import Union

WHISPER_CPP_MODELS = [
    "tiny",
    "tiny.en",
    "tiny-q5_1",
    "tiny.en-q5_1",
    "base",
    "base.en",
    "base-q5_1",
    "base.en-q5_1",
    "small",
    "small.en",
    "small-q5_1",
    "small.en-q5_1",
    "medium",
    "medium.en",
    "medium-q5_0",
    "medium.en-q5_0",
    "large-v1",
    "large-v2",
    "large-v2-q5_0",
    "large-v3",
    "large-v3-q5_0",
]


def model_name_to_path(model_name: str, dest_dir: Union[str, Path]) -> Path:
    return Path(dest_dir) / f"ggml-{model_name}.bin"


def download_model(
    model_name: str,
    dest_dir: Union[str, Path],
) -> None:
    """Downloads whisper.cpp model using the ggml download script."""
    dest_dir = Path(dest_dir)

    dest_dir.mkdir(parents=True, exist_ok=True)
    subprocess.check_call(["download-ggml-model.sh", str(model_name), str(dest_dir)])
