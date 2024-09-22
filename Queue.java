import java.util.*;

public class Queue<T>
{
    public LinkedList<T> queue;

    public Queue()
    {
        queue = new LinkedList<>();
    }

    public void enqueue(T item)
    {
        queue.addFirst(item);
    }

    public T dequeue()
    {
        if (queue.size() == 0) {
            return null;
        }
        return queue.removeLast();
    }

    public int size()
    {
        return queue.size();
    }

}


