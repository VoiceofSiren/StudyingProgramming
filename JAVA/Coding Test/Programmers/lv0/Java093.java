import java.util.Arrays;
import java.util.Scanner;

public class Java093 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181852?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] strArr = inputString.substring(1, inputString.length() - 1).split(", ");
        int[] num_list = solution.convert(strArr);

        System.out.println(solution.returnToString(solution.solution(num_list)));
    }

    private static class Solution {
        public int[] solution(int[] num_list) {
            int[] answer = new int[num_list.length - 5];
            num_list = Arrays.stream(num_list).sorted().toArray();
            for (int i = 5; i < num_list.length; i++) {
                answer[i - 5] = num_list[i];
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
[12, 4, 15, 46, 38, 1, 14, 56, 32, 10]
 */