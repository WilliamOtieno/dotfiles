
def init_widgets_list():
    widgets_list = [
        widget.Sep(linewidth=0, padding=6, foreground=colors[2], background=colors[0]),
        widget.GroupBox(
            font="mononoki",
            fontsize=14,
            margin_y=3,
            margin_x=0,
            padding_y=4,
            padding_x=5,
            borderwidth=1,
            active=colors[2],
            inactive=colors[2],
            rounded=False,
            highlight_method="block",
            this_current_screen_border=colors[4],
            this_screen_border=colors[1],
            other_current_screen_border=colors[0],
            other_screen_border=colors[0],
            foreground=colors[2],
            background=colors[0],
        ),
        widget.Prompt(
            prompt=prompt,
            font="mononoki",
            padding=10,
            foreground=colors[3],
            background=colors[1],
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.WindowName(
            foreground=colors[4],
            background=colors[0],
            padding=5,
            padding_y=1
        ),
        widget.TextBox(
            text="",
            background=colors[0],
            foreground=colors[5],
            padding=0,
            fontsize=37
        ),
        widget.CPU(
            background=colors[5],
            foreground=colors[2],
            padding=5
        ),
        widget.TextBox(
            text="",
            background=colors[5],
            foreground=colors[4],
            padding=0,
            fontsize=37
        ),
        widget.TextBox(
            text = "💽",
            background = colors[4]
        ),
        widget.Memory(
            background = colors[4],
            padding = 5
        ),
        widget.TextBox(
            text="",
            background=colors[4],
            foreground=colors[5],
            padding=0,
            fontsize=37
        ),
        widget.TextBox(
            text="🌡",
            background = colors[5]
        ),
        widget.ThermalSensor(
            background = colors[5]
        ),
        widget.TextBox(
            text="",
            background=colors[5],
            foreground=colors[4],
            padding=0,
            fontsize=37
        ),
        widget.TextBox(
            text="🔓",
            background = colors[4]
        ),
        widget.CapsNumLockIndicator(
            background=colors[4],
            foreground=colors[2],
            padding=5
        ),
        widget.TextBox(
            text="", background=colors[4], foreground=colors[5], padding=0, fontsize=37
        ),
        widget.CurrentLayoutIcon(
            padding=5,
            foreground=colors[2],
            background=colors[5],
        ),
        widget.CurrentLayout(foreground=colors[2], background=colors[5], padding=5),
        widget.TextBox(
            text="", background=colors[5], foreground=colors[4], padding=0, fontsize=37
        ),
        widget.Sep(linewidth=0, padding=5, foreground=colors[0], background=colors[4]),
        widget.Clock(
            foreground=colors[2], background=colors[4], format="%A, %B %d - %H:%M"
        ),
        widget.Sep(linewidth=0, padding=5, foreground=colors[0], background=colors[4]),
        widget.Systray(background=colors[0], padding=5),
    ]
    return widgets_list
