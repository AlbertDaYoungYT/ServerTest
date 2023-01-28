import modules.event.manager
from __main__ import logger
logger.success("Event module Initiated")


def trigger(id, *args):
    event = modules.event.manager.FetchEvent(id)

    if eval(event[3] + event[5] + event[4]):
        try:
            exec(event[6])
            logger.success(f"Event '{id}' triggered")
            return True           
        except Exception as e:
            logger.error(f"Exception in Event '{id}': {e}")
            return False
    else:
        return False