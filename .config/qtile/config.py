##### IMPORTS #####

import os
import re
import socket
import subprocess
from typing import List  # noqa: F401

from libqtile import bar, hook, layout, widget
from libqtile.command import lazy
from libqtile.config import Click, Drag, Group, Key, Screen

##### DEFINING SOME VARIABLES #####

mod = "mod4"  # Sets mod key to SUPER/WINDOWS
myTerm = "termite"  # My terminal of choice
myConfig = "/home/samarth/.config/qtile/config.py"  # The Qtile config file location

##### KEYBINDINGS #####
keys = [

    ### The essentials

    Key([mod], "Return", lazy.spawn(myTerm)),  # Open terminal
    Key([mod, "shift"], "Return", lazy.spawn("dmenu_run")),  # Dmenu Run Launcher
    Key([mod], "Tab", lazy.next_layout()),  # Toggle through layouts
    Key([mod, "shift"], "c", lazy.window.kill()),  # Kill active window
    Key([mod, "shift"], "r", lazy.restart()),  # Restart Qtile
    Key([mod, "shift"], "q", lazy.shutdown()),  # Shutdown Qtile

    ### Treetab controls

    Key([mod, "control"], "k", lazy.layout.section_up()),  # Move up a section in treetab
    Key([mod, "control"],"j", lazy.layout.section_down()),  # Move down a section in treetab

    ### Window controls

    Key([mod], "k", lazy.layout.down()),  # Switch between windows in current stack pane
    Key([mod], "j", lazy.layout.up()),  # Switch between windows in current stack pane
    Key([mod, "shift"], "k", lazy.layout.shuffle_down()),  # Move windows down in current stack
    Key([mod, "shift"], "j", lazy.layout.shuffle_up()),  # Move windows up in current stack
    Key([mod], "h", lazy.layout.grow(),  # Grow size of current window (XmonadTall)
        lazy.layout.increase_nmaster()),  # Increase number in master pane (Tile)
    Key([mod], "l", lazy.layout.shrink(),  # Shrink size of current window (XmonadTall)
        lazy.layout.decrease_nmaster()),  # Decrease number in master pane (Tile)
    Key([mod], "n", lazy.layout.normalize()),  # Restore all windows to default size ratios
    Key([mod], "m", lazy.layout.maximize()),  # Toggle a window between minimum and maximum sizes
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),  # Toggle floating

    ### Stack controls

    Key([mod, "shift"], "space", lazy.layout.rotate(),  # Swap panes of split stack (Stack)
        lazy.layout.flip()),  # Switch which side main pane occupies (XmonadTall)
    Key([mod], "space", lazy.layout.next()),  # Switch window focus to other pane(s) of stack
    Key([mod, "control"], "Return", lazy.layout.toggle_split()),  # Toggle between split and unsplit sides of stack

    ### Dmenu scripts launched with ALT + CTRL + KEY

    Key(["mod1", "control"], "n", lazy.spawn("networkmanager_dmenu")),
    Key(["mod1", "control"], "s", lazy.spawn("bash /opt/dmenu/dmenu-scrot.sh")),

    ### My applications launched with SUPER + ALT + KEY

    Key([mod, "mod1"], "g", lazy.spawn("gimp")),
    Key([mod, "mod1"], "q", lazy.spawn("qutebrowser")),
    Key([mod, "mod1"], "i", lazy.spawn("modem-manager-gui")),
    Key([mod, "mod1"], "s", lazy.spawn("spotify")),
    Key([mod, "mod1"], "t", lazy.spawn("xterm")),
    Key([mod, "mod1"], "a", lazy.spawn("alacritty")),
    Key([mod, "mod1"], "x", lazy.spawn("firefox")),
    Key([mod, "mod1"], "b", lazy.spawn("brave")),
    Key([mod, "mod1"], "e", lazy.spawn("emacs")),
    Key([mod, "mod1"], "f", lazy.spawn(myTerm + " -e /home/samarth/.config/vifm/scripts/vifmrun ")),
    Key([mod, "mod1"], "m", lazy.spawn(myTerm + " -e mocp")),
]

##### GROUPS #####
group_names = [
    ("WWW", {"layout": "ratiotile"}),
    ("DEV", {"layout": "ratiotile"}),
    ("TERM", {"layout": "ratiotile"}),
    ("SYS", {"layout": "ratiotile"}),
    ("SRV", {"layout": "ratiotile"}),
    ("MUS", {"layout": "ratiotile"}),
    ("GFX", {"layout": "max"}),
    ("VID", {"layout": "max"}),
    ("DOC", {"layout": "max"}),
]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(
        Key([mod], str(i), lazy.group[name].toscreen())
    )  # Switch to another group
    keys.append(
        Key([mod, "shift"], str(i), lazy.window.togroup(name))
    )  # Send current window to another group


