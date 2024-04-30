import java.util.Scanner;

public class Java045 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181874?language=java
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
            return myString.toLowerCase().replace("a", "A");
        }
    }
}

// "abstract algebra"
// "PrOgRaMmErS"