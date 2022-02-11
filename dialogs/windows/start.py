from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Row, Cancel

from dialogs import sg
from dialogs.getters.start import get_home
from dialogs.widgets.lang import Lang as _

home_win = Window(
    _('Hi', '✌️ <b>{name}</b>!'),
    Row(
        Cancel(),
    ),
    state=sg.MainSG.home,
    getter=get_home
)
