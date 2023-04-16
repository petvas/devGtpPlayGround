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

if __name__ == '__main__':
    main()