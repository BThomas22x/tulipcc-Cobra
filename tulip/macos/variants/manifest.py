#include("$(MPY_DIR)/../lv_binding_micropython/driver/linux/lv_timer.py")
include("$(MPY_DIR)/extmod/asyncio")
freeze("$(MPY_DIR)/../tulip/shared/py")
freeze("$(MPY_DIR)/../amy", "amy.py")
freeze("$(MPY_DIR)/../amy", "juno.py")

