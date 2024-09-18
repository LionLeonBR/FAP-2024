from fasthtml.common import *

app, rt = fast_app()

# route server para "post" ou "get" data
# e não apenas serve() o html

tasks = []

@rt("/")
def get():
    adicionar_tarefa_formulario = Form(
        Input(type="text", name="task", placeholder="Adicione nova tarefa"),
        Button("Adicionar"),
        method="post",
        action="/adicionar-tarefa",   
    )

    lista_tarefa = Ul(
        *[
            Li( # List Item
                f"{task} ",
                " ",
                A("Excluir", href=f"/deletar/{i}"), 
            )
            for i, task in enumerate(tasks)
        ],
        id="lista_tarefa",
    )

    return Titled("Lista de tarefas", H1("Minhas tarefas"), adicionar_tarefa_formulario, lista_tarefa)

@rt("/adicionar-tarefa", methods=["post"])
def post(task: str):
    if task:
        tasks.append(task)
    return RedirectResponse(url="/", status_code=303)

@rt("/deletar/{index}", methods=["get"])
def deletar(index: int):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return RedirectResponse(url="/", status_code=303)

serve()