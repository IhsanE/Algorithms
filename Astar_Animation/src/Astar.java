/*************************************  
		Developer: Ihsan Etwaroo
		Time Used: 4hours
		Date: 07/11/2013
		Algorithm: A* Search 
*************************************/

import java.applet.*;
import java.awt.*;
import java.math.*;
import java.util.*;
public class Astar extends Applet {
	int boxSize;
	int gridX[];
	int gridY[];
	int G[][];
	double H[];
	int start;
	int end;
	int x;
	int y;
	public void init() {
		boxSize=10;
		gridX = new int[100];
		gridY = new int[100];
		start = 0;
		end = 37;
		x = 0;
		y = 0;
		for (int i = 0; i < 100; ++i) {
			if (i % 10 == 0) {
				y += 10;
				x = 0;
}
			x += 10;
			gridX[i] = x;
			gridY[i] = y;
}
		G = dGen(10);
		H = hGen(10, end);
}
	public void paint(Graphics ge) {
		ge.fillRect(gridX[end], gridY[end], boxSize,boxSize);
		for (int i = 0; i < 100; ++i) {
			ge.setColor(Color.black);
			ge.drawRect(gridX[i], gridY[i], boxSize, boxSize);
}
		ArrayList<Double> F = new ArrayList<Double>();
		ArrayList<String> V = new ArrayList<String>();
		ArrayList<Integer> GG = new ArrayList<Integer>();
		F.add(H[0]);
		V.add("00");
		GG.add(0);
		while (1 == 1) {
			try {
				Thread.sleep(500);
} 
			catch (InterruptedException e) {
				
			e.printStackTrace();}
			ArrayList<Integer> temp = (ArrayList<Integer>) F.clone();
			Collections.sort(F);
			double f = F.get(0);
			F.remove(0);
			int index = temp.indexOf(f);
			String v = V.get(index);
			int g = GG.get(index);
			V.remove(index);
			GG.remove(index);
			ge.setColor(Color.yellow);
			ge.fillRect(
					gridX[Integer.parseInt(v.substring(v.length() - 2))],
					gridY[Integer.parseInt(v.substring(v.length() - 2))], boxSize, boxSize);

			if (Integer.parseInt(v.substring(v.length() - 2)) == end) {
				ge.setColor(Color.black);
				ge.drawString("Path Sequence: " + v, 0,130);
				ge.drawString("Path Length: "+v.length()/2, 0,150);
				ge.setColor(Color.green);
				for(String i :v.split("(?<=\\G..)")){
					ge.fillRect(gridX[Integer.parseInt(i)],gridY[Integer.parseInt(i)] , boxSize, boxSize);
}
				break;
}                       else {
				for (int edges = 0; edges < G.length; ++edges) {
					if (G[Integer.parseInt(v.substring(v.length() - 2))][edges] != 100
							&& G[Integer.parseInt(v.substring(v.length() - 2))][edges] != 0) {
						
						
						F.add(H[edges]
								+ G[Integer.parseInt(v.substring(v.length() - 2))][edges]
								+ g);
						if (Integer.toString(edges).length() ==1 )V.add(v +"0"+ Integer.toString(edges));
						else V.add(v + Integer.toString(edges));
						GG.add(G[Integer.parseInt(v.substring(v.length() - 2))][edges]
								+ g);
}}}}
		ge.setColor(Color.red);
		ge.fillRect(gridX[end], gridY[end], boxSize,boxSize);
		try {
			Thread.sleep(9999999);
}               catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
}}
	public int[][] dGen(int dimension) {          
		int nNum = dimension * dimension;
		int retArray[][];
		int count;
		count = -1;
		retArray = new int[nNum][nNum];
		for (int i = 0; i < nNum; ++i) {
			for (int j = 0; j < nNum; ++j) {
				if (Math.abs(i - j) == 10){
					retArray[i][j] = 1;
} 
				else if(Integer.toString(i).length()==2 &&  Integer.toString(j).length()==2 ){
					if (Math.abs(Math.floor(i/10)-Math.floor(j/10))==0 && Math.abs(i-j)==1)retArray[i][j] = 1;
}
				else if(Integer.toString(i).length()==1 &&  Integer.toString(j).length()==1 ){
					if (Math.abs(i-j)==1)retArray[i][j] = 1;
					
				}
				else {
					retArray[i][j] = 100;
}}}
		return retArray;
}
	public double[] hGen(int cells, int end) {
		double retArray[];
		int count = -1;
		retArray = new double[cells * cells];

		for (int i = 0; i < cells*cells; ++i) {
				int xx=gridX[end]-gridX[i];
				int yy=gridY[end]-gridY[i];
				//retArray[++count]=10*(Math.abs(gridX[i]-gridX[end]))+Math.abs(gridY[i]-gridY[end]);       //Heuristic from internet
				retArray[++count]=Math.sqrt((xx*xx)+(yy*yy));                                               //My own Heuristic
			
}
		return retArray;
}}