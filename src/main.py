from config import Config

def main():
    config = Config('./src/config.csv').parse()
    config.print()

if __name__ == '__main__':
    main()