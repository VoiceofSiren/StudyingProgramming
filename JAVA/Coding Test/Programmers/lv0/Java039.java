import java.util.Scanner;

public class Java039 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181850?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        double flo = scanner.nextDouble();

        System.out.println(solution.solution(flo));
    }

    private static class Solution {
        public int solution(double flo) {
            return (int) Math.floor(flo);
        }
    }
}

// 1.42
// 69.32