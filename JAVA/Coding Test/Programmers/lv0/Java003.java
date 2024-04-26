import java.util.Arrays;
import java.util.Scanner;

public class Java003 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120804
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);
        String[] inputList = Arrays.stream(scanner.nextLine().split(" "))
                .map(String::trim)
                .toArray(String[]::new);
        int num1 = Integer.parseInt(inputList[0]);
        int num2 = Integer.parseInt(inputList[1]);
        System.out.println(solution.solution(num1, num2));
    }

    private static class Solution {
        public int solution(int num1, int num2) {
            return num1 * num2;
        }
    }
}

// 3 4
// 27 19