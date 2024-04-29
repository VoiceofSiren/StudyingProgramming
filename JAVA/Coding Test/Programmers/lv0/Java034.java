import java.util.Arrays;
import java.util.Scanner;

public class Java034 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120905
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        int n = Integer.parseInt(scanner.nextLine());

        String inputString = scanner.nextLine();
        String[] input_arr = inputString.substring(1, inputString.length() - 1).split(", ");
        int[] numlist = solution.convert(input_arr);

        System.out.println(solution.returnToString(solution.solution(n, numlist)));
    }

    private static class Solution {
        public int[] solution(int n, int[] numlist) {
            return Arrays.stream(numlist).filter(num -> num % n == 0).toArray();
        }

        public int[] convert(String[] input_arr) {
            int[] num_list = new int[input_arr.length];
            for (int i  = 0; i < input_arr.length; i++) {
                num_list[i] = Integer.parseInt(input_arr[i]);
            }
            return num_list;
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

/*
3
[4, 5, 6, 7, 8, 9, 10, 11, 12]
 */

/*
5
[1, 9, 3, 10, 13, 5]
 */

/*
12
[2, 100, 120, 600, 12, 12]
 */