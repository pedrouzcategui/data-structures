package chapter10binarysearch;

public class recursiveImplementation {
    public static void main(String[] args){
        int numbers[] = {1,2,3,4,5,6};
        int n = numbers.length;
        BinarySearch bs = new BinarySearch();
        int result = bs.binarySearch(numbers, 0, n-1, 3);
        if(result == -1){
            System.out.println("Not found");
        } else {
            System.out.println(result);
        }
    }
}

class BinarySearch {
    public int binarySearch(int arr[], int lower, int higher, int element){
        if(higher >= lower){
            int mid = lower + higher / 2;
            if(element == arr[mid]){
                return mid;
            }
            if(element > arr[mid]){
                return this.binarySearch(arr, mid+1, higher, element);
            }    
            return this.binarySearch(arr, lower, mid-1, element);
        }
        return -1;
    }
}