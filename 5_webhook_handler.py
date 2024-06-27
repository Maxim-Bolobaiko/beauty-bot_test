# --------------------------------------------------------------#
# В маршрутизаторе проекта добавляем url нашего эндпоинта
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("Datalore/", include("webhook_handler.urls")),
]

# --------------------------------------------------------------#
# Создаем обработчик вебхуков
import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name="dispatch")
class WebhookHandler(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            function = data.get("function")

            if function:
                method = getattr(self, f"handle_{function}", None)
                if method:
                    return method(data)

            return HttpResponse("Invalid function", status=400)
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON", status=400)

    def handle_function1(self, data):
        # Логика обработки function1
        return HttpResponse("Function 1 processed")

    def handle_function2(self, data):
        # Логика обработки function2
        return HttpResponse("Function 2 processed")


# --------------------------------------------------------------#
# В маршрутизаторе приложения добавляем url обработчка
from django.urls import path

from .views import WebhookHandler

urlpatterns = [
    path("", WebhookHandler.as_view(), name="webhook_handler"),
]

# --------------------------------------------------------------#
# Регистрируем приложение в settings.py
INSTALLED_APPS = [
    # ...
    "webhook_handler",
]
