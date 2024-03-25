FROM python:3.12-slim-bookworm
COPY . /app
WORKDIR /app
RUN apt update -y && apt install -y pandoc texlive-latex-base
RUN ["python", "./task_2.py", ">", "./artifacts/task_2.tex"]
ENTRYPOINT [ "pandoc", "./artifacts/task_2.tex", "-o", "task_2.pdf"]