class Listener:
    listeners = {}

    def __init__(self, name):
        self.callbacks = []

        if name in Listener.listeners:
            print("Listener already exists:", name)
        Listener.listeners[name] = self

    def subscribe(self, callback):
        self.callbacks.append(callback)

    def remove(self, callback):
        self.callbacks.remove(callback)

    def notify(self, *args, **kwargs):
        for callback in self.callbacks:
            callback(*args, **kwargs)

    @staticmethod
    def Get(name):
        return Listener.listeners[name]
