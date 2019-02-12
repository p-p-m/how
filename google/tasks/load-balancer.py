# https://www.lintcode.com/problem/load-balancer/description

class Node:
    def __init__(self, value):
        self.value = value
        self.next = self
        self.prev = self


class LoadBalancer:

    def __init__(self):
        self.servers = {}
        self.current = None

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        if server_id in self.servers:
            return False

        server = Node(server_id)
        self.servers[server_id] = server

        if self.current is None:
            self.current = server
        else:
            server.next = self.current.next
            server.prev = self.current
            self.current.next.prev = server
            self.current.next = server
        return True

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        if server_id not in self.servers:
            return False

        server = self.servers[server_id]
        prev = server.prev
        next = server.next
        prev.next = next
        next.prev = prev

        del self.servers[server_id]
        return True

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        self.current = self.current.next
        return self.current.value


lb = LoadBalancer()
lb.add(1)
lb.add(2)
lb.add(3)

for i in range(10):
    print lb.pick()

lb.remove(3)


for i in range(10):
    print lb.pick()