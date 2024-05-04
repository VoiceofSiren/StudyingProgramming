import java.util.Arrays;
import java.util.Scanner;

public class Java104 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120833
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] strArr = inputString.substring(1, inputString.length() - 1).split(", ");
        int[] numbers = solution.convert(strArr);
        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();

        System.out.println(solution.returnToString(solution.solution(numbers, num1, num2)));
    }

    private static class Solution {
        public int[] solution(int[] numbers, int num1, int num2) {
            int len = num2 - num1 + 1;
            int[] answer = new int[len];
            for (int i = 0; i < len; i++) {
                answer[i] = numbers[num1 + i];
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

        public String returnToString(int[] numbers) {
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
[1, 2, 3, 4, 5]
1
3
 */

/*
[1, 3, 5]
1
2
 */