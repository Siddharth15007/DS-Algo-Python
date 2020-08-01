/**
 * Array
 */
public class Array {

    public static int[] insertElement(int N, int arr[], int Pos, int X){
        
        //Create New Array of Size N+1
        int[] NewArr = new int[N+1];

        // Now  insert Arr[]'s value in NewArr[] with the X, which we want to insert
        for (int i=0; i<N+1; i++){
            if(i < Pos-1)
                NewArr[i] = arr[i];
            else if(i == Pos -1)
                NewArr[i] = X;
            else
                NewArr[i] = arr[i-1];
        } 
        return NewArr;

    }
    public static int[] removeElement(int arr[], int Pos){
        
        if(arr == null || Pos < 0 || Pos >= arr.length)
            return arr;

        //Create New Array of Size N+1
        int[] NewArr = new int[arr.length - 1];

        // Now  insert Arr[]'s value in NewArr[] with the X, which we want to insert
        for (int i=0,k =0; i<arr.length; i++){
            if(i == Pos){
                continue;
            }
            NewArr[k++] = arr[i];
        }
        return NewArr;
    }

    public static void main(String[] args) {
        // Create Integer Array
        int[] intArr = new int[5];  // similarlly we can create String Array List.
        intArr[0] = 123;
        intArr[1] = 234;
        intArr[2] = 345;
        intArr[3] = 456;
        intArr[4] = 567;

        // Print Integer Without Any Operation Array:
        System.out.println("Before Perform any operation:");
        for (int i=0; i<intArr.length; i++){
            System.out.println(intArr[i]);
        }

        // insert element at Position 2:
        intArr = insertElement(intArr.length, intArr, 2, 678);

        //Print after operation:
        System.out.println("Before Perform Insertion operation:");
        for (int i=0; i<intArr.length; i++){
            System.out.println(intArr[i]);
        }

        intArr = removeElement(intArr, 3);

        //Print after operation:
        System.out.println("Before Perform Deletion operation:");
        for (int i=0; i<intArr.length; i++){
            System.out.println(intArr[i]);
        }
        
    }
}