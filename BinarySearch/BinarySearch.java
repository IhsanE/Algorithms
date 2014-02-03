class BinarySearch {
BinarySearch(){};
static public int BS(int arr [],int key, int min, int max){
int mid = (max+min)/2; 
if (key > arr[mid]) return BS(arr,key, mid, max);
else if (key < arr[mid]) return BS(arr,key, min, mid);
else return arr[mid];}}
