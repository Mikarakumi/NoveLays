# ==============================
# МИНИ-ИГРА: Drag & Drop сортировка
# ==============================

init python:
    import pygame
    import random

    # Все возможные предметы (каждый раз рандомно выбираются 3+3)
    ALL_ITEMS = [
        ("Учебник математики", "book"),
        ("Учебник истории",    "book"),
        ("Учебник биологии",   "book"),
        ("Учебник физики",     "book"),
        ("Учебник химии",      "book"),
        ("Тетрадь по физике",  "notebook"),
        ("Тетрадь по химии",   "notebook"),
        ("Тетрадь по русскому","notebook"),
        ("Тетрадь по алгебре", "notebook"),
        ("Тетрадь по истории", "notebook"),
    ]

    # --------------------------------------------------
    class DragItem:
        """Одна перетаскиваемая карточка"""
        def __init__(self, name, item_type, x, y):
            self.name      = name
            self.item_type = item_type   # "book" или "notebook"
            self.x         = float(x)
            self.y         = float(y)
            self.start_x   = float(x)   # стартовая позиция — для возврата
            self.start_y   = float(y)
            self.dragging  = False
            self.sorted    = False       # True = брошена в правильную зону
            self.wrong     = False       # True = мигает красным (ошибка)
            self.wrong_time = 0.0        # момент ошибки

        def contains(self, mx, my):
            """Курсор попадает в карточку?"""
            return abs(mx - self.x) < 70 and abs(my - self.y) < 35

    # --------------------------------------------------
    class SortingGame(renpy.Displayable):

        SCR_W  = 1920
        SCR_H  = 1080
        ZONE_W = 200
        ZONE_H = 420
        CARD_W = 150
        CARD_H = 70

        def __init__(self):
            super(SortingGame, self).__init__()

            # Случайные 3 книги + 3 тетради, перемешанные
            books     = random.sample([i for i in ALL_ITEMS if i[1] == "book"],     3)
            notebooks = random.sample([i for i in ALL_ITEMS if i[1] == "notebook"], 3)
            selected  = books + notebooks
            random.shuffle(selected)

            # Позиции карточек: 2 ряда по 3, по центру экрана
            cx = self.SCR_W // 2
            cy = self.SCR_H // 2
            positions = [
                (cx - 170, cy - 60), (cx, cy - 60), (cx + 170, cy - 60),
                (cx - 170, cy + 60), (cx, cy + 60), (cx + 170, cy + 60),
            ]

            self.items = [
                DragItem(name, itype, px, py)
                for (name, itype), (px, py) in zip(selected, positions)
            ]

            self.dragged     = None
            self.drag_off_x  = 0.0
            self.drag_off_y  = 0.0
            self.errors      = 0
            self.done        = False

        # ---- Координаты зон --------------------------------
        def _book_zone(self):
            y0 = (self.SCR_H - self.ZONE_H) // 2
            return (30, y0, self.ZONE_W, self.ZONE_H)

        def _nb_zone(self):
            y0 = (self.SCR_H - self.ZONE_H) // 2
            return (self.SCR_W - 30 - self.ZONE_W, y0, self.ZONE_W, self.ZONE_H)

        def _in_zone(self, rect, mx, my):
            x, y, w, h = rect
            return x < mx < x + w and y < my < y + h

        # ---- Render ----------------------------------------
        def render(self, width, height, st, at):
            r = renpy.Render(width, height)
            c = r.canvas()

            # Фон
            # c.rect((20, 20, 40), (0, 0, width, height))

            # Зона учебников (слева)
            bz = self._book_zone()
            c.rect((30, 60, 110, 90), bz)
            c.rect((80, 140, 220), bz, 3)

            # Зона тетрадей (справа)
            nz = self._nb_zone()
            c.rect((80, 30, 110, 90), nz)
            c.rect((170, 90, 220), nz, 3)

            # Подписи зон
            self._text(r, "УЧЕБНИКИ", bz[0] + bz[2]//2, bz[1] - 30, 22, (100, 170, 255))
            self._text(r, "ТЕТРАДИ",  nz[0] + nz[2]//2, nz[1] - 30, 22, (190, 110, 255))

            # Счётчик
            done_count = sum(1 for i in self.items if i.sorted)
            self._text(r,
                f"Разложено: {done_count} / 6      Ошибок: {self.errors}",
                width // 2, 28, 22, (200, 200, 200))

            # Подсказка
            self._text(r, "Перетащи каждый предмет в нужную зону",
                    width // 2, height - 28, 18, (120, 120, 120))

            # Карточки (сначала не тащимые, потом тащимую — поверх)
            for item in self.items:
                if not item.sorted and not item.dragging:
                    self._draw_card(r, c, item, st)

            if self.dragged:
                self._draw_card(r, c, self.dragged, st, shadow=True)

            # Финальный оверлей
            if self.done:
                ov = renpy.Render(width, height)
                oc = ov.canvas()
                oc.rect((0, 0, 0, 170), (0, 0, width, height))
                self._text(ov, "Готово!",
                        width // 2, height // 2 - 30, 52, (255, 255, 255))
                self._text(ov,
                        f"Ошибок: {self.errors}   —   нажми куда угодно",
                        width // 2, height // 2 + 30, 24, (180, 180, 180))
                r.blit(ov, (0, 0))

            renpy.redraw(self, 0)
            return r

        # ---- Рисовка одной карточки ------------------------
        def _draw_card(self, render, canvas, item, st, shadow=False):
            hw = self.CARD_W // 2
            hh = self.CARD_H // 2
            ix = int(item.x)
            iy = int(item.y)

            # Тень при перетаскивании
            if shadow:
                canvas.rect((0, 0, 0, 120),
                            (ix - hw + 6, iy - hh + 6, self.CARD_W, self.CARD_H))

            # Мигание при ошибке
            blink = item.wrong and (int(st * 7) % 2 == 0)
            if blink:
                bg = (180, 40, 40)
            elif item.item_type == "book":
                bg = (40, 80, 150)
            else:
                bg = (100, 40, 150)

            canvas.rect(bg, (ix - hw, iy - hh, self.CARD_W, self.CARD_H))
            canvas.rect((220, 220, 220),
                        (ix - hw, iy - hh, self.CARD_W, self.CARD_H), 2)

            # Название предмета
            self._text(render, item.name, ix, iy, 18, (255, 255, 255))

            # Сброс мигания через ~0.6 сек
            if item.wrong and (st - item.wrong_time) > 0.6:
                item.wrong = False

        # ---- Текст -----------------------------------------
        def _text(self, render, text, cx, cy, size, color):
            td = Text(text, size=size, color=color)
            tw, th = td.render(900, 80, 0, 0).get_size()
            render.blit(
                td.render(900, 80, 0, 0),
                (int(cx - tw / 2), int(cy - th / 2))
            )

        # ---- Events ----------------------------------------
        def event(self, ev, x, y, st):
            # После завершения — любой клик возвращает количество ошибок
            if self.done:
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    renpy.end_interaction(self.errors)
                    return self.errors  
                raise renpy.IgnoreEvent()

            # Зажать
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                for item in reversed(self.items):
                    if not item.sorted and item.contains(x, y):
                        item.dragging   = True
                        self.dragged    = item
                        self.drag_off_x = item.x - x
                        self.drag_off_y = item.y - y
                        break

            # Двигать
            elif ev.type == pygame.MOUSEMOTION:
                if self.dragged:
                    self.dragged.x = x + self.drag_off_x
                    self.dragged.y = y + self.drag_off_y

            # Отпустить
            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                if self.dragged:
                    self._on_drop(self.dragged, x, y, st)
                    self.dragged.dragging = False
                    self.dragged = None

            raise renpy.IgnoreEvent()

        # ---- Логика броска ---------------------------------
        def _on_drop(self, item, mx, my, st):
            in_book = self._in_zone(self._book_zone(), mx, my)
            in_nb   = self._in_zone(self._nb_zone(),   mx, my)

            if in_book:
                if item.item_type == "book":
                    item.sorted = True                      # правильно
                else:
                    self._wrong(item, st)                   # ошибка
            elif in_nb:
                if item.item_type == "notebook":
                    item.sorted = True                      # правильно
                else:
                    self._wrong(item, st)                   # ошибка
            else:
                # Промах мимо зон — просто вернуть
                item.x, item.y = item.start_x, item.start_y

            if all(i.sorted for i in self.items):
                self.done = True

        def _wrong(self, item, st):
            self.errors     += 1
            item.wrong       = True
            item.wrong_time  = st
            item.x, item.y   = item.start_x, item.start_y  # вернуть на место

        def visit(self):
            return []


# ==============================
# LABEL — вызывается из сценария
# ==============================
screen sorting_game():
    add SortingGame() xalign 0.5 yalign 0.5

label sorting_minigame:
    call screen sorting_Game
    $ _errors = ui.interact(_game)

    if _errors == 0:
        $ affection_igorina += 2
    elif _errors <= 2:
        $ affection_igorina += 1
    return
