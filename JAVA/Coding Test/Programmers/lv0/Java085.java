import java.util.Scanner;

public class Java085 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181842?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] str_list = inputString.split(" ");
        String str1 = str_list[0];
        String str2 = str_list[1];

        System.out.println(solution.solution(str1, str2));
    }

    private static class Solution {
        public int solution(String str1, String str2) {
            return contains(str1, str2)? 1: 0;
        }

        public boolean contains(String str1, String str2) {
            for (int i = 0; i < str2.length() - str1.length() + 1; i++) {
                String slice = str2.substring(i, i + str1.length());
                if (slice.equals(str1)) {
                    return true;
                }
            }
            return false;
        }
    }
}

/*
abc aabcc
 */

/*
tbt tbbttb
 */