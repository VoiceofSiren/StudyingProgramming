import java.util.Arrays;
import java.util.Scanner;

public class Java050 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181879?language=java
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
            int answer = 1;
            if (num_list.length < 11) {
                for (int num: num_list) {
                    answer *= num;
                }
            } else {
                answer = 0;
                for (int num: num_list) {
                    answer += num;
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

// [3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]
// [2, 3, 4, 5]