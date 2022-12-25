#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add(pep):
    # Запросить данные о работнике.
    name = input("name faname? ")
    num = int(input("number? "))
    br = int(input("burftday? "))

    # Создать словарь.
    chel = {
        'name': name,
        'num': num,
        'br': br,
    }

    # Добавить словарь в список.
    pep.append(chel)
    # Отсортировать список в случае необходимости.
    if len(pep) > 1:
        pep.sort(key=lambda item: item.get('br', ''))
    return pep