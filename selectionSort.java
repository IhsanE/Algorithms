import java.util.Arrays;
import java.util.Vector;

public class selectionSort {
	
static public Vector <Integer> ss (int [] a, Vector<Integer> ret){
	
	if (a.length < 1) return ret;
	else{
		int min = a[0];
		int index = 0;
		for (int i = 1; i < a.length; i++)
			if (min > a[i]){
				min = a[i];
				index = i;
				}
		
		ret.add(min);
		a[index] = a[0];
		a[0] = min;
		
		return ss (Arrays.copyOfRange(a, 1, a.length),ret);
						
		
	}
	
	
}
	
public static void main (String [] args){
	int [] a = {5,4,60,3,2,1,9,10};
	System.out.println(ss(a,new Vector <Integer>()));
	
}
}
