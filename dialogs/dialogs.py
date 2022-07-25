from aiogram_dialog import Dialog

from .events.start import switch_invited  # , choosed
from .windows import start

start_dlg = Dialog(
    start.set_opponent_win,
    start.invite_opponent_win,
    start.options_win,
    start.wait_for_choise_win,
    start.wait_for_join_win,
    # start.solved_win,
    on_start=switch_invited,
    # on_close=choosed,
)
