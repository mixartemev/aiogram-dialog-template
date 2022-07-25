from aiogram.dispatcher.fsm.context import FSMContext
from aiogram_dialog import DialogManager

from models import UserModel


async def _get_opts(opponent_id: int, state: FSMContext):
    ctx = await _get_context(opponent_id, state)
    return ctx['dialog_data'].get('my_opts', []) if ctx else []


async def _get_context(uid: int, state: FSMContext):
    from aiogram.dispatcher.fsm.storage.base import StorageKey
    stk = StorageKey(state.bot.id, uid, uid, 'aiogd:stack:')
    if data := await state.storage.get_data(state.bot, stk):
        stk = StorageKey(state.bot.id, uid, uid, 'aiogd:context:'+data['intents'][-1])
        data = await state.storage.get_data(state.bot, stk)
        return data


async def get_start(dialog_manager: DialogManager, state: FSMContext, **kwargs):
    user = dialog_manager.event.from_user
    return {
        'name': user.full_name,
    }


async def get_deeplink(dialog_manager: DialogManager, state: FSMContext, **kwargs):
    user = dialog_manager.event.from_user
    data = dialog_manager.current_context().dialog_data
    return {
        'nick': data["opponent_nick"],
        'link': f'https://t.me/deadlocksolverbot?start={user.id}',
    }


async def get_options(dialog_manager: DialogManager, state: FSMContext, **kwargs):
    data = dialog_manager.current_context().dialog_data
    if opponent_id := data.get('opponent_id'):
        data['options'] = await _get_opts(opponent_id, state)
    options = data.get('options')
    my_opts = data.get('my_opts', [])
    op_nick = data.get('opponent_nick') or 'your opponent'
    return {
        'nick': op_nick,
        'has_my_opts': bool(my_opts),
        'has_opts': bool(options),
        'my_opts': " - " + "\n - ".join(my_opts) + "\n",
        'opts': options,
    }


async def get_waiting(dialog_manager: DialogManager, state: FSMContext, **kwargs):
    data = dialog_manager.current_context().dialog_data
    if start_data := dialog_manager.current_context().start_data:
        data['opponent_id'] = start_data['opponent_id']
    nick = data.get('opponent_nick') or (await UserModel.get(data.get('opponent_id'))).nick
    return {
        'nick': nick,
    }
