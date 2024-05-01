import java.util.Scanner;

public class Java079 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181839?language=java
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
            int answer = 0;
            if (a%2 == 0 && b%2 == 0) {
                answer = Math.abs(a - b);
            } else if (a%2 == 1 && b%2 == 1) {
                answer = (int) Math.pow(a, 2) + (int) Math.pow(b, 2);
            } else {
                answer = 2 * (a + b);
            }
            return answer;
        }
    }
}

/*
3 5
 */

/*
6 1
 */

/*
2 4
 */