import java.util.Arrays;
import java.util.Scanner;

public class Java055 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181887?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] input_arr = inputString.substring(1, inputString.length() - 1).split(", ");
        int[] num_list = solution.convert(input_arr);

        System.out.println(solution.solution(num_list));
    }

    private static class Solution {
        public int solution(int[] num_list) {
            int[] answers = {0, 0};
            for (int i = 0; i < num_list.length; i++) {
                if (i%2 == 0) {
                    answers[0] += num_list[i];
                } else {
                    answers[1] += num_list[i];
                }
            }
            return Arrays.stream(answers).max().getAsInt();
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

// [4, 2, 6, 1, 7, 6]
// [-1, 2, 5, 6, 3]