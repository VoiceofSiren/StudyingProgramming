import java.util.Scanner;

public class Java098 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181834?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String myString = scanner.nextLine();

        System.out.println(solution.solution(myString));
    }

    private static class Solution {
        public String solution(String myString) {
            String answer = "";
            for (int i = 0; i < myString.length(); i++) {
                char target = myString.charAt(i);
                if ('a' <= target && target <= 'k') {
                    answer += "l";
                } else {
                    answer += "" + myString.charAt(i);
                }
            }
            return answer;
        }
    }
}

/*
abcdevwxyz
 */

/*
jjnnllkkmm
 */