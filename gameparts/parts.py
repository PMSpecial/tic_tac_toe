# Объявить класс.

class Board:
    """Класс, который описывает игровое поле."""
    # Инициализировать игровое поле - список списков с пробелами.
    # Пробелы - это пустые клетки.
    # Новый атрибут.

    field_size = 4

    def __init__(self):
        self.board = [
            [' ' for _ in range(self.field_size)]
            for _ in range(self.field_size)
        ]

    # Метод, который обрабатывает ходы игроков.
    def make_move(self, row, col, player):
        self.board[row][col] = player

    # Метод, который отрисовывает игровое поле.
    def display(self):
        print('\n' + '-' * (self.field_size * 4 + 1))
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')
            print('-' * (self.field_size * 4 + 1))
        print('\n')

    def is_board_full(self):
        # Цикл проходится по всем столбцам игрового поля.
        for i in range(self.field_size):
            # А потом по всем строчкам.
            for j in range(self.field_size):
                # Если находит свободную ячейку...
                if self.board[i][j] == ' ':
                    # ...игра продолжается.
                    return False
        # Иначе - ничья!
        return True

    # Этот метод будет определять победу.
    def check_win(self, player):
        # Тут реализована проверка по вертикали и горизонтали.
        for i in range(self.field_size):
            if (all([self.board[i][j] == player
                     for j in range(self.field_size)]) or
                all([self.board[j][i] == player
                     for j in range(self.field_size)])):
                return True
        # Тут реализована проверка по диагонали.
        if (all([self.board[i][i] == player
                 for i in range(self.field_size)]) or
            all([self.board[i][self.field_size - 1 - i] == player
                 for i in range(self.field_size)])):
            return True

        return False

# Переопределяем метод __str__.
    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        )
