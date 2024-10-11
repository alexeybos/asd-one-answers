import java.util.*;

public class PowerSet
{
    public Map<String, Object> set;

    public PowerSet()
    {
        set = new HashMap<>(20000);
    }

    public int size()
    {
        return set.size();
    }


    public void put(String value)
    {
        set.put(value, 0);
    }

    public boolean get(String value)
    {
        return set.containsKey(value);
    }

    public boolean remove(String value)
    {
        boolean result = set.containsKey(value);
        set.remove(value);
        return result;
    }

    public PowerSet intersection(PowerSet set2)
    {
        PowerSet result = new PowerSet();
        for (String val: set2.set.keySet()) {
            if (set.containsKey(val)) {
                result.put(val);
            }
        }
        return result;
    }

    public PowerSet union(PowerSet set2)
    {
        PowerSet result = new PowerSet();
        for (String val: set.keySet()) {
            result.put(val);
        }
        for (String val: set2.set.keySet()) {
            result.put(val);
        }
        return result;
    }

    public PowerSet difference(PowerSet set2)
    {
        PowerSet result = new PowerSet();
        for (String val: set.keySet()) {
            if (!set2.set.containsKey(val)) {
                result.put(val);
            }
        }
        return result;
    }

    public boolean isSubset(PowerSet set2)
    {
        PowerSet diff = set2.difference(this);
        return diff.size() == 0;
    }

    public boolean equals(PowerSet set2)
    {
        if (set.size() != set2.size()) {
            return false;
        }
        PowerSet diff = set2.difference(this);
        return diff.size() == 0;
    }
}



