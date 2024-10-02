public class HashTable
{
    public int size;
    public int step;
    public String [] slots;

    public int count;

    public HashTable(int sz, int stp)
    {
        size = sz;
        step = stp;
        slots = new String[size];
        for(int i=0; i<size; i++) slots[i] = null;
        count = 0;
    }

    public int hashFun(String value)
    {
        byte[] chars = value.getBytes();
        int sum = 0;
        for (byte aChar : chars) {
            sum += aChar;
        }
        return sum%size;
    }

    public int seekSlot(String value)
    {
        int slot = hashFun(value);
        for (int i = 0; i <= step; i++) {
            for (; slot < size; slot += step) {
                if (slots[slot] == null) return slot;
            }
            slot -= size;
        }
        return -1;
    }

    public int put(String value)
    {
        if (count == size) {
            return -1;
        }
        int slot = seekSlot(value);
        if (slot == -1) return -1;
        slots[slot] = value;
        count += 1;
        return slot;
    }

    public int find(String value)
    {
        int slot = hashFun(value);
        for (int i = 0; i <= step; i++) {
            for (; slot < size; slot += step) {
                //if (Objects.equals(slots[slot], value)) return slot;
                if (slots[slot] == value) return slot;
                if (slots[slot] == null) return -1;
            }
            slot -= size;
        }
        return -1;
    }
}



