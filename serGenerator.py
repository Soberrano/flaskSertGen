import pandas as pd
from PIL import Image, ImageDraw, ImageFont

def sertGeneratorList(data, kvantOrCube):
    name1_list = data["name1"].tolist()
    name2_list = data["name2"].tolist()
    patronymic_list = data["patronymic"].tolist()
    status_list = data["status"].tolist()
    kvant_list = data["kvantum"].tolist()
    mod_list = data["mod"].tolist()
    hour_list = data["hour"].tolist()
    number_list = data["number"].tolist()

    count = len(name1_list)
    for i in range(len(name1_list)):
        sert_type = 0
        if kvantOrCube == 'kvant':
            # Кванториум
            im_nice = Image.open(r'static/img/с отличием.png')
            im = Image.open(r'static/img/обычный.png')
            im_none = Image.open(r'static/img/Справка.png')
        else:
            #IT - Cube
            im_nice = Image.open(r'static/img/куб/С отличием.png')
            im = Image.open(r'static/img/куб/Обычный.png')
            im_none = Image.open(r'static/img/Справка.png')


        if status_list[i].lower() == 'сертификат с отличием':
            status_list[i] = "Успешно прошёл(-ла) обучение по\n" \
                             "дополнительной общеобразовательной\n" \
                             "общеразвивающей программе"
            sert_type = 0
            count -= 1
        elif status_list[i].lower() == 'сертификат':
            status_list[i] = "прошёл(-ла) обучение по\n" \
                             "дополнительной общеобразовательной\n" \
                             "общеразвивающей программе"
            sert_type = 1
            count -= 1
        elif status_list[i].lower() == 'справка':
            status_list[i] = "прослушал(-ла) курс по\n" \
                             "дополнительной общеобразовательной\n" \
                             "общеразвивающей программе"
            sert_type = 2
            count -= 1
        else:
            count -= 1
            continue

        hight = 1250
        w, h = im.size
        # цвет текста, RGB
        text_color = (124, 153, 178)
        text_color_small = (0, 0, 0)
        font = ImageFont.truetype("fonts/RussoOne-Regular.ttf", 70)
        fontSmall = ImageFont.truetype('fonts/Roboto-Light.ttf', 35)

        if sert_type == 0:
            img2 = im_nice.copy()
            text_color = (84, 150, 155)
        elif sert_type == 1:
            img2 = im.copy()
            text_color = (124, 153, 178)
        else:
            img2 = im_none.copy()

        name = name1_list[i] + " " + name2_list[i]
        hour = f'Объем часов - {hour_list[i]} ч.'
        if type(number_list[i]) == float:
            number_list[i] = ""

        # определяете объект для рисования
        draw = ImageDraw.Draw(img2)

        # добавляем текст
        draw.text((1400, hight - 775), name, text_color, font, anchor="ms", stroke_width=1, stroke_fill=text_color)
        draw.text((1400, hight - 700), patronymic_list[i], text_color, font, anchor="ms", stroke_width=1)
        draw.text((1400, hight - 600), status_list[i], text_color_small, fontSmall, anchor="ms", align="center")
        draw.text((1400, hight - 480), kvant_list[i], text_color_small, fontSmall, anchor="ms")
        draw.text((1400, hight - 430), mod_list[i], text_color_small, fontSmall, anchor="ms")
        draw.text((900, hight - 300), hour, text_color_small, fontSmall, anchor="ms")
        draw.text((350, 1400), str(number_list[i]), (20, 20, 20), font=ImageFont.truetype('fonts/Roboto-Light.ttf', 25),
                  anchor="ms")

        # сохраняем новое изображение
        img2.save("uploads/certificate_" + name + ".pdf")

        print(f"{count} + {name}")
    return len(name1_list)


def sertGeneratorSingle(name1_list,name2_list,patronymic_list,status_list,kvant_list,mod_list,hour_list,number_list,kvantOrCube):
    print(name1_list)
    sert_type = 1
    if kvantOrCube == 'kvant':
        # Кванториум
        im_nice = Image.open(r'static/img/с отличием.png')
        im = Image.open(r'static/img/обычный.png')
        im_none = Image.open(r'static/img/Справка.png')
    else:
        # IT - Cube
        im_nice = Image.open(r'static/img/куб/С отличием.png')
        im = Image.open(r'static/img/куб/Обычный.png')
        im_none = Image.open(r'static/img/Справка.png')

    if status_list.lower() == 'сертификат с отличием':
        status_list = "Успешно прошёл(-ла) обучение по\n" \
                      "дополнительной общеобразовательной\n" \
                      "общеразвивающей программе"
        sert_type = 0
    elif status_list.lower() == 'сертификат':
        status_list = "прошёл(-ла) обучение по\n" \
                      "дополнительной общеобразовательной\n" \
                      "общеразвивающей программе"
        sert_type = 1
    else:
        status_list = "прослушал(-ла) курс по\n" \
                      "дополнительной общеобразовательной\n" \
                      "общеразвивающей программе"
        sert_type = 2

    hight = 1250
    w, h = im.size
    # цвет текста, RGB
    text_color = (124, 153, 178)
    text_color_small = (0, 0, 0)
    font = ImageFont.truetype("fonts/RussoOne-Regular.ttf", 70)
    fontSmall = ImageFont.truetype('fonts/Roboto-Light.ttf', 35)

    if sert_type == 0:
        img2 = im_nice.copy()
        text_color = (84, 150, 155)
    elif sert_type == 1:
        img2 = im.copy()
        text_color = (124, 153, 178)
    else:
        img2 = im_none.copy()

    name = name1_list + " " + name2_list
    hour = f'Объем часов - {hour_list} ч.'
    if type(number_list) == float:
        number_list = ""

    # определяете объект для рисования
    draw = ImageDraw.Draw(img2)

    # добавляем текст
    draw.text((1400, hight - 775), name, text_color, font, anchor="ms", stroke_width=1, stroke_fill=text_color)
    draw.text((1400, hight - 700), patronymic_list, text_color, font, anchor="ms", stroke_width=1)
    draw.text((1400, hight - 600), status_list, text_color_small, fontSmall, anchor="ms", align="center")
    draw.text((1400, hight - 480), kvant_list, text_color_small, fontSmall, anchor="ms")
    draw.text((1400, hight - 430), mod_list, text_color_small, fontSmall, anchor="ms")
    draw.text((900, hight - 300), hour, text_color_small, fontSmall, anchor="ms")
    draw.text((350, 1400), str(number_list), (20, 20, 20), font=ImageFont.truetype('fonts/Roboto-Light.ttf', 25),
              anchor="ms")
    # сохраняем новое изображение
    img2.save("uploads/certificate_" + name + ".pdf")
    return(name1_list)
