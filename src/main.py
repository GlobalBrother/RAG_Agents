import json

from graph import build_graph


def main() -> None:
    graph = build_graph()
    graph.invoke({})

if __name__ == "__main__":
    main()
