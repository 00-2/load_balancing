MAX_CONNECTIONS = 100
# server pod entity
class Pod:
    url = "" 
    is_active = True
    _max_connections = MAX_CONNECTIONS
    _connection_count = 0
    def __init__(self, url_) -> None:
        self.url = url_
        #TODO check is url ping
    def create_connection(self):
        self._connection_count += 1
    # TODO ON CREATE CONNECTION -> connection_count++
    # TODO on async holder return -> connection_count--
