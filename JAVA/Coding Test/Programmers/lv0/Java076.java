import java.util.Scanner;

public class Java076 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181938?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] input_arr = inputString.split(" ");
        int a = Integer.parseInt(input_arr[0]);
        int b = Integer.parseInt(input_arr[1]);

        System.out.println(solution.solution(a, b));
    }

    private static class Solution {
        public int solution(int a, int b) {
            int num1 = Integer.parseInt(a + "" + b);
            int num2 = Integer.parseInt(b + "" + a);
            return Math.max(num1, num2);
        }
    }
}

/*
9 91
 */

/*
89 8
 */