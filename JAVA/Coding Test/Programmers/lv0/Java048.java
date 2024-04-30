import java.util.Scanner;

public class Java048 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181877?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String myString = inputString.substring(1, inputString.length() - 1);

        System.out.println(solution.solution(myString));
    }

    private static class Solution {
        public String solution(String myString) {
            return myString.toUpperCase();
        }
    }
}

// "aBcDeFg"
// "AAA"