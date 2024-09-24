import java.util.*;

public class Deque<T>
{
    public LinkedList<T> deque;

    public Deque()
    {
        deque = new LinkedList<>();
    }

    public void addFront(T item)
    {
        deque.addLast(item);
    }

    public void addTail(T item)
    {
        deque.addFirst(item);
    }

    public T removeFront()
    {
        if (size() == 0) {
            return null;
        }
        return deque.removeLast();
    }

    public T removeTail()
    {
        if (size() == 0) {
            return null;
        }
        return deque.removeFirst();
    }

    public int size()
    {
        return deque.size();
    }
}



