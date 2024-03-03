# Артефакты к ДЗ 1

## nl

печатает пронумерованные строки из переданного файла

_тестовый запуск производился вот так_

`python ./nl.py ./artifacts/Istoria_Gosudarstva_Rossiyskogo.txt > ./artifacts/nl_output.txt`

## tail

печатает последние 10 строк файла

_тестовый запуск производился вот так_

`python ./tail.py ./artifacts/Istoria_Gosudarstva_Rossiyskogo.txt ./artifacts/nl_output.txt > ./artifacts/tail_output.txt`

## wc

печатает количетсво строк слов и символов в файле

`python ./wc.py ./artifacts/Istoria_Gosudarstva_Rossiyskogo.txt ./artifacts/nl_output.txt ./artifacts/tail_output.txt > ./artifacts/wc_output.txt`