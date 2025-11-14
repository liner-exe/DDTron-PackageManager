from config import Config
from pathlib import Path

def main():
    base_dir = Path(__file__).resolve().parent
    config = Config(base_dir / 'config.csv').parse()
    if config is None:
        print("Program terminated due to configuration errors.")
        return
    config.print()

if __name__ == '__main__':
    main()