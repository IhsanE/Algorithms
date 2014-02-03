class BinarySearchEXAMPLE {
static public int BS(int arr [],int key, int min, int max){
int mid = (max+min)/2; 
if (key > arr[mid]) return BS(arr,key, mid, max);
else if (key < arr[mid]) return BS(arr,key, min, mid);
else return arr[mid];}
static public void main (String [] Args){
int arr [] = new int [10000];
for (int i = -1;++i<10000;)arr[i] = 20*i; 
System.out.println(BS(arr,5000,0,9998));
}}
