import asyncio
from aiogram_dialog.tools import render_transitions, render_preview

from dialogs.sg import MainSG
from loader import registry

registry.register_start_handler(MainSG.set_opponent)  # get all windows from root
asyncio.run(render_preview(registry, "diagram/preview.html"))  # render windows preview (async)
render_transitions(registry, filename='diagram/dd')  # render graph with current transitions
