# Файл: test_typing.rpy

init python:
    # Функция для сравнения текста
    def calculate_accuracy(original, typed):
        if not typed:
            return 0
        matches = 0
        min_len = min(len(original), len(typed))
        for i in range(min_len):
            if original[i] == typed[i]:
                matches += 1
        return int((matches / len(original)) * 100)

# Экран мини-игры
screen typing_minigame(goal_text):
    # Переменная внутри экрана
    default typed_text = ""
    
    # Таймер засыпания
    timer 12.0 action Return(typed_text)
    
    # Визуальное потемнение
    add Solid("#000") at transform:
        alpha 0.0
        linear 12.0 alpha 1.0
    
    vbox:
        align (0.5, 0.4)
        spacing 20
        
        fixed:
            xsize 1000 ysize 200
            text "Записывайте лекцию:" size 20 color "#aaa" xalign 0.5 yalign 0.0
            text goal_text size 30 color "#fff" xalign 0.5 yalign 0.5 text_align 0.5
            
        frame:
            background Solid("#ffffff11")
            padding (10, 10)
            xalign 0.5
            
            # ИСПРАВЛЕННАЯ СТРОКА: используем ScreenVariableInputValue
            input value ScreenVariableInputValue("typed_text"):
                size 34
                color "#ffff00"
                length len(goal_text)
                action Return(typed_text) 

    text "Нажимайте Enter, когда закончите (если успеете)..." align(0.5, 0.9) size 16 italic True