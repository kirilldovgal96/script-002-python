#!/usr/bin/env python3

prog="MyProgram V1.2.3 Copyright (c) 2022"
n1 = prog.lower().find(' v') +2
n2 = prog.find(' ', n1)
concl_version = prog[n1:n2]
print(f'Версия: {concl_version}')