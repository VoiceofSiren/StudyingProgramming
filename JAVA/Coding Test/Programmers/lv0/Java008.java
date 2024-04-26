import java.util.Arrays;
import java.util.Scanner;

public class Java008 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120817
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
        System.out.println(solution.solution(numbers));
    }

    private static class Solution {
        public double solution(int[] numbers) {
            double answer = 0;
            for (int number: numbers) {
                answer += (double) number;
            }
            answer /= numbers.length;
            return answer;
        }
    }
}

// [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
// [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]