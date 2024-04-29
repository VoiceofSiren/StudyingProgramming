import java.util.Arrays;
import java.util.Scanner;

public class Java040 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181856?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] input_arr = inputString.substring(1, inputString.length() - 1).split(", ");
        int[] arr1 = solution.convert(input_arr);

        inputString = scanner.nextLine();
        input_arr = inputString.substring(1, inputString.length() - 1).split(", ");
        int[] arr2 = solution.convert(input_arr);

        System.out.println(solution.solution(arr1, arr2));
    }

    private static class Solution {
        public int solution(int[] arr1, int[] arr2) {
            if (arr1.length > arr2.length) {
                return 1;
            } else if (arr1.length < arr2.length) {
                return -1;
            } else {
                int sum1 = Arrays.stream(arr1).sum();
                int sum2 = Arrays.stream(arr2).sum();
                if (sum1 > sum2) {
                    return 1;
                } else if (sum1 < sum2) {
                    return -1;
                } else {
                    return 0;
                }
            }
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
[49, 13]
[70, 11, 2]
 */

/*
[100, 17, 84, 1]
[55, 12, 65, 36]
 */

/*
[1, 2, 3, 4, 5]
[3, 3, 3, 3, 3]
 */