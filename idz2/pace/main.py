#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys

from pace.Add import add
from pace.Li import li
from pace.Sel import sel


def main():
    # Список работников.
    pep = []
    chel = ""
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            pep = add(pep)

        elif command == 'list':
            li(pep)
        elif command == 'select':
            zapros = int(input("zapros po numeru  "))
            chel, count = sel(pep, zapros)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                    count,
                    chel.get('name', ''),
                    chel.get('num', ''),
                    chel.get('br', 0)
                )
            )

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - add chel;")
            print("list - show list of pep;")
            print("select <стаж> - запросить работников со стажем;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
