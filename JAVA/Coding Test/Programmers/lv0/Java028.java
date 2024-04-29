import java.util.Arrays;
import java.util.Scanner;

public class Java028 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120889
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] input_arr = inputString.substring(1, inputString.length() - 1).split(", ");

        int[] sides = solution.convert(input_arr);

        System.out.println(solution.solution(sides));
    }

    private static class Solution {
        public int solution(int[] sides) {
            int max_value = Arrays.stream(sides).max().getAsInt();
            for (int i = 0; i < sides.length; i++) {
                if (sides[i] == max_value) {
                    sides[i] = 0;
                    break;
                }
            }
            int sum_value = Arrays.stream(sides).sum();
            return max_value < sum_value? 1: 2;
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

// [1, 2, 3]
// [3, 6, 2]
// [199, 72, 222]