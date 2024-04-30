import java.util.ArrayList;
import java.util.Scanner;

public class Java054 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181886?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] names = inputString.substring(2, inputString.length() - 2).split("\", \"");

        System.out.println(solution.returnToString(solution.solution(names)));
    }

    private static class Solution {
        public String[] solution(String[] names) {
            ArrayList<String> answer = new ArrayList<>();

            for (int i = 0; i < names.length; i++) {
                if (i%5 == 0) {
                    answer.add(names[i]);
                }
            }
            return answer.toArray(String[]::new);
        }

        public String returnToString(String[] numbers) {
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
["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]
 */
