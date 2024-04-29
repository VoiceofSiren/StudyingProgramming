import java.util.Scanner;

public class Java025 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120845
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] input_arr = inputString.substring(1, inputString.length() - 1).split(", ");

        int[] boxes = solution.convert(input_arr);
        int n = scanner.nextInt();

        System.out.println(solution.solution(boxes, n));
    }

    private static class Solution {
        public int solution(int[] boxes, int n) {
            int answer = 1;
            for (int i = 0; i < boxes.length; i++) {
                answer *= boxes[i]/n;
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
[1, 1, 1]
1
 */

/*
[10, 8, 6]
3
 */