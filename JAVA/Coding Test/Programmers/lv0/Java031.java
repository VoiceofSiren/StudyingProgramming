import java.util.Scanner;

public class Java031 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120898
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String message = inputString.substring(1, inputString.length() - 1);

        System.out.println(solution.solution(message));
    }

    private static class Solution {
        public int solution(String message) {
            return message.length() * 2;
        }
    }
}

// "happy birthday!"
// "I love you~"