import java.util.*;

public class LinkedList2
{
    public Node head;
    public Node tail;

    public LinkedList2()
    {
        head = null;
        tail = null;
    }

    public void addInTail(Node _item)
    {
        if (head == null) {
            this.head = _item;
            this.head.next = null;
            this.head.prev = null;
        } else {
            this.tail.next = _item;
            _item.prev = tail;
        }
        this.tail = _item;
    }

    public Node find(int _value)
    {
        Node node = this.head;
        while (node != null) {
            if (node.value == _value) {
                return node;
            }
            node = node.next;
        }
        return null;
    }

    public ArrayList<Node> findAll(int _value)
    {
        ArrayList<Node> nodes = new ArrayList<Node>();
        Node node = this.head;
        while (node != null) {
            if (node.value == _value) {
                nodes.add(node);
            }
            node = node.next;
        }
        return nodes;
    }

    public boolean remove(int _value)
    {
        Node node = this.find(_value);
        if (node != null) {
            nodesAdjusting(node);
            return true;
        }
        return false;
    }

    public void removeAll(int _value)
    {
        ArrayList<Node> nodes = this.findAll(_value);
        for (Node node: nodes) {
            nodesAdjusting(node);
        }
    }

    private void nodesAdjusting(Node node) {
        if (node.prev == null) {
            this.head = node.next;
        } else {
            node.prev.next = node.next;
        }
        if (node.next == null) {
            this.tail = node.prev;
        } else {
            node.next.prev = node.prev;
        }
    }

    public void clear()
    {
        this.head = null;
        this.tail = null;
    }

    public int count()
    {
        Node node = this.head;
        int cnt = 0;
        while (node != null) {
            cnt++;
            node = node.next;
        }
        return cnt;
    }

    public void insertAfter(Node _nodeAfter, Node _nodeToInsert)
    {
        if (_nodeAfter == null) {
            addToHead(_nodeToInsert);
            return;
        }
        Node node = this.head;
        while (node != null) {
            if (node == _nodeAfter) {
                _nodeToInsert.prev = node;
                _nodeToInsert.next = node.next;
                node.next = _nodeToInsert;
                if (_nodeToInsert.next != null) {
                    _nodeToInsert.next.prev = _nodeToInsert;
                } else {
                    this.tail = _nodeToInsert;
                }
            }
            node = node.next;
        }
    }

    public void addToHead(Node _nodeToInsert)
    {
        _nodeToInsert.next = this.head;
        this.head = _nodeToInsert;
        if (this.tail == null) {
            this.tail = _nodeToInsert;
        } else {
            _nodeToInsert.next.prev = _nodeToInsert;
        }
    }

    public void revert() {
        Node node = this.head;
        this.head = this.tail;
        this.tail = node;
        while (node != null) {
            Node next = node.next;
            node.next = node.prev;
            node.prev = next;
            node = next;
        }
    }

    public boolean hasCycles() {

        return false;
    }

    public void sort() {
        LinkedList2 list = mergeSort(this);
        this.head = list.head;
        this.tail = list.tail;
    }

    public LinkedList2 merge(LinkedList2 _list1, LinkedList2 _list2) {
        LinkedList2 resultList = new LinkedList2();
        Node node1 = _list1.head;
        Node node2 = _list2.head;
        while (node1 != null && node2 != null) {
            if (node1.value <= node2.value) {
                resultList.addInTail(new Node(node1.value));
                node1 = node1.next;
            } else {
                resultList.addInTail(new Node(node2.value));
                node2 = node2.next;
            }
        }
        while (node1 != null) {
            resultList.addInTail(new Node(node1.value));
            node1 = node1.next;
        }
        while (node2 != null) {
            resultList.addInTail(new Node(node2.value));
            node2 = node2.next;
        }

        return resultList;
    }

    private LinkedList2 mergeSort(LinkedList2 list) {
        int size = list.count();
        if (size < 2) {
            return list;
        }
        LinkedList2 leftList = new LinkedList2();
        LinkedList2 rightList = new LinkedList2();
        Node node = list.head;
        for (int i = 0; i < size / 2; i++) {
            leftList.addInTail(new Node(node.value));
            node = node.next;
        }
        while (node != null) {
            rightList.addInTail(new Node(node.value));
            node = node.next;
        }

        leftList = mergeSort(leftList);
        rightList = mergeSort(rightList);

        return merge(leftList, rightList);
    }

}

class Node
{
    public int value;
    public Node next;
    public Node prev;

    public Node(int _value)
    {
        value = _value;
        next = null;
        prev = null;
    }
}



