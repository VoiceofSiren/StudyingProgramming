import java.util.Scanner;

public class Java018 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120816
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String[] inputList = scanner.nextLine().split(" ");

        int slice = Integer.parseInt(inputList[0]);
        int n = Integer.parseInt(inputList[1]);

        System.out.println(solution.solution(slice, n));
    }

    private static class Solution {
        public int solution(int slice, int n) {
            return (n - 1)/slice + 1;
        }
    }
}

// 7 10
// 4 12