# 文字列を追加・検索できる Trie。
class Trie:
    # 根頂点だけを持つ空の Trie を作る。
    def __init__(self) -> None:
        self.children: list[dict[str, int]] = [{}]
        self.terminal = [False]

    # word を登録し、その末尾に対応する頂点番号を返す。
    def insert(self, word: str) -> int:
        vertex = 0
        for character in word:
            if character not in self.children[vertex]:
                self.children[vertex][character] = len(self.children)
                self.children.append({})
                self.terminal.append(False)
            vertex = self.children[vertex][character]
        self.terminal[vertex] = True
        return vertex

    # word に対応する頂点番号を返す。経路がなければ None。
    def find(self, word: str) -> int | None:
        vertex = 0
        for character in word:
            if character not in self.children[vertex]:
                return None
            vertex = self.children[vertex][character]
        return vertex

    # word が完全一致で登録されているか返す。
    def contains(self, word: str) -> bool:
        vertex = self.find(word)
        return vertex is not None and self.terminal[vertex]


# X を付けた頂点の部分木を除外し、Y の個数を数える Trie。
# 先に全ての文字列を insert してから add_x / add_y を行う。
# answer は X の付いた頂点の配下にない Y の合計。
# 元コードの to, ng, num_y, ans はそれぞれ
# children, blocked, y_count, answer に対応する。
class MarkedTrie:
    # 根頂点と、未設定の X / Y 状態を作る。
    def __init__(self) -> None:
        self.children: list[dict[str, int]] = [{}]
        self.blocked = [False]
        self.y_count = [0]
        self.answer = 0

    # word の文字列を登録し、その末尾に対応する頂点番号を返す。
    def insert(self, word: str) -> int:
        vertex = 0
        for character in word:
            if character not in self.children[vertex]:
                self.children[vertex][character] = len(self.children)
                self.children.append({})
                self.blocked.append(False)
                self.y_count.append(0)
            vertex = self.children[vertex][character]
        return vertex

    # 元コードの init と同じく、X / Y の状態を初期化する。
    def reset_marks(self) -> None:
        self.blocked = [False] * len(self.children)
        self.y_count = [0] * len(self.children)
        self.answer = 0

    # vertex 以下を X で塞ぎ、既存の Y を answer から引く。
    def add_x(self, vertex: int) -> None:
        if self.blocked[vertex]:
            return
        self.blocked[vertex] = True
        self.answer -= self.y_count[vertex]
        for child in self.children[vertex].values():
            self.add_x(child)

    # vertex が塞がれていなければ Y を 1 個追加する。
    def add_y(self, vertex: int) -> None:
        if self.blocked[vertex]:
            return
        self.answer += 1
        self.y_count[vertex] += 1
