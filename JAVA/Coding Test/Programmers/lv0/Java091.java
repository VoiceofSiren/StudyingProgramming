import java.util.Arrays;
import java.util.Scanner;

public class Java091 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181835?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] strArr = inputString.substring(1, inputString.length() - 1).split(", ");
        int[] arr = solution.convert(strArr);
        int k = scanner.nextInt();

        System.out.println(solution.returnToString(solution.solution(arr, k)));
    }

    private static class Solution {
        public int[] solution(int[] arr, int k) {
            if (k%2 == 1) {
                arr = Arrays.stream(arr).map(num -> num *= k).toArray();
            } else {
                arr = Arrays.stream(arr).map(num -> num += k).toArray();
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
[1, 2, 3, 100, 99, 98]
3
 */

/*
[1, 2, 3, 100, 99, 98]
2
 */