##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {
    "border_width": 2,
    "margin": 4,
    "border_focus": "#8fbcbb",
    "border_normal": "#1D2330",
}

##### THE LAYOUTS #####
layouts = [
    # layout.Max(),
    # layout.Stack(num_stacks=2),
    # layout.MonadWide(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Stack(stacks=2, **layout_theme),
    # layout.Columns(**layout_theme),
    layout.RatioTile(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    # layout.TreeTab(
    #     font="Ubuntu",
    #     fontsize=14,
    #     sections=["FIRST", "SECOND"],
    #     section_fontsize=17,
    #     bg_color="141414",
    #     active_bg="90C435",
    #     active_fg="000000",
    #     inactive_bg="384323",
    #     inactive_fg="a0a0a0",
    #     padding_y=5,
    #     section_top=10,
    #     panel_width=300,
    # ),
    layout.Floating(**layout_theme),
]

##### COLORS #####
colors = [
    ["#2b303b", "#2b303b"],
    # ["#8fbcbb", "#8fbcbb"],
    ["#88c0d0", "#88c0d0"],
    ["#eceff4", "#eceff4"],
    ["#ff5555", "#ff5555"],
    ["#b48ead", "#b48ead"],
    ["#7197E7", "#7197E7"],
]  # background color for pacman widget

##### PROMPT #####
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(font="mononoki", fontsize=15, padding=2, background=colors[1])
extension_defaults = widget_defaults.copy()

##### WIDGETS #####


def init_widgets_list():
    widgets_list = [
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.TextBox(
            text = "",
            background = colors[0],
            foreground="#7de1e8",
            fontsize=30
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0]
        ),
        # widget.TextBox(
        #     text = "",
        #     background = colors[0],
        #     foreground=colors[1],
        #     fontsize=30
        # ),
        # widget.Sep(
        #     linewidth=0,
        #     padding=6,
        #     foreground=colors[2],
        #     background=colors[0]
        # ),
        # widget.TextBox(
        #     text = "",
        #     background = colors[0],
        #     foreground=colors[1],
        #     fontsize=30
        # ),
        # widget.Sep(
        #     linewidth=0,
        #     padding=6,
        #     foreground=colors[2],
        #     background=colors[0]
        # ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.TextBox(
            text = "[",
            background = colors[0],
            foreground=colors[1],
        ),
        widget.GroupBox(
            font="mononoki",
            fontsize=14,
            margin_y=4,
            margin_x=0,
            padding_y=5,
            padding_x=5,
            borderwidth=3,
            active="#ffffff",
            inactive=colors[1],
            rounded=True,
            highlight_method="line",
            this_current_screen_border=colors[1],
            this_screen_border=colors[4],
            other_current_screen_border=colors[1],
            other_screen_border=colors[1],
            foreground=colors[1],
            background=colors[0],
        ),
        widget.TextBox(
            text = "]",
            background = colors[0],
            foreground=colors[1],
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            foreground=colors[2],
            background=colors[0]
        ),
        # widget.TextBox(
        #     text = "",
        #     background = colors[0],
        #     foreground=colors[1],
        #     fontsize=30
        # ),
        # widget.Sep(
        #     linewidth=0,
        #     padding=10,
        #     foreground=colors[2],
        #     background=colors[0]
        # ),
        # widget.TextBox(
        #     text = "[",
        #     background = colors[0],
        # ),
        # widget.AGroupBox(
        #     background = colors[0],
        #     border = colors[0],
        #     margin_y = 4
        # ),
        # widget.TextBox(
        #     text = "]",
        #     background = colors[0],
        # ),
        widget.TextBox(
            text = "[",
            background = colors[0],
            foreground="#a3be8c",
        ),
        widget.WindowName(
            foreground="#a3be8c",
            background=colors[0],
            padding=5,
        ),
        widget.TextBox(
            text = "]",
            background = colors[0],
            # foreground = colors[1],
            foreground="#a3be8c",
        ),
        # widget.Sep(
        #     linewidth=0,
        #     padding=10,
        #     foreground=colors[2],
        #     background=colors[0]
        # ),
        # widget.TextBox(
        #     text = "",
        #     background = colors[0],
        #     foreground=colors[1],
        #     fontsize=30
        # ),
        widget.Sep(
            linewidth=0,
            padding=10,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.TextBox(
            text = "[",
            background = colors[0],
            # foreground=colors[1],
            foreground = colors[4]
        ),
        widget.CPU(
            background=colors[0],
            # foreground=colors[1],
            foreground=colors[4],
            padding=5
        ),
        widget.TextBox(
            text = "]",
            background = colors[0],
            # foreground=colors[1],
            foreground = colors[4]
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.TextBox(
            text = "[",
            background = colors[0],
            foreground = "#ebcb8b",
            # foreground=colors[1],
        ),
        widget.Memory(
            background = colors[0],
            padding = 5,
            foreground = "#ebcb8b",
            # foreground=colors[1],
        ),

        widget.TextBox(
            text = "]",
            background = colors[0],
            foreground = "#ebcb8b",
            # foreground=colors[1],
        ),
        # widget.Sep(
        #     linewidth=0,
        #     padding=10,
        #     foreground=colors[2],
        #     background=colors[0]
        # ),
        # widget.TextBox(
        #     text = "[",
        #     background = colors[0],
        #     foreground = "#d08770",
        # ),
        # widget.ThermalSensor(
        #     background = colors[0],
        #     # foreground=colors[1],
        #     foreground = "#d08770",
        # ),
        # widget.TextBox(
        #     text = "]",
        #     background = colors[0],
        #     foreground = "#d08770",
        #     # foreground=colors[1],
        # ),
        # widget.Sep(
        #     linewidth=0,
        #     padding=10,
        #     foreground=colors[2],
        #     background=colors[0]
        # ),
        # widget.TextBox(
        #     text = "[",
        #     background = colors[0],
        #     foreground = "#8cd1ce",
        #     # foreground=colors[1],
        # ),
        # widget.Net(
        #     interface = "wwp0s20f0u4i3",
        #     background = colors[0],
        #     foreground = "8cd1ce",
        #     format = '{down} ↑ ↓ {up}'
        #     # foreground=colors[1],
        # ),
        # widget.TextBox(
        #     text = "]",
        #     background = colors[0],
        #     foreground = "#8cd1ce",
        #     # foreground=colors[1],
        # ),
        widget.Sep(
            linewidth=0,
            padding=10,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.TextBox(
            text = "[",
            background = colors[0],
            foreground = "#5e81ce",
            # foreground=colors[1],
        ),
        widget.Volume(
            volume_up_command="amixer -q sset Master 3%+",
            volume_down_command="amixer -q sset Master 3%-",
            background=colors[0],
            foreground = "#5e81ce",
            # foreground=colors[1],
            padding=5
        ),

        widget.TextBox(
            text = "]",
            background = colors[0],
            foreground = "#5e81ce",
            # foreground=colors[1],
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.TextBox(
            text = "[",
            background = colors[0],
            foreground = "#81a1c1",
            # foreground=colors[1],
        ),
        widget.CurrentLayout(
            foreground = "#81a1c1",
            # foreground=colors[1],
            background=colors[0],
            padding=5
        ),
        widget.TextBox(
            text = "]",
            background = colors[0],
            foreground = "#81a1c1",
            # foreground=colors[1],
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            foreground=colors[0],
            background=colors[0]
        ),
        widget.TextBox(
            text = "[",
            background = colors[0],
            foreground = "#d8dee9",
            # foreground=colors[1],
        ),
        widget.Clock(
            foreground = "#d8dee9",
            # foreground=colors[1],
            background=colors[0],
            format="%A, %B %d - %H:%M"
        ),
        widget.TextBox(
            text = "]",
            background = colors[0],
            foreground = "#d8dee9",
            # foreground=colors[1],
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            foreground=colors[0],
            background=colors[0]
        ),
        widget.Systray(
            background=colors[0],
            padding=5
        ),
    ]
    return widgets_list


##### SCREENS #####


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1  # Slicing removes unwanted widgets on Monitors 1,3

def init_screens():
    return [
        Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.95, size=22)),
    ]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()

##### DRAG FLOATING WINDOWS #####
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

##### FLOATING WINDOWS #####
floating_layout = layout.Floating(
    float_rules=[
        {"wmclass": "confirm"},
        {"wmclass": "dialog"},
        {"wmclass": "download"},
        {"wmclass": "error"},
        {"wmclass": "file_progress"},
        {"wmclass": "notification"},
        {"wmclass": "splash"},
        {"wmclass": "toolbar"},
        {"wmclass": "confirmreset"},  # gitk
        {"wmclass": "makebranch"},  # gitk
        {"wmclass": "maketag"},  # gitk
        {"wname": "branchdialog"},  # gitk
        {"wname": "pinentry"},  # GPG key password entry
        {"wmclass": "ssh-askpass"},  # ssh-askpass
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"

##### STARTUP APPLICATIONS #####
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call(["/home/samarth/.config/qtile/autostart.sh"])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
