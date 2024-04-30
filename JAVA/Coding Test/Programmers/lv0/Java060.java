import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Java060 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181896?language=java
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
            int answer = -1;
            for (int i = 0; i < num_list.length; i++) {
                if (num_list[i] < 0) {
                    answer = i;
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
[12, 4, 15, 46, 38, -2, 15]
 */

/*
[13, 22, 53, 24, 15, 6]
 */