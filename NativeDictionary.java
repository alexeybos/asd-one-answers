import java.lang.reflect.Array;

class NativeDictionary<T>
{
    private static final int STEP = 3;
    public int size;
    public String [] slots;
    public T [] values;

    public NativeDictionary(int sz, Class clazz)
    {
        size = sz;
        slots = new String[size];
        values = (T[]) Array.newInstance(clazz, this.size);
    }

    public int hashFun(String key)
    {
        byte[] chars = key.getBytes();
        int sum = 0;
        for (byte aChar : chars) {
            sum += aChar;
        }
        return sum%size;
    }

    private int seekSlot(String key)
    {
        int slot = hashFun(key);
        for (int i = 0; i <= STEP; i++) {
            for (; slot < size; slot += STEP) {
                if (slots[slot] == null) return slot;
            }
            slot -= size;
        }
        return -1;
    }

    public boolean isKey(String key)
    {
        return !(find(key) < 0);
    }

    public void put(String key, T value)
    {
        if (!isKey(key)) {
            int slot = seekSlot(key);
            slots[slot] = key;
            values[slot] = value;
            return;
        }
        int slot = find(key);
        values[slot] = value;
    }

    public T get(String key)
    {
        if (!isKey(key)) {
            return null;
        }
        int slot = find(key);
        return values[slot];
    }

    private int find(String key)
    {
        int slot = hashFun(key);
        for (int i = 0; i <= STEP; i++) {
            for (; slot < size; slot += STEP) {
                if (slots[slot] == key) return slot;
                if (slots[slot] == null) return -1;
            }
            slot -= size;
        }
        return -1;
    }
}



