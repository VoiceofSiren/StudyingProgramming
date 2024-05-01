import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Java068 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181927?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] input_arr = inputString.substring(1, inputString.length() - 1).split(", ");
        int[] num_list = solution.convert(input_arr);

        System.out.println(solution.returnToString(solution.solution(num_list)));
    }

    private static class Solution {
        public Integer[] solution(int[] num_list) {
            List<Integer> answer = new ArrayList<>();
            int num1 = num_list[num_list.length - 2];
            int num2 = num_list[num_list.length - 1];
            int new_num = (num1 < num2)?  (num2 - num1): num2*2;
            for (int num: num_list) {
                answer.add(num);
            }
            answer.add(new_num);
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
[2, 1, 6]
 */

/*
[5, 2, 1, 7, 5]
 */