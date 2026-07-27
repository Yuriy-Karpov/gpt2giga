import multiprocessing

from gpt2giga.api_server import run


if __name__ == "__main__":
    multiprocessing.freeze_support()
    run()
