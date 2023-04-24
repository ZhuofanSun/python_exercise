class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    """双链表"""
    def __init__(self, node=None):
        # 私有属性前加一个下划线，在外部调用对象函数时不需要管私有属性
        """头节点信息外部不需要知道，初始没有所以是空链表。链表中没有任何一个节点就说明第一个节点（self.__head）是none"""
        self.__head = node

    def is_empty(self):
        # 判断为空
        return self.__head is None

    def length(self):
        # 链表长度
        current = self.__head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def travel(self):
        # 遍历整个链表
        current = self.__head
        while current is not None:
            print(current.elem)
            current = current.next

    def add(self, item):
        # 链表头部添加元素
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        # 链表尾部添加元素
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            current = self.__head
            while current.next is not None:
                current = current.next
            current.next = node

    def insert(self, pos, item):
        # 制定位置添加元素
        pre = self.__head
        count = 0
        while count < pos:
            count += 1
            pre = pre.next
        node = Node(item)
        node.next = pre.next
        pre.next = node

    def remove(self, item):
        # 删除节点
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    # 前一个的下一个是我想删掉的指向的下一个，也就是cur的下一个
                    pre.next = cur.next
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        # 查找节点是否存在
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

