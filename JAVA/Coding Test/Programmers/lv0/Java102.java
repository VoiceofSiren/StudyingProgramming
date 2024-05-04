import java.util.Scanner;

public class Java102 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120826
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] strArr = inputString.split(" ");
        String my_string = strArr[0];
        String letter = strArr[1];

        System.out.println(solution.solution(my_string, letter));
    }

    private static class Solution {
        public String solution(String my_string, String letter) {
            return my_string.replace(letter, "");
        }
    }
}

/*
abcdef f
 */

/*
BCBdbe B
 */