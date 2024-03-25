**task 1**  
артифакт создал вот так
`python3 ./task_1.py > ./artifacts/task_1.tex`

**task 2**  
выложил либу на PyPi, в `task_2.py` импортируется уже либа устрановленная через пип,
также она добавлена в `requirements.txt`
[https://pypi.org/project/latex-gen-pro-py/](https://pypi.org/project/latex-gen-pro-py/)  
PDF скомпилял на маке командой  
`pandoc ./artifacts/task_2.tex -o task_2.pdf`

**task 3**  
```
docker build -t task3 .
docker run task3
```
