import java.util.Scanner;

public class Java041 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181863?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String rny_string = inputString.substring(1, inputString.length() - 1);

        System.out.println(solution.solution(rny_string));
    }

    private static class Solution {
        public String solution(String rny_string) {
            return rny_string.replace("m", "rn");
        }
    }
}

// "masterpiece"
// "programmers"
// "jerry"
// "burn"