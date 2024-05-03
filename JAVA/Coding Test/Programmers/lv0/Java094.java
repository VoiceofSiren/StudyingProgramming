import java.util.Arrays;
import java.util.Scanner;

public class Java094 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120847
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] strArr = inputString.substring(1, inputString.length() - 1).split(", ");
        int[] numbers = solution.convert(strArr);

        System.out.println(solution.solution(numbers));
    }

    private static class Solution {
        public int solution(int[] numbers) {
            numbers = Arrays.stream(numbers).sorted().toArray();
            int len = numbers.length;
            return numbers[len - 2] * numbers[len - 1];
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
[1, 2, 3, 4, 5]
 */

/*
[0, 31, 24, 10, 1, 9]
 */