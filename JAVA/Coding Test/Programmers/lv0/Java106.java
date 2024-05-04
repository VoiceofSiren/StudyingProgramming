import java.util.Scanner;

public class Java106 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120830
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] strArr = inputString.split(" ");
        int n = Integer.parseInt(strArr[0]);
        int k = Integer.parseInt(strArr[1]);

        System.out.println(solution.solution(n, k));
    }

    private static class Solution {
        public int solution(int n, int k) {
            k -= n/10;
            return n * 12000 + k * 2000;
        }
    }
}

/*
10 3
 */

/*
64 6
 */