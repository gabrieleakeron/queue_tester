from http.client import HTTPException

from pydantic import BaseModel
from pathlib import Path
import json

def create_json_file_from_model(dir_name:str, file_name:str,  model: BaseModel) -> Path:
    _dir = Path(__file__).parent.parent.parent / dir_name
    _dir.mkdir(exist_ok=True)

    _path = _dir / f"{file_name}.json"

    with _path.open("w") as f:
        json.dump(model.model_dump(), f, indent=2)

    return _path

def create_json_file_from_dict(dir_name:str, file_name:str,  d: dict) -> Path:
    _dir = Path(__file__).parent.parent.parent / dir_name
    _dir.mkdir(exist_ok=True)

    _path = _dir / f"{file_name}.json"

    with _path.open("w") as f:
        json.dump(d, f, indent=2)

    return _path

def load_json_file(dir_name:str, name: str) -> dict | list[dict]:
    _dir = Path(__file__).parent.parent.parent / dir_name
    _path = _dir / f"{name}.json"

    if not _path.exists():
        raise HTTPException(f"File {_path} not found")

    with _path.open("r") as f:
        json_data = json.load(f)

    return json_data

def find_files_name_in_dir(dir_name: str) -> list[str]:
    _dir = Path(__file__).parent.parent.parent / dir_name

    if not _dir.exists():
        raise HTTPException(f"Directory {_dir} not found")

    file_names = [file.stem for file in _dir.glob("*.json")]

    return file_names