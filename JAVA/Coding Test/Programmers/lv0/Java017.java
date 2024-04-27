import java.util.Scanner;

public class Java017 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120814
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        System.out.println(solution.solution(n));
    }

    private static class Solution {
        public int solution(int n) {
            return (n - 1)/7 + 1;
        }
    }
}

// 7
// 1
// 15