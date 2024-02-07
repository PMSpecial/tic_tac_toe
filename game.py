# game.py

from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def main():
    game = Board()
    # Первыми ходят крестики.
    current_player = 'X'
    # Это флаговая переменная. По умолчанию игра запущена и продолжается.
    running = True
    game.display()

    # Тут запускается основной цикл игры.
    while running:

        print(f'Ход делают {current_player}')

        # Запускается бесконечный цикл.
        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError('Ячейка занята. '
                                            'Введите другие координаты.')
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Введите значения для строки и столбца заново.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Введите значения для строки и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        game.make_move(row, column, current_player)
        game.display()
        # После каждого хода надо делать проверку на победу и на ничью.
        if game.check_win(current_player):
            win_result = f'Победили {current_player}!\n'
            print(win_result)
            save_result(win_result)
            running = False
        elif game.is_board_full():
            no_win_result = 'Ничья\n'
            print(no_win_result)
            save_result(no_win_result)
            running = False

        current_player = 'O' if current_player == 'X' else 'X'


def save_result(result):
    with open('result.txt', 'a', encoding='utf-8') as res_file:
        res_file.write(result)


if __name__ == '__main__':
    main()
