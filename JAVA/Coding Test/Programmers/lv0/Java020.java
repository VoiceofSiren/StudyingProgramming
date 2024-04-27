import java.util.Scanner;

public class Java020 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120819
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        int money = scanner.nextInt();

        System.out.println(solution.returnToString(solution.solution(money)));
    }

    private static class Solution {
        public int[] solution(int money) {
            int[] answer = new int[2];
            answer[0] = money / 5500;
            answer[1] = money % 5500;
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

// 5500
// 15000