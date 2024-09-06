import java.util.*;

public class LinkedList
{
    public Node head;
    public Node tail;

    public LinkedList()
    {
        head = null;
        tail = null;
    }

    public void addInTail(Node item) {
        if (this.head == null)
            this.head = item;
        else
            this.tail.next = item;
        this.tail = item;
    }

    public Node find(int value) {
        Node node = this.head;
        while (node != null) {
            if (node.value == value)
                return node;
            node = node.next;
        }
        return null;
    }

    public ArrayList<Node> findAll(int _value) {
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
        Node node = this.head;
        Node previousNode = null;
        while (node != null) {
            if (node.value == _value) {
                if (previousNode == null) {
                    this.head = node.next;
                } else {
                    previousNode.next = node.next;
                }
                if (node.next == null) {
                    this.tail = previousNode;
                }
                return true;
            }
            previousNode = node;
            node = node.next;
        }
        return false;
    }

    public void removeAll(int _value)
    {
        Node node = this.head;
        Node previousNode = null;
        while (node != null) {
            if (node.value == _value) {
                if (previousNode == null) { // head, no previous node
                    this.head = node.next;
                } else {
                    previousNode.next = node.next;
                }
                if (node.next == null) { //tail
                    this.tail = previousNode;
                }
            } else {
                previousNode = node;
            }
            node = node.next;
        }
    }

    public void clear()
    {
        this.head = null;
        this.tail = null;
    }

    public int count()
    {
        int cnt = 0;
        Node node = this.head;
        while (node != null) {
            cnt++;
            node = node.next;
        }
        return cnt;
    }

    public void insertAfter(Node _nodeAfter, Node _nodeToInsert)
    {
        if (_nodeAfter == null) { //change head
            _nodeToInsert.next = this.head;
            this.head = _nodeToInsert;
            if (_nodeToInsert.next == null) {
                this.tail = _nodeToInsert;
            }
            return;
        }
        Node node = this.head;
        while (node != null) {
            if (node == _nodeAfter) {
                _nodeToInsert.next = node.next;
                node.next = _nodeToInsert;
                if (_nodeToInsert.next == null) {
                    this.tail = _nodeToInsert;
                }
                return;
            }
            node = node.next;
        }
    }

}

class Node
{
    public int value;
    public Node next;
    public Node(int _value)
    {
        value = _value;
        next = null;
    }
}


