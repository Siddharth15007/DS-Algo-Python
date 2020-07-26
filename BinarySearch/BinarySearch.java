public class BinarySearch{
    
    public static void main(String[] args) {
        Integer[] list = {20,21,22,23,24,25,33,34,35,44,45,55,56,57,58,59,60,66,67,68,69,70,77,88,99,100,101,102};
        int low = 0;
        int high = list.length;
        int count = 0;
        int searchKey = 88;

        while( low <= high){
            int mid = (low + high) / 2;
            int guess = list[mid];
            if(guess == searchKey){
                System.out.println(guess);
                break;
            }
            if(guess > searchKey){
                high = mid - 1;
                System.out.println("step " + ++count);
            }
            else{
                low = mid + 1;
                System.out.println("step " + ++count);
            }
        }

    }
}