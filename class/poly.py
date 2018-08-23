class Node(object):
    def __init__(self, power, coefficient):
        self.coefficient = coefficient
        self.power = power
        self.next = None
class Polynomial:
    def __init__(self, power=None, coefficient=None):
        if power is None:
            self._Head = None
        else:
            self._Head = Node(power, coefficient)
        self._Tail = self._Head
    def append(self, power, coefficient): 
         #if coefficient != 0:##this coeff need 0#
        newNode = Node(power, coefficient)
        if self._Head is None:
            self._Head = newNode
        else:
            self._Tail.next = newNode
        self._Tail = newNode#new node all#
    def __add__(self, nextPoly):
        outcomePoly = Polynomial()
        node1 = self._Head
        node2 = nextPoly._Head        
        while node1 is not None and node2 is not None:
            if node1.power > node2.power:
                power = node1.power
                coefficient = node1.coefficient
                node1 = node1.next
            elif node1.power < node2.power:
                power = node2.power
                coefficient = node2.coefficient
                node2 = node2.next
            else:
                power = node1.power
                coefficient = node1.coefficient + node2.coefficient
                node1 = node1.next
                node2 = node2.next

            outcomePoly.append(power, coefficient)
        while node1 is not None:
            outcomePoly.append(node1.power, node1.coefficient)
            node1 = node1.next
        while node2 is not None:
            outcomePoly.append(node2.power, node2.coefficient)
            node2 = node2.next
        return outcomePoly
    def printPoly(self):
        Node = self._Head
        coeff = []
        if Node is None:
            print(0)
        else:
            while Node is not None:
                coeff.append(Node.coefficient)
                Node = Node.next
            print(' '.join(str(i) for i in coeff))
    def Multiply1(self, Node2):
        newPoly = Polynomial()
        Node1 = self._Head
        while Node1 is not None:
            newpower = Node1.power + Node2.power
            newCoefficient = Node1.coefficient * Node2.coefficient
            newPoly.append(newpower, newCoefficient)
            Node1 = Node1.next
        return newPoly
    def __mul__(self, nextPoly):
        node = self._Head
        outcomePoly = Polynomial()         
        while node is not None:
            Poly1 = nextPoly.Multiply1(node)
            outcomePoly += Poly1
            node = node.next
        return outcomePoly
poly1 = [int(x) for x in input().split()]#int(x) for x#
poly2 = [int(x) for x in input().split()]
leftPoly = Polynomial()
rightPoly = Polynomial()
index1 = len(poly1)
index2 = len(poly2)
for i in range(0,len(poly1)):
    index1 = index1 - 1
    leftPoly = leftPoly + Polynomial(index1,poly1[i])#power,coeff#
for i in range(0,len(poly2)):
    index2 = index2 - 1
    rightPoly = rightPoly + Polynomial(index2,poly2[i])
add = leftPoly + rightPoly
add.printPoly()
