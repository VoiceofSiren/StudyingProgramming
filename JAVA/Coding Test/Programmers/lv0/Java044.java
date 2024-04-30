import java.util.Scanner;

public class Java044 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181873?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String my_string = inputString.substring(1, inputString.length() - 1);

        String alp = scanner.nextLine();

        System.out.println(solution.solution(my_string, alp));
    }

    private static class Solution {
        public String solution(String my_string, String alp) {
            return my_string.replace(alp, alp.toUpperCase());
        }
    }
}

/*
"programmers"
p
 */

/*
"lowercase"
x
 */