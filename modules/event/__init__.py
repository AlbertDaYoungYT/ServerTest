import modules.event.manager


def trigger(id):
    event = modules.event.manager.FetchEvent(id)

    if eval(event[3] + event[5] + event[4]):
        exec(event[6])
        return True           
    else:
        return False