from collections import defaultdict
from typing import Generic, TypeVar

Node = TypeVar('Node')
Edge = TypeVar('Edge')


class Graph(Generic[Node, Edge]):
    def __init__(self):
        self.edges: dict[Node, list[Edge]] = defaultdict(list)

    def add_relation(self, node: Node, to: Edge):
        self.edges[node].append(to)

    def get_relation(self, node: Node) -> list[Edge]:
        return self.edges[node]


# cookbooks: Graph[CookBook, CookBook] = Graph()
# recipes: Graph[Recipe, Recipe] = Graph()
#
# cookbook_recipes: Graph[Cookbook, Recipe] = Graph()
#
# recipes.add_relation(
#     Recipe("スパゲッティミートソース"), Recipe("ソーセージとバジルのパスタ")
# )
#
# cookbook_recipes.add_relation(
#     Cookbook("The Food Lab"), Recipe("スパゲッティミートソース")
# )
#
