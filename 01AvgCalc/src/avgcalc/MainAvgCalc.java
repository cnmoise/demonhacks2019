package avgcalc;

import java.math.BigDecimal;
import java.util.Scanner;

//Author: Claudiu Moise
//GPA calculator for Java and Python


public class MainAvgCalc {

	public static void main(String[] args) {
		//Sample Test case 1
	   String Sname = "Bob Saget";
		double ColGPA = 1.389454;
		double HighGPA = 3.7;
		boolean weighted = false;
		String kbw = "x";
		float RoundedGPA = 0.0f;
		
		//user can enter in their own values
		Scanner kb = new Scanner(System.in);
		
		System.out.println("Please enter the students name:");
		Sname = kb.nextLine();		
		System.out.println("Please enter the students College GPA:");
		ColGPA = kb.nextDouble();		
		System.out.println("Please enter the students High School GPA:");
		HighGPA = kb.nextDouble();
		kbw = kb.nextLine();
		
		System.out.println("Is the High School GPA weighted? y/n:");
		kbw = kb.next();
		
		//we need the .equals method to handle strings
		if(kbw.equals("y")) {
			weighted = true;
		}
		else if(kbw.equals("n")) {
			weighted = false;
		}
		else {
			System.out.println("Invalid entry... Assuming GPA is unweighted");
		}
			
		System.out.println("Returning Output...");
		//in python theres no confusion with float and double
		if(weighted) {
			RoundedGPA= round((((float)Math.min(4, HighGPA) + (float)((2*ColGPA))))/3,2);
		}
		else
		{
			float temp = (float)(HighGPA + ColGPA)/2;
			RoundedGPA = round(temp, 2);	
		}
		
		
		System.out.println("Student Name: " + Sname);
		System.out.println("College GPA: " + ColGPA);
		if(weighted) {
         System.out.println("High School GPA (Weighted): " + HighGPA);
      }
      else{
         System.out.println("High School GPA (Unweighted): " + HighGPA);
      }
				
		System.out.println("Rounded GPA: " + RoundedGPA);

		
	}
	
	/* No Pretty way to do rounding to 2 decimal points in java see
	 * https://stackoverflow.com/questions/8911356/whats-the-best-practice-to-round-a-float-to-2-decimals
	 * 
	 * For my source code
	 * */
	
	public static float round(float d, int decimalPlace) {
        BigDecimal bd = new BigDecimal(Float.toString(d));
        //serves to round to the nearest decimal neighbor
        bd = bd.setScale(decimalPlace, BigDecimal.ROUND_HALF_UP);
        return bd.floatValue();
    }
}
