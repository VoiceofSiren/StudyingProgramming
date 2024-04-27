import java.util.Scanner;

public class Java013 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120583
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] inputArr = inputString.substring(1, inputString.length() - 1).split(", ");

        int[] numbers = new int[inputArr.length];

        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = Integer.parseInt(inputArr[i]);
        }
        System.out.println(solution.returnToString(solution.solution(numbers)));
    }

    private static class Solution {
        public int[] solution(int[] numbers) {
            int[] answer = new int[numbers.length];
            for (int i = 0; i < numbers.length; i++) {
                answer[i] = numbers[i] * 2;
            }
            return answer;
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
// [1, 2, 100, -99, 1, 2, 3]