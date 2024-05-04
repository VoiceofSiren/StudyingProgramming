import java.util.Scanner;
import java.util.Stack;

public class Java110 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120834
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        int age = scanner.nextInt();

        System.out.println(solution.solution(age));
    }

    private static class Solution {
        public String solution(int age) {
            String answer = "";
            Stack<Integer> stack = new Stack<>();
            while (age > 0) {
                int num = age%10;
                stack.push(num);
                age /= 10;
            }
            while (stack.size() > 0) {
                answer += "" + (char) (stack.pop() + 97);
            }
            return answer;
        }
    }
}

/*
23
 */

/*
51
 */

/*
100
 */