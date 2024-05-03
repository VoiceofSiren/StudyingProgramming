import java.util.Scanner;

public class Java097 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181864?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] strArr = inputString.split(" ");
        String myString = strArr[0];
        String pat = strArr[1];

        System.out.println(solution.solution(myString, pat));
    }

    private static class Solution {
        public int solution(String myString, String pat) {
            String newString = "";
            for (int i = 0; i < myString.length(); i++) {
                String alph = "" + myString.charAt(i);
                if (alph.equals("A")) {
                    newString += "B";
                } else {
                    newString += "A";
                }
            }
            return contains(newString, pat)? 1: 0;
        }

        public boolean contains(String newString, String pat) {
            if (pat.length() > newString.length()) {
                return false;
            } else {
                for (int i = 0; i < newString.length() - pat.length() + 1; i++) {
                    String slice = newString.substring(i, i + pat.length());
                    if (slice.equals(pat)) {
                        return true;
                    }
                }
                return false;
            }
        }
    }
}

/*
ABBAA AABB
 */

/*
ABAB ABAB
 */