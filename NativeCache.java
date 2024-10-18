import java.lang.reflect.Array;

class NativeCache<T>
{
    private static final int STEP = 3;
    public int size;
    public String [] slots;
    public T [] values;
    public int [] hits;

    public NativeCache(int sz, Class clazz) {
        size = sz;
        slots = new String[size];
        hits = new int[size];
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
        int slot = find(key);
        if (slot != -1) {
            values[slot] = value;
            hits[slot] += 1;
            return;
        }
        slot = seekSlot(key);
        if (slot == -1) {
            int min = hits[0];
            int removeIndex = 0;
            for (int i = 1; i < hits.length; i++) {
                if (min > hits[i]) removeIndex = i;
            }
            slots[removeIndex] = null;
            slot = seekSlot(key);
        }
        slots[slot] = key;
        values[slot] = value;
        hits[slot] = 0;
    }

    public T get(String key)
    {
        if (!isKey(key)) {
            return null;
        }
        int slot = find(key);
        hits[slot] += 1;
        return values[slot];
    }

    private int find(String key)
    {
        int slot = hashFun(key);
        for (int i = 0; i <= STEP; i++) {
            for (; slot < size; slot += STEP) {
                if (slots[slot] == key) {
                    return slot;
                }
                if (slots[slot] == null) return -1;
            }
            slot -= size;
        }
        return -1;
    }
}



