from django.shortcuts import render
import datetime

def index(request):
    today = datetime.datetime.now()
    day_name = today.strftime("%A")  # Получаем название дня недели на английском
    day_class = day_name.lower()      # Приводим к нижнему регистру для использования в классе CSS

    # Словарь для перевода названий дней на русский язык
    days_translation = {
        "monday": "Понедельник",
        "tuesday": "Вторник",
        "wednesday": "Среда",
        "thursday": "Четверг",
        "friday": "Пятница",
        "saturday": "Суббота",
        "sunday": "Воскресенье"
    }

    context = {
        'day_name': days_translation.get(day_name.lower(), "Неизвестный день"),
        'day_class': day_class,
    }

    return render(request, 'index.html', context)