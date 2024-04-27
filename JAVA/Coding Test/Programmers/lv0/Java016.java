import java.util.Scanner;

public class Java016 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120813
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        System.out.println(solution.returnToString(solution.solution(n)));
    }

    private static class Solution {
        public int[] solution(int n) {
            int[] numbers = null;
            if (n%2 == 0) {
                numbers = new int[n/2];
            } else {
                numbers = new int[n/2 + 1];
            }
            for (int i = 0; i < numbers.length; i++) {
                numbers[i] = i * 2 + 1;
            }
            return numbers;
        }

        public String returnToString(int[] numbers) {
            String result = "[";
            if (numbers.length == 1) {
                result += numbers[0];
            } else {
                for (int i = 0; i < numbers.length - 1; i++) {
                    result += numbers[i] + ", ";
                }
                result += numbers[numbers.length - 1];
            }
            result += "]";
            return result;
        }
    }
}

// 10
// 5