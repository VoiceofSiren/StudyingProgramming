import java.util.Arrays;
import java.util.Scanner;

public class Java090 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181870?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] strArr = inputString.substring(1, inputString.length() - 1).split(", ");
        int[] dot = solution.convert(strArr);

        System.out.println(solution.solution(dot));
    }

    private static class Solution {
        public int solution(int[] dot) {
            int x = dot[0];
            int y = dot[1];
            if (x > 0 && y > 0) {
                return 1;
            } else if (x < 0 && y > 0) {
                return 2;
            } else if (x < 0 && y < 0) {
                return 3;
            } else {
                return 4;
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
[2, 4]
 */

/*
[-7, 9]
 */