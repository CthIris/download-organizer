from dataclasses import dataclass
from pathlib import Path

@dataclass
class Move:
    src: Path
    dst: Path
    category_name: str

class MoveLogger:
    
    def __init__(self, log_path: Path) -> None:
        pass
    
    def log_move(self, move: Move) -> None:
        pass

class FileCategory:
    """分类规则"""
    
    def __init__(self, name: str, extensions: set[str], target_dir: Path):
        pass
    
    def matches(self, path: Path) -> bool:
        pass
    
class FileScanner:
    
    def __init__(self, source_dir: Path):
        pass
    
    def scan(self) -> list[Path]:
        pass

class Organizer:
    
    def __init__(self, categories: list[FileCategory]):
        pass
    
    def plan(self, files) -> list[Move]:
        pass
    
    def execute(self, moves: list[Move], dry_run: bool=False):
        pass
    
    def _resolve_conflict(self, dst: Path):
        pass

def parse_args():
    pass


def default_categories():
    pass


def main():
    pass

if __name__ == "__main__":
    main()