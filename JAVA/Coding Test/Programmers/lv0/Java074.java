import java.util.Scanner;

public class Java074 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181937?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] input_arr = inputString.split(" ");
        int num = Integer.parseInt(input_arr[0]);
        int n = Integer.parseInt(input_arr[1]);

        System.out.println(solution.solution(num, n));
    }

    private static class Solution {
        public int solution(int num, int n) {
            return (num%n == 0)? 1: 0;
        }
    }
}

/*
60 2 3
 */

/*
55 10 5
 */