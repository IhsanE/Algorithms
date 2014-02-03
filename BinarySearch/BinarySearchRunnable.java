class BinarySearchRunnable {
static public void main (String [] Args){
BinarySearch ob1 = new BinarySearch();
int arr [] = new int [10000];
for (int i = -1;++i<10000;)arr[i] = 20*i; 
System.out.println(ob1.BS(arr,5000,0,9998));
}}
