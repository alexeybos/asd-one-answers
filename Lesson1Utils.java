
public class Lesson1Utils {

    public LinkedList sumEqualLengthLists(LinkedList _firstList, LinkedList _secondList) {
        LinkedList resultList = new LinkedList();
        if (_firstList == null || _secondList == null) {
            return resultList;
        }
        Node nodeFromFirstList = _firstList.head;
        Node nodeFromSecondList = _secondList.head;
        while (nodeFromFirstList != null) {
            if (nodeFromSecondList == null) {
                return resultList;
            }
            nodeFromSecondList = nodeFromSecondList.next;
            nodeFromFirstList = nodeFromFirstList.next;
        }
        if (nodeFromSecondList == null) {
            nodeFromFirstList = _firstList.head;
            nodeFromSecondList = _secondList.head;
            while (nodeFromFirstList != null) {
                resultList.addInTail(new Node(nodeFromFirstList.value + nodeFromSecondList.value));
                nodeFromFirstList = nodeFromFirstList.next;
                nodeFromSecondList = nodeFromSecondList.next;
            }
        }
        return resultList;
    }

}


