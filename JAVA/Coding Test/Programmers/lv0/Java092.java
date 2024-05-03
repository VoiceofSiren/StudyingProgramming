import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Java092 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181867?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String myString = scanner.nextLine();

        System.out.println(solution.returnToString(solution.solution(myString)));
    }

    private static class Solution {
        public Integer[] solution(String myString) {
            List<Integer> answer = new ArrayList<>();
            String[] str_list = myString.split("x");
            for (int i = 0; i < str_list.length; i++) {
                answer.add(str_list[i].length());
            }
            if (myString.charAt(myString.length() - 1) == 'x') {
                answer.add(0);
            }
            return answer.toArray(Integer[]::new);
        }

        public String returnToString(Integer[] numbers) {
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
oxooxoxxox
 */

/*
xabcxdefxghi
 */