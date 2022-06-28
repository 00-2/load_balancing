class Connection:
    podURL = -1
    is_finalized = -1
    def set_pod_url(self, podURL_) -> None:
        self.podURL = podURL_
    def close_connection(self):
        self.is_finalized = 1
    def __init__(self) -> None:
        pass