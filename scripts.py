# pyright: reportUnknownMemberType=false
# pyright: reportUnknownVariableType=false
# pyright: reportMissingTypeStubs=false
import pyright
from watchdog.events import PatternMatchingEventHandler, FileModifiedEvent
from watchdog.observers import Observer
import time
import sys
import pycodestyle


class TestFileWatchEventHandler(PatternMatchingEventHandler):
    def __run_test(self):
        run_all_tests()

    def on_created(self, event: FileModifiedEvent):
        self.__run_test()

    def on_modified(self, event: FileModifiedEvent):
        self.__run_test()

    def on_moved(self, event: FileModifiedEvent):
        self.__run_test()


def watch_tests():
    event_handler = TestFileWatchEventHandler(patterns=['*.py'])
    observer = Observer()
    observer.schedule(event_handler, './src', recursive=True)
    observer.start()
    print('Watching test files...')

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.stop()

    print('Stop watch test files')


def run_all_tests():
    import unittest
    loader = unittest.defaultTestLoader

    suite = loader.discover("./src")

    runner = unittest.TextTestRunner()

    if not runner.run(suite).wasSuccessful():
        sys.exit(1)


def run_lint():
    style = pycodestyle.StyleGuide()
    report = style.check_files(["src/", "scripts.py"])

    if report.total_errors:
        print("pycodestyle validation failed")
        sys.exit(1)

    exit_code = pyright.main([])
    sys.exit(exit_code)
