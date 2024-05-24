
# from aiogram.fsm.context import FSMContext

# from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
no_redis = MemoryStorage()


# Cоздаем класс, наследуемый от StatesGroup, для группы состояний нашей FSM
class FSM_IN_GAME(StatesGroup):
    after_start = State()  # Состояние вне игры
    in_game = State()        # Состояние в игре


