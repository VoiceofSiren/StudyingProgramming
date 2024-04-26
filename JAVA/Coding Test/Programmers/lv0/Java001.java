import java.util.Arrays;
import java.util.Scanner;

public class Java001 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120802?language=java
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
            return num1 + num2;
        }
    }
}

// 2 3