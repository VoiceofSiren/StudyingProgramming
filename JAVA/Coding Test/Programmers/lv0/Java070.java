import java.util.Arrays;
import java.util.Scanner;

public class Java070 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181929?language=java
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

            int[] answer = {1, 0};

            Arrays.stream(num_list).forEach(num -> {
                answer[0] *= num;
                answer[1] += num;
            });

            return answer[0] < (int) Math.pow(answer[1], 2)? 1: 0;
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
[3, 4, 5, 2, 1]
 */

/*
[5, 7, 8, 3]
 */