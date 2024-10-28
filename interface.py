import dearpygui.dearpygui as dpg
from index import create_cup


def paint_cup():
    with dpg.texture_registry(show=False):
        dpg.delete_item('cup_texture')
        dpg.delete_item('cup_image')
        name_f = 'cup.png'
        create_cup(name_f)
        width, height, _, data = dpg.load_image(f'./{name_f}')
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="cup_texture")
        dpg.add_image(tag='cup_image', texture_tag='cup_texture', parent='main_wind')


def main():
    dpg.create_context()
    dpg.create_viewport(title='Random Cup', width=530, height=600)

    with dpg.font_registry():
        with dpg.font("./LiteralRegular.otf", 20, default_font=True, tag="rus_font") as f:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

    with dpg.window(tag='main_wind'):
        dpg.add_button(label="Создать чашку", callback=paint_cup)
        dpg.add_text(tag='cup_texture')
        dpg.add_text(tag='cup_image')

    dpg.bind_font("rus_font")

    dpg.set_primary_window(window='main_wind', value=True)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == '__main__':
    main()