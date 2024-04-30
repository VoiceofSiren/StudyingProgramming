import java.util.Arrays;
import java.util.Scanner;

public class Java052 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181884?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] input_arr = inputString.substring(1, inputString.length() - 1).split(", ");
        int[] numbers = solution.convert(input_arr);
        int n = scanner.nextInt();

        System.out.println(solution.solution(numbers, n));
    }

    private static class Solution {
        public int solution(int[] numbers, int n) {
            int answer = 0;
            for (int number: numbers) {
                answer += number;
                if (answer > n) {
                    break;
                }
            }
            return answer;
        }

        public int[] convert(String[] input_arr) {
            int[] num_list = new int[input_arr.length];
            for (int i  = 0; i < input_arr.length; i++) {
                num_list[i] = Integer.parseInt(input_arr[i]);
            }
            return num_list;
        }
    }
}

/*
[34, 5, 71, 29, 100, 34]
123
 */

/*
[58, 44, 27, 10, 100]
139
 */