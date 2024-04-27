import java.util.Scanner;

public class Java012 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120809
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

        int n = scanner.nextInt();
        System.out.println(solution.solution(numbers, n));
    }

    private static class Solution {
        public int solution(int[] array, int n) {
            int answer = 0;
            for (int i = 0; i < array.length; i++) {
                if (array[i] == n) {
                    answer += 1;
                }
            }
            return answer;
        }
    }
}

// [1, 1, 2, 3, 4, 5]
// [0, 2, 3, 4]