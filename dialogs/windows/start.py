import operator

from aiogram.types import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Row, Cancel, Next, Back, Button, Select, Group
from aiogram_dialog.widgets.text import Format

from dialogs import sg
from dialogs.events.start import set_opponent, add_option, make_choise, invite, opts_complete
from dialogs.getters.start import get_start, get_deeplink, get_waiting, get_options
from dialogs.widgets.lang import Lang as _

set_opponent_win = Window(
    _('Hi✌️ <b>{name}</b>!\nWrite your opponent @nick:'),
    MessageInput(set_opponent, content_types=[ContentType.TEXT]),
    Row(
        Cancel(),
    ),
    state=sg.MainSG.set_opponent,
    getter=get_start,

)

invite_opponent_win = Window(
    _('Send @{nick} the link {link}'),
    Row(
        Next(on_click=invite),
        Back(),
        Cancel(),
    ),
    state=sg.MainSG.invite_link,
    getter=get_deeplink
)

wait_for_join_win = Window(
    _('Wait for `{nick}` join to this discuss..'),
    Row(
        Back(),
        Cancel(),
    ),
    state=sg.MainSG.waiting_for_join,
    getter=get_waiting
)

options_win = Window(
    _('Your options:\n{my_opts}', when='has_my_opts'),
    _('Choose one from {nick} options or ', when='has_opts'),
    _('propose your option:'),
    MessageInput(add_option, content_types=[ContentType.TEXT]),
    Group(
        Select(
            Format("{item}"),
            id="s_opts",
            item_id_getter=str,
            items="opts",
            on_click=make_choise,
            when='has_opts'
        ),
        width=1
    ),
    Row(
        Next(on_click=opts_complete, when='has_my_opts'),
        Cancel(),
    ),
    state=sg.MainSG.options,
    getter=get_options
)

wait_for_choise_win = Window(
    _('Wait for `{nick}` choise or proposal..'),
    Row(
        Back(),
        Cancel(),
    ),
    state=sg.MainSG.waiting_for_choise,
    getter=get_waiting
)
