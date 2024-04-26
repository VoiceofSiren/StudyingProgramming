import java.util.Arrays;
import java.util.Scanner;

public class Java009 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120829
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        int angle = scanner.nextInt();
        System.out.println(solution.solution(angle));
    }

    private static class Solution {
        public int solution(int angle) {
            int answer = 0;
            if (angle <= 90) {
                if (angle%90 > 0) {
                    answer = 1;
                }
                else {
                    answer = 2;
                }
            } else {
                if (angle%90 > 0) {
                    answer = 3;
                }
                else {
                    answer = 4;
                }
            }
            return answer;
        }
    }
}

// 70
// 91
// 180