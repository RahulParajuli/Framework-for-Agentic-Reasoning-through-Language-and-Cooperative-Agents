import os
import yaml
from dotenv import load_dotenv
from pathlib import Path
from typing import Union, Optional
from paths import PUBLICATION_FPATH, ENV_FPATH

def load_publication():
    """
    loads the md file
    returns: content of the publiation as string. 
    Raises:
        FileNotFoundError: if the publication file does not exist
    """
    file_path = Path(PUBLICATION_FPATH)
    if not file_path.exists():
        raise FileNotFoundError(f"Publication file not found at {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        raise IOError(f"Error reading publication file: {e}")
    
def load_yaml_config(file_path: Union[str, Path]) -> dict:
    """
    Loads a YAML configuration file and returns its content as a dictionary.
    
    Args:
        file_path (Union[str, Path]): Path to the YAML file.
        
    Returns:
        dict: Content of the YAML file.
        
    Raises:
        FileNotFoundError: If the specified file does not exist.
        yaml.YAMLError: If there is an error parsing the YAML file.
    """
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"Configuration file not found at {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML file: {e}")
    except Exception as e:
        raise IOError(f"Error reading configuration file: {e}")
    
def load_env() -> None:
    """
    Loads environment variables from a .env file.
    This function uses the `dotenv` package to load environment variables
    """
    load_dotenv(ENV_FPATH, override=True)
    api_key= os.getenv("OPENAI_API_KEY")
    assert api_key, "OPENAI_API_KEY not found in .env file. Please set it before running the script."

def save_text_to_file(text: str, file_path: Union[str, Path], header:Optional[str]) -> None:
    """
    Saves a given text to a specified file.
    
    Args:
        text (str): The text to save.
        file_path (Union[str, Path]): The path to the file where the text will be saved.
        
    Raises:
        IOError: If there is an error writing to the file.
    """
    try:
        filepath = Path(file_path)
        filepath.parent.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists
        with open(filepath, 'w', encoding='utf-8') as f:
            if header:
                f.write(f"{header}\n\n")
                f.write("# " + "=" * 50 + "\n\n")
            f.write(text)
    except Exception as e:
        raise IOError(f"Error writing to file {file_path}: {e}")