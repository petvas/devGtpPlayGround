import tcod

def draw_character(x, y):
    tcod.console_set_default_foreground(0, tcod.white)
    tcod.console_put_char(0, x, y, '@', tcod.BKGND_NONE)

def clear_character(x, y):
    tcod.console_put_char(0, x, y, ' ', tcod.BKGND_NONE)

def handle_keys(key, player_x, player_y):
    if key.vk == tcod.KEY_UP:
        clear_character(player_x, player_y)
        draw_character(player_x, player_y-1)
        player_y -= 1
    elif key.vk == tcod.KEY_DOWN:
        clear_character(player_x, player_y)
        draw_character(player_x, player_y+1)
        player_y += 1
    elif key.vk == tcod.KEY_LEFT:
        clear_character(player_x, player_y)
        draw_character(player_x-1, player_y)
        player_x -= 1
    elif key.vk == tcod.KEY_RIGHT:
        clear_character(player_x, player_y)
        draw_character(player_x+1, player_y)
        player_x += 1
    return player_x, player_y

main.py<::FILE::>
import tcod
from basics_character import draw_character, clear_character, handle_keys

def main():
    screen_width = 80
    screen_height = 40

    tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(screen_width, screen_height, 'Python 3 libtcod tutorial', False, tcod.RENDERER_SDL2, vsync=True)
    con = tcod.console_new(screen_width, screen_height)

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    while not tcod.console_is_window_closed():
        tcod.console_set_default_foreground(con, tcod.white)
        tcod.console_put_char(con, player_x, player_y, '@', tcod.BKGND_NONE)

        tcod.console_flush()

        clear_character(player_x, player_y)

        for event in tcod.event.wait():
            if event.type == 'QUIT':
                raise SystemExit()
            elif event.type == 'KEYDOWN':
                player_x, player_y = handle_keys(event.sym, player_x, player_y)
                if event.sym == tcod.event.K_ESCAPE:
                    raise SystemExit()

if __name__ == '__main__':
    main()