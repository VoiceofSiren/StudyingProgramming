import java.util.Scanner;

public class Java021 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120821
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
        public int[] solution(int[] num_list) {
            for (int i = 0; i < num_list.length/2; i++) {
                int temp = num_list[i];
                num_list[i] = num_list[num_list.length - i - 1];
                num_list[num_list.length - i - 1] = temp;
            }
            return num_list;
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

// [1, 2, 3, 4, 5]
// [1, 1, 1, 1, 1, 2]
// [1, 0, 1, 1, 1, 3, 5]