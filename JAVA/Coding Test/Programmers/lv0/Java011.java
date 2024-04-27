import java.util.Scanner;

public class Java011 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120806
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] inputArr = inputString.split(" ");

        int num1 = Integer.parseInt(inputArr[0]);
        int num2 = Integer.parseInt(inputArr[1]);

        System.out.println(solution.solution(num1, num2));
    }

    private static class Solution {
        public int solution(int num1, int num2) {
            int answer = 0;
            answer = 1000 * num1 / num2;
            return answer;
        }
    }
}

// 3 2
// 7 3
// 1 16