from typing import TypeVar, Generic, List
T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)

def hanoi(tower_a: Stack[int], tower_c: Stack[int], tower_b: Stack[int], num_discs: int) -> None:
    print('State: Move')
    print(f'Tower A: {tower_a}')
    print(f'Tower B: {tower_b}')
    print(f'Tower C: {tower_c}')
    print('End: State\n')

    if num_discs == 1:
        tower_c.push(tower_a.pop())
    else:
        hanoi(tower_a, tower_b, tower_c, num_discs - 1)
        hanoi(tower_a, tower_c, tower_b, 1)
        hanoi(tower_b, tower_c, tower_a, num_discs - 1)


if __name__ == "__main__":
    num_discs: int = 3
    tower_a: Stack[int] = Stack()
    tower_b: Stack[int] = Stack()
    tower_c: Stack[int] = Stack()

    for i in range(1, num_discs + 1):
        tower_a.push(i)

    hanoi(tower_a, tower_c, tower_b, num_discs)
    print('State: Hanoi Changed')
    print(f'Tower A: {tower_a}')
    print(f'Tower B: {tower_b}')
    print(f'Tower C: {tower_c}')