from libqtile import bar, layout, widget, hook
from libqtile.config import Key, Group, Match
from libqtile.lazy import lazy
from libqtile import qtile

# Define modifier key
mod = "mod4"  # Super/Windows key

# Key bindings
keys = [
    Key([mod], "x", lazy.spawn("~/.config/rofi/powermenu.sh"), desc="Power menu"),
    Key([mod], "d", lazy.spawn("rofi -show drun -theme ~/.config/rofi/black_blue.rasi"), desc="Launch Rofi"),
    Key([mod], "f", lazy.spawn("thunar"), desc="Launch Thunar"),
    Key([mod], "w", lazy.spawn("floorp"), desc="Launch Floorp browser"),
]

# Define groups
groups = [Group(i) for i in "123456789"]

for i, group in enumerate(groups, 1):
    keys.append(Key([mod], str(i), lazy.group[group.name].toscreen()))  # Switch to group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(group.name)))  # Move window to group

# Layouts
layouts = [
    layout.MonadTall(margin=8, border_focus="#a3be8c", border_normal="#4c566a"),
    layout.Max(),
]

# No top bar (using Polybar instead)
screens = []

# Floating rules
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(title="Confirmation"),
        Match(wm_class="arandr"),
    ]
)

# Hooks
@hook.subscribe.startup_once
def autostart():
    import subprocess
    subprocess.Popen(["polybar", "topbar"])

# Configurations
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"  # For Java UI compatibility
