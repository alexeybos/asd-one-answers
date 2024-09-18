import java.util.*;

public class Stack<T>
{

    //public LinkedList<T> stack;
    public ArrayList<T> stack;

    public Stack()
    {
        stack = new ArrayList<>();
    }

    public int size()
    {
        return stack.size();
    }

    public T pop()
    {
        if (stack.size() == 0) {
            return null;
        }

        return stack.remove(stack.size() - 1);
    }

    public void push(T val)
    {
        stack.add(val);
    }

    public T peek()
    {
        if (stack.size() == 0) {
            return null;
        }
        return stack.get(stack.size() - 1);
    }
}


