class Router:
    def __init__(self, router_id):
        self.router_id = router_id
        self.forwarding_table = {}
    
    def add_neighbor(self, neighbor, interface):
        self.forwarding_table[neighbor] = interface
    
    def forward_multicast_packet(self, source_router, multicast_group):
        if source_router in self.forwarding_table:
            interface = self.forwarding_table[source_router]
            print(f"Router {self.router_id} forwarding multicast packet for group {multicast_group} via interface {interface}")
        else:
            print(f"Router {self.router_id} discarding multicast packet for group {multicast_group}")
        
# Create routers and set up neighbors
r1 = Router(1)
r2 = Router(2)
r3 = Router(3)

r1.add_neighbor(r2.router_id, 'eth0')
r2.add_neighbor(r1.router_id, 'eth1')
r2.add_neighbor(r3.router_id, 'eth0')
r3.add_neighbor(r2.router_id, 'eth1')

# Simulate multicast packet forwarding
multicast_group = '230.0.0.1'
source_router = r1.router_id

r2.forward_multicast_packet(source_router, multicast_group)
r3.forward_multicast_packet(source_router, multicast_group)
