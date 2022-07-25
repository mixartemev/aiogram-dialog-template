from aiogram.types import Message, CallbackQuery
from aiogram_dialog.manager.protocols import ManagedDialogAdapterProto, DialogManager
from aiogram_dialog.widgets.kbd import Next

from dialogs.getters.start import _get_opts, _get_context
from dialogs.sg import MainSG
from models import UserIds, UserModel


async def switch_invited(_, mi: DialogManager):
    if cmd := mi.event.text.replace('/start', ''):  # logged in by invite link
        user = mi.event.from_user
        data = mi.current_context().dialog_data
        my_id = UserIds(id=user.id)
        user_db: UserModel = await UserModel.get(user.id)
        opponent_id = UserIds(id=int(cmd))
        user_db.ref = opponent_id
        await user_db.save()
        opponent_db = await UserModel.get(int(cmd))
        opponent_db.ref = my_id
        await opponent_db.save()
        data['opponent_id'] = opponent_id.id
        data['options'] = await _get_opts(opponent_id.id, mi.data['state'])
        await mi.bg(opponent_id.id, opponent_id.id).switch_to(MainSG.waiting_for_choise)
        await mi.switch_to(MainSG.options)


async def invite(cb: CallbackQuery, button: Next, mng: DialogManager):
    data = mng.current_context().dialog_data
    if opponent := await UserIds.find_one(UserIds.nick == data['opponent_nick']):
        data['opponent_id'] = opponent.id
        bg = mng.bg(opponent.id, opponent.id, load=True)
        if ctx := await _get_context(opponent.id, mng.data['state']):
            await bg.switch_to(MainSG.waiting_for_choise)
        else:
            await bg.start(MainSG.waiting_for_choise, {'opponent_id': cb.from_user.id})
            # further: because on bg.start don't show the window
            await mng.data['bot'].send_message(opponent.id, 'test hi')
            await bg.switch_to(MainSG.waiting_for_choise)


async def set_opponent(msg: Message, mda: ManagedDialogAdapterProto, mng: DialogManager):
    data = mng.current_context().dialog_data
    data['opponent_nick'] = msg.text.replace('@', '')
    await mda.switch_to(MainSG.invite_link)


async def add_option(msg: Message, mda: ManagedDialogAdapterProto, mng: DialogManager):
    data = mng.current_context().dialog_data
    if data.get('my_opts'):
        data['my_opts'].append(msg.text)
    else:
        data['my_opts'] = [msg.text]


async def opts_complete(cb: CallbackQuery, button: Next, mng: DialogManager):
    data = mng.current_context().dialog_data
    if opponent_id := data.get('opponent_id'):
        bg = mng.bg(opponent_id, opponent_id, load=True)
        await bg.switch_to(MainSG.options)


async def make_choise(cb: CallbackQuery, button, mng: DialogManager, sid: str):
    data = mng.current_context().dialog_data
    opid = data['opponent_id']
    await mng.bg(opid, opid, load=True).done({'res': sid})
    await mng.done({'res': sid})
    await mng.data['bot'].send_message(opid, sid)
    await mng.event.answer(sid, True)
