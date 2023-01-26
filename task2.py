from typing import Callable, Any, List


def create_handlers(callback: Callable[[Any], Any]) -> List[Callable[[Any], Any]]:
    return [lambda x=step: callback(x) for step in range(5)]


def execute_handlers(handlers: List[Callable[[], Any]]) -> None:
    for handler in handlers:
        handler()
