import java.util.*;


class Node<T>
{
    public T value;
    public Node<T> next, prev;

    public Node(T _value)
    {
        value = _value;
        next = null;
        prev = null;
    }
}

public class OrderedList<T>
{
    public Node<T> head, tail;
    private boolean _ascending;
    private int _count;

    public OrderedList(boolean asc)
    {
        head = null;
        tail = null;
        _ascending = asc;
        _count = 0;
    }

    public int compare(T v1, T v2)
    {
        if (v1 instanceof Number && v2 instanceof Number) {
            if (((Number) v1).doubleValue() < ((Number) v2).doubleValue()) {
                return -1;
            }
            if (((Number) v1).doubleValue() > ((Number) v2).doubleValue()) {
                return 1;
            }
        }
        if (v1 instanceof String && v2 instanceof String) {
            int result = ((String) v1).trim().compareTo(((String) v2).trim());
            if (result < 0) {
                return -1;
            }
            if (result > 0) {
                return 1;
            }
        }
        return 0;
    }

    public void add(T value)
    {
        _count += 1;
        Node<T> item = new Node<>(value);
        if (head == null) {
            this.head = item;
            this.tail = item;
            this.head.next = null;
            this.head.prev = null;
            return;
        }
        if ((_ascending && compare(this.head.value, value) >= 0) ||
                (!_ascending && compare(value, this.head.value) >= 0)) { //new head value
            item.next = this.head;
            this.head.prev = item;
            this.head = item;
            return;
        }
        if ((_ascending && compare(value, this.tail.value) >= 0) ||
                (!_ascending && compare(this.tail.value, value) >= 0)) { //new tail value
            item.prev = this.tail;
            this.tail.next = item;
            this.tail = item;
            return;
        }
        Node<T> iNode = this.head;
        while ((_ascending && compare(value, iNode.value) > 0) || (!_ascending && compare(value, iNode.value) < 0)) {
            iNode = iNode.next;
        }
        item.next = iNode;
        iNode.prev.next = item;
        item.prev = iNode.prev;
        iNode.prev = item;
    }

    public Node<T> find(T val)
    {
        Node<T> node = this.head;
        for (int i = 0; i < this._count; i++) {
            int compareResult = compare(node.value, val);
            if (compareResult == 0) {
                return node;
            }
            if ((_ascending && compareResult > 0) || (!_ascending && compareResult < 0)) {
                return null;
            }
            node = node.next;
        }
        return null;
    }

    public void delete(T val)
    {
        if (_count == 0) {
            return;
        }
        Node<T> node = find(val);
        if (node != null) {
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
            _count -= 1;
        }

    }

    public void clear(boolean asc)
    {
        _ascending = asc;
        _count = 0;
        this.head = null;
        this.tail = null;
    }

    public int count()
    {
        return _count;
    }

    ArrayList<Node<T>> getAll()
    {
        ArrayList<Node<T>> r = new ArrayList<Node<T>>();
        Node<T> node = head;
        while(node != null)
        {
            r.add(node);
            node = node.next;
        }
        return r;
    }
}



