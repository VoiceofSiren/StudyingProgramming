import java.util.Scanner;

public class Java038 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120910
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String[] inputArr = scanner.nextLine().split(" ");
        int n = Integer.parseInt(inputArr[0]);
        int t = Integer.parseInt(inputArr[1]);

        System.out.println(solution.solution(n, t));
    }

    private static class Solution {
        public int solution(int n, int t) {
            return n * (int) Math.pow(2, t);
        }
    }
}


// 2 10
// 7 15