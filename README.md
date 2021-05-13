# AC Labs - Django Project

## How to run project

Build image:<br>
`docker build . --tag todo-app`

Run image:<br>
`docker run -it -v "$(pwd)":/app -p 8000:8000 --rm todo-app`
