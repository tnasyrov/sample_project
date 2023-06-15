from django.http import HttpResponse


def index(request):
    host = request.META["HTTP_HOST"] # получаем адрес сервера
    user_agent = request.META["HTTP_USER_AGENT"] # получаем данные браузера
    path = request.path # получаем запрошенный путь
    return HttpResponse(f""" <p>Host: {host}</p> <p>Path: {path}</p> <p>User-agent: {user_agent}</p> """, content_type="text/plain",
                        charset="utf-8", headers={"SecretCode": '313373228'})


def about(request, name, age):
    return HttpResponse(f"""
    <h2>О пользователе</h2> 
    <p>Имя: {name}</p> 
    <p>Возраст: {age}</p> """)


def contacts(request):
    return HttpResponse("<h2>Контакты</h2>")
