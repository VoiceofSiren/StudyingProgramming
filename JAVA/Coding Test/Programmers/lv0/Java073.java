import java.util.Scanner;

public class Java073 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181936?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] input_arr = inputString.split(" ");
        int number = Integer.parseInt(input_arr[0]);
        int n = Integer.parseInt(input_arr[1]);
        int m = Integer.parseInt(input_arr[2]);

        System.out.println(solution.solution(number, n, m));
    }

    private static class Solution {
        public int solution(int number, int n, int m) {
            return (number%n == 0 && number%m == 0)? 1: 0;
        }
    }
}

/*
60 2 3
 */

/*
55 10 5
 */