import os

from pathlib import Path

from dotenv import load_dotenv
from PIL import Image

class Fish:
    def __init__(self):
        self._ROOT = Path(__file__).parent.parent
        self._BLUB_BLUB = self._ROOT / "data" / "blub_blub.png"

    def blub(self) -> str:
        return "Blub blub."
    
    def fih(self) -> Image.Image:
        return Image.open(self._BLUB_BLUB)
    
    def get_flag(self) -> str:
        load_dotenv()
        return os.getenv('FLAG')
