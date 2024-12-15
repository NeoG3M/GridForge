# GRID FORGE

Grid Forge - это tower defense игра, написанная на pygame и выполненная в стилистике будущего, где идёт война за ресурсы с помощью различных мехов и стационарных турелей.

***
## КОНЦЕПЦИЯ

Основным объектов для защиты является реактор, что подпитывает все клетки башен, а также открытие хранилища, дабы группа игрока смогла изучить новое вооружение и противостоять врагу с большей силой. Идёт война за ресурсы.

Данная игра основана на традициях жанра, но со своими особенностями: 

### Фишки:
- возможность создания собственных башен на основе модулей с разными характеристиками
- различные усиления, что игрок может получить в ходе боя. Могут появиться в случайных местах или выпасть как награда за убийство
- HP у башен(некоторые враги способны уничтожать/отключать башни)
- лабиринтные карты - у противника будет извилистый путь, что даст ему возможность выбирать наилучшую дорогу

### ЧЕРТЕЖИ И МОДУЛИ

Основной фишкой игры является механика создания пользовательских башен с различным вооружением и характеристиками, что как раз будут складываться из возможностей модулей.

Ограничение в энергии - несмотря на возможное обилие клеток для размещения башен, игрок будет ограничен выработкой электроэнергии самим реактором, что не позволит использовать слишком много мощных орудий. Но выработку можно будет улучшить по ходу боя или в главном меню.

Каждая клетка для размещения башен имеет свою некую мощность и “пропускную способность”, то есть при создании башни игрок будет ограничен определённым уровнем “базы”(MK.1, MK.2 и т.д.) - у каждой своя максимальная мощность, размер.

За основу каждой башни будет лежать основной модуль - шарнир, со своей скоростью поворота и максимальной грузоподъёмностью(что определяется размерами сетки). Дальше же игрок может накладывать модули брони, ракетниц, рельсотрона, пулемёта и подобного.

## ВРАГИ 

Врагами выступают различные роботы-мехи, что отличаются количеством здоровья, скоростью и мощностью собственных орудий. Они способны атаковать башни, ухудшая их характеристики, НО у каждого блока будет свой предел, после которого настаёт “предсмертного дыхание”, что будет выдавать увеличенную скорострельность, защиту. Данный режим будет активироваться при снижении НР ниже определённого уровня, что можно будет улучшить.

## ЭКОНОМИКА

С каждого убийства игрок будет получать прибыль и на неё уже устанавливать свои или заранее предоставленные башни. Также у него есть возможность ремонтировать башни с помощью соответствующего инструмента.

После окончания уровня, игрок получает чертежи башен и определённое количество очков рейтинга, что зависит от оставшегося НР реактора. 

## СТАТИСТИКА

В главном меню игрок сможет понаблюдать своё общее количество очков.

## СТРУКТУРА УРОВНЕЙ

Карта каждого уровня представляет собой клетчатое поле( для компьютера), записанное в ccv файле. Остальные же настройки уровня(список врагов, волн, количество награды и чертежей) будут записаны в других файлах этого уровня.
## СТРУКТУРА CCV

Каждая клетка будет хранится в виде - {class_first_letter}{spec_num(0-...)}
Class_first_letter - первая буква класса клеток, к примеру, E - клетка environment, которая будет выполнять роль обычного оформления; R - клетка для тропинок; T - клетка для башен.
Spec_num - градация чисел от нуля, что просто будут означать определённый класс клетки или её спрайт.
