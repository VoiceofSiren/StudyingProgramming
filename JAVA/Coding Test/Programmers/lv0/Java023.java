import java.util.Scanner;

public class Java023 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120837
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        int hp = scanner.nextInt();

        System.out.println(solution.solution(hp));
    }

    private static class Solution {
        public int solution(int hp) {
            int[] ants = {5, 3, 1};
            int answer = 0;
            for (int i = 0; i < ants.length; i++) {
                answer += hp / ants[i];
                hp %= ants[i];
            }
            return answer;
        }
    }
}

// 23
// 24
// 999