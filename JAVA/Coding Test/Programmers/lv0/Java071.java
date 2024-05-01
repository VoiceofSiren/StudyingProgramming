import java.util.Arrays;
import java.util.Scanner;

public class Java071 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181933?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] input_arr = inputString.split(" ");
        int a = Integer.parseInt(input_arr[0]);
        int b = Integer.parseInt(input_arr[1]);
        boolean flag = Boolean.parseBoolean(input_arr[2]);

        System.out.println(solution.solution(a, b, flag));
    }

    private static class Solution {
        public int solution(int a, int b, boolean flag) {
            return flag? a+b: a-b;
        }
    }
}

/*
-4 7 true
 */

/*
-4 7 false
 */