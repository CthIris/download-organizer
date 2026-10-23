from dataclasses import dataclass
from pathlib import Path

@dataclass
class Move:
    src: Path
    dst: Path
    category_name: str

class MoveLogger:
    """把每次移动写进日志，undo 就靠读它"""
    
    def __init__(self, log_path: Path) -> None:
        pass
    
    def log_move(self, move: Move) -> None:
        pass

class FileCategory:
    """分类规则"""
    
    def __init__(self, name: str, extensions: set[str], target_dir: Path):
        pass
    
    def matches(self, path: Path) -> bool:
        """这个文件归我管吗"""
    
class FileScanner:
    """只负责列出文件，不决定搬去哪"""
    
    def __init__(self, source_dir: Path):
        pass
    
    def scan(self) -> list[Path]:
        """待整理文件列表，跳过隐藏文件、日志和没下载完的"""

class Organizer:
    """决定每个文件搬去哪，并执行"""
    
    def __init__(self, categories: list[FileCategory]):
        pass
    
    def plan(self, files) -> list[Move]:
        """只算不搬：给每个文件算好目标路径"""
    
    def execute(self, moves: list[Move], dry_run: bool=False):
        """dry_run=True 只打印；否则建目录并移动"""
    
    def _resolve_conflict(self, dst: Path):
        """目标已存在就加 (1)(2)，内部方法外部别调"""

def parse_args():
    """解析 --source 和 --dry-run"""


def default_categories():
    """造默认规则组，最后一个是兜底"""


def main():
    pass

if __name__ == "__main__":
    main()