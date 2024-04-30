import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Java056 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181888?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] input_arr = inputString.substring(1, inputString.length() - 1).split(", ");
        int[] num_list = solution.convert(input_arr);
        int n = scanner.nextInt();

        System.out.println(solution.returnToString(solution.solution(num_list, n)));
    }

    private static class Solution {
        public Integer[] solution(int[] num_list, int n) {
            List<Integer> answer = new ArrayList<>();
            for (int i = 0; i < num_list.length; i++) {
                if (i%n == 0) {
                    answer.add(num_list[i]);
                }
            }
            return answer.toArray(Integer[]::new);
        }

        public int[] convert(String[] input_arr) {
            int[] num_list = new int[input_arr.length];
            for (int i  = 0; i < input_arr.length; i++) {
                num_list[i] = Integer.parseInt(input_arr[i]);
            }
            return num_list;
        }

        public String returnToString(Integer[] numbers) {
            String result = "[";
            if (numbers.length == 1) {
                result += numbers[0];
            } else {
                for (int i = 0; i < numbers.length - 1; i++) {
                    result += numbers[i] + ", ";
                }
                result += numbers[numbers.length - 1];
            }
            result += "]";
            return result;
        }
    }
}

/*
[4, 2, 6, 1, 7, 6]
2
 */

/*
[4, 2, 6, 1, 7, 6]
4
 */