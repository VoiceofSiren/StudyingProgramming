import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Java103 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120854
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] strlist = inputString.substring(2, inputString.length() - 2).split("\", \"");

        System.out.println(solution.returnToString(solution.solution(strlist)));
    }

    private static class Solution {
        public int[] solution(String[] strlist) {
            int[] answer = new int[strlist.length];
            for (int i = 0; i < strlist.length; i++) {
                answer[i] = strlist[i].length();
            }
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

/*
["We", "are", "the", "world!"]
 */

/*
["I", "Love", "Programmers."]
 */