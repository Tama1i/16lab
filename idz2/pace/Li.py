#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def li(pep):
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 8
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
            "№",
            "F.I.O.",
            "NUMBER",
            "BRDAY"
        )
    )
    print(line)
    for idx, chel in enumerate(pep, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                idx,
                chel.get('name', ''),
                chel.get('num', ''),
                chel.get('br', 0)
            )
        )
        print(line)
