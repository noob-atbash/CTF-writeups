import java.util.Scanner;
public class EnglishLanguage
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //String inp = sc.nextLine();
        String inp="1dd3|y_3tttb5g`q]^dhn3j";
        if (inp.length()!=23) {
            System.out.println("Your input is incorrect.");
            System.exit(0);
        }
        for (int i = 0; i<3; i++) {
            inp=xor(inp);
            inp=transpose(inp);
        }
        System.out.println(inp);
    }
    public static String transpose(String input) {
        int[] transpose = {11,18,15,19,8,17,5,2,12,6,21,0,22,7,13,14,4,16,20,1,3,10,9};
        char str[]=new char[23];
        for (int i=0;i<23;i++)
        {
            str[transpose[i]]=input.charAt(i);
        }
        return String.valueOf(str);
    }
    public static String xor(String input) {
        int[] xor = {4,1,3,1,2,1,3,0,1,4,3,1,2,0,1,4,1,2,3,2,1,0,3};
        String ret = "";
        for (int i = 0; i<input.length(); i++) {
            ret+=(char)(input.charAt(i)^xor[i]) ;
        }
        return ret;
    }
}
