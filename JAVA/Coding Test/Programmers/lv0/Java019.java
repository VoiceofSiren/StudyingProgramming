import java.util.Scanner;

public class Java019 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120818
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        int price = scanner.nextInt();

        System.out.println(solution.solution(price));
    }

    private static class Solution {
        public int solution(int price) {
            if (price >= 500000) {
                price *= 0.8;
            } else if (price >= 300000) {
                price *= 0.9;
            } else if (price >= 100000) {
                price *= 0.95;
            }
            return price;
        }
    }
}

// 150000
// 580000