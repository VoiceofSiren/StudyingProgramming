import java.util.Scanner;

public class Java062 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181908?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String my_string = inputString.substring(1, inputString.length() - 1);

        inputString = scanner.nextLine();
        String is_suffix = inputString.substring(1, inputString.length() - 1);

        System.out.println(solution.solution(my_string, is_suffix));
    }

    private static class Solution {
        public int solution(String my_string, String is_suffix) {
            if (is_suffix.length() > my_string.length()) {
                return 0;
            } else {
                String str = my_string.substring(my_string.length() - is_suffix.length());
                if (str.equals(is_suffix)) {
                    return 1;
                }
                return 0;
            }
        }
    }
}

/*
"banana"
"ana"
 */

/*
"banana"
"nan"
 */

/*
"banana"
"wxyz"
 */

/*
"banana"
"abanana"
 */