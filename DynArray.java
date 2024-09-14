import java.lang.reflect.Array;

public class DynArray<T>
{
    private static final int INITIAL_CAPACITY = 16;
    private static final int APPEND_MULTIPLIER = 2;
    private static final double REDUCE_MULTIPLIER = 1.5;
    private static final double EMPTY_RATIO = 0.5;
    public T [] array;
    public int count;
    public int capacity;
    Class clazz;

    public DynArray(Class clz)
    {
        clazz = clz;
        count = 0;
        makeArray(INITIAL_CAPACITY);
    }

    public void makeArray(int new_capacity)
    {
        T[] oldArray = array;
        array = (T[]) Array.newInstance(this.clazz, new_capacity);
        if (count > 0) {
            System.arraycopy(oldArray, 0, array, 0, count);
        }
        capacity = new_capacity;
    }

    public T getItem(int index)
    {
        if (index < 0 || index >= count) {
            throw new ArrayIndexOutOfBoundsException();
        }
        return array[index];
    }

    public void append(T itm)
    {
        if (count == capacity) {
            makeArray(capacity * APPEND_MULTIPLIER);
        }
        array[count] = itm;
        count += 1;
    }

    public void insert(T itm, int index)
    {
        if (index < 0 || index > count) {
            throw new ArrayIndexOutOfBoundsException();
        }
        if (index == capacity || count == capacity) {
            makeArray(capacity * APPEND_MULTIPLIER);
        }
        for (int i = count; i > index; i--) {
            array[i] = array[i - 1];
        }
        array[index] = itm;
        count += 1;
    }

    public void remove(int index)
    {
        if (index < 0 || index >= count) {
            throw new ArrayIndexOutOfBoundsException();
        }
        shrinkIfNeed();
        for (int i = index; i < count; i++) {
            array[i] = array[i + 1];
        }
        count -= 1;
    }

    private void shrinkIfNeed() {
        if (capacity == INITIAL_CAPACITY) {
            return;
        }
        if (count - 1 < (int) (capacity * EMPTY_RATIO)) {
            makeArray(Math.max((int) (capacity / REDUCE_MULTIPLIER), INITIAL_CAPACITY));
        }
    }

}



