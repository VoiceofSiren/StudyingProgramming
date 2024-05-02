import java.util.Arrays;
import java.util.Scanner;

public class Java082 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181841?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] str_list = inputString.substring(1, inputString.length() - 1).split(", ");
        int[] num_list = solution.convert(str_list);
        int n = scanner.nextInt();

        System.out.println(solution.solution(num_list, n));
    }

    private static class Solution {
        public int solution(int[] num_list, int n) {
            boolean b = Arrays.stream(num_list).anyMatch(num -> num == n);
            return b? 1: 0;
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
3
 */

/*
[15, 98, 23, 2, 15]
20
 */