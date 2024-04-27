import java.util.Scanner;

public class Java014 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120585
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

        int height = scanner.nextInt();

        System.out.println(solution.solution(numbers, height));
    }

    private static class Solution {
        public int solution(int[] array, int height) {
            int answer = 0;
            for (int i = 0; i < array.length; i++) {
                if (array[i] > height) {
                    answer += 1;
                }
            }
            return answer;
        }
    }
}

/*
[149, 180, 192, 170]
167
 */
/*
[180, 120, 140]
190
 */