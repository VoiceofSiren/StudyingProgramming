import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Java061 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181907?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String my_string = inputString.substring(1, inputString.length() - 1);
        int n = scanner.nextInt();

        System.out.println(solution.solution(my_string, n));
    }

    private static class Solution {
        public String solution(String my_string, int n) {
            return my_string.substring(0, n);
        }
    }
}

/*
"ProgrammerS123"
11
 */

/*
"He110W0r1d"
5
 */