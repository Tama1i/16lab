#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sel(pep, zapros):

    count = 0
# Проверить сведения работников из списка.
    for chel in pep:
        if chel.get('num') == zapros:
            count += 1
            return chel, count
        # Если счетчик равен 0, то работники не найдены.
    if count == 0:
        return "cheela s takim nomerom net", count
