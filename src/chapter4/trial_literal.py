from dataclasses import dataclass
from typing import Literal


@dataclass
class Error:
    error_code: Literal[1, 2, 3, 4, 5]
    disposed_of: bool


@dataclass
class Snack:
    name: Literal["プレッツェル", "ホットドッグ", "ベジーバーガー"]
    condiments: set[Literal["マスタード", "ケチャップ"]]


# 3.12だとエラー発生しない。warningは出ている。pydantic.BaseModelの方が良さそう
print("1")
error = Error(0, False)
print(f"{error=}")
snack1 = Snack("無効", set())
print(f"{snack1=}")
snack2 = Snack("プレッツェル", {"マスタード", "レリッシュ"})
print(f"{snack2=}")
