import tcod

def draw_player(con, x, y):
    tcod.console_put_char(con, x, y, '@', tcod.BKGND_NONE)

def clear_player(con, x, y):
    tcod.console_put_char(con, x, y, ' ', tcod.BKGND_NONE)

def handle_keys():
    key = tcod.console_check_for_keypress()
    if key.vk == tcod.KEY_ESCAPE:
        return True  # exit game
    # movement keys
    if key.vk == tcod.KEY_UP:
        return (0, -1)
    elif key.vk == tcod.KEY_DOWN:
        return (0, 1)
    elif key.vk == tcod.KEY_LEFT:
        return (-1, 0)
    elif key.vk == tcod.KEY_RIGHT:
        return (1, 0)
    return False

def move_player(x, y, dx, dy):
    return (x + dx, y + dy)

def handle_events(con, player_x, player_y):
    for event in tcod.event.get():
        if event.type == 'QUIT':
            raise SystemExit()
        elif event.type == 'KEYDOWN':
            move = handle_keys()
            if move:
                clear_player(con, player_x, player_y)
                player_x, player_y = move_player(player_x, player_y, move[0], move[1])
                draw_player(con, player_x, player_y)
    return player_x, player_y

def main():
    con = tcod.console.Console(80, 50)
    player_x, player_y = 40, 25
    while True:
        tcod.console_flush()
        clear_player(con, player_x, player_y)
        player_x, player_y = handle_events(con, player_x, player_y)
        draw_player(con, player_x, player_y)

basics_map.py<::FILE::>
import tcod

def main():
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    colors = {
        'dark_wall': tcod.Color(0, 0, 100),
        'dark_ground': tcod.Color(50, 50, 150),
        'light_wall': tcod.Color(130, 110, 50),
        'light_ground': tcod.Color(200, 180, 50),
    }

    dungeon_map = generate_dungeon(map_width, map_height)

    with tcod.console_init_root(screen_width, screen_height, 'libtcod tutorial', False) as root_console:
        while True:
            draw_con(root_console, dungeon_map, colors, screen_width, screen_height)
            tcod.console_flush()

            for event in tcod.event.wait():
                if event.type == 'QUIT':
                    raise SystemExit()

if __name__ == '__main__':
    main()

basics_engine.py<::FILE::>
import tcod

def main():
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    with tcod.console_init_root(screen_width, screen_height, 'libtcod tutorial', False) as root_console:
        while True:
            root_console.print(x=player_x, y=player_y, string='@', fg=tcod.white, bg=tcod.black)
            tcod.console_flush()

            for event in tcod.event.wait():
                if event.type == 'QUIT':
                    raise SystemExit()
                elif event.type == 'KEYDOWN':
                    if event.sym == tcod.event.K_ESCAPE:
                        raise SystemExit()
                    elif event.sym == tcod.event.K_UP:
                        player_y -= 1
                    elif event.sym == tcod.event.K_DOWN:
                        player_y += 1
                    elif event.sym == tcod.event.K_LEFT:
                        player_x -= 1
                    elif event.sym == tcod.event.K_RIGHT:
                        player_x += 1

if __name__ == '__main__':
    main()

basics_input.py<::FILE::>
import tcod

def main():
    screen_width = 80
    screen_height = 50

    with tcod.console_init_root(screen_width, screen_height, 'libtcod tutorial', False) as root_console:
        while True:
            root_console.print(x=1, y=1, string='@', fg=tcod.white, bg=tcod.black)
            tcod.console_flush()

            for event in tcod.event.wait():
                if event.type == 'QUIT':
                    raise SystemExit()
                elif event.type == 'KEYDOWN':
                    print(event)  # print the event to the console

if __name__ == '__main__':
    main()

basics_tileset.py<::FILE::>
import tcod

def main():
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet('dejavu10x10_gs_tc.png', 32, 8, tcod.tileset.CHARMAP_TCOD)

    with tcod.console_init_root(screen_width, screen_height, 'libtcod tutorial', False, renderer=tcod.RENDERER_SDL2, tileset=tileset) as root_console:
        while True:
            root_console.print(x=1, y=1, string='@', fg=tcod.white, bg=tcod.black)
            tcod.console_flush()

            for event in tcod.event.wait():
                if event.type == 'QUIT':
                    raise SystemExit()

if __name__ == '__main__':
    main()

basics_menus.py<::FILE::>
import tcod

def main():
    screen_width = 80
    screen_height = 50

    with tcod.console_init_root(screen_width, screen_height, 'libtcod tutorial', False) as root_console:
        while True:
            root_console.print(x=1, y=1, string='@', fg=tcod.white, bg=tcod.black)
            tcod.console_flush()

            key = tcod.console_wait_for_keypress(True)
            if key.vk == tcod.KEY_ESCAPE:
                raise SystemExit()

if __name__ == '__main__':
    main()