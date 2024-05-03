import java.util.Arrays;
import java.util.Scanner;

public class Java096 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181854?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] strArr = inputString.substring(1, inputString.length() - 1).split(", ");
        int[] arr = solution.convert(strArr);
        int n = scanner.nextInt();

        System.out.println(solution.returnToString(solution.solution(arr, n)));
    }

    private static class Solution {
        public int[] solution(int[] arr, int n) {
            if (arr.length%2 == 1) {
                for (int i = 0; i < arr.length; i += 2) {
                    arr[i] += n;
                }
            } else {
                for (int i = 1; i < arr.length; i += 2) {
                    arr[i] += n;
                }
            }
            return arr;
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
[49, 12, 100, 276, 33]
27
 */

/*
[444, 555, 666, 777]
100
 */