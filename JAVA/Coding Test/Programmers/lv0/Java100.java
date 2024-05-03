import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Java100 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181861?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] strArr = inputString.substring(1, inputString.length() - 1).split(", ");
        int[] arr = solution.convert(strArr);

        System.out.println(solution.returnToString(solution.solution(arr)));
    }

    private static class Solution {
        public Integer[] solution(int[] arr) {
            List<Integer> answer = new ArrayList<>();
            for (int num: arr) {
                for (int i = 0; i < num; i++) {
                    answer.add(num);
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
[5, 1, 4]
 */

/*
[6, 6]
 */

/*
[1]
 */