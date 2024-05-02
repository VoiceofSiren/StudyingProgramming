import java.util.Scanner;

public class Java083 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181841?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] str_list = inputString.split(" ");
        String my_string = str_list[0];
        String target = str_list[1];

        System.out.println(solution.solution(my_string, target));
    }

    private static class Solution {
        public int solution(String my_string, String target) {
            int answer = 0;
            boolean b = contains(my_string, target);
            return b? 1: 0;
        }

        public boolean contains(String str, String ex) {
            if (ex.length() > str.length()) {
                return false;
            } else {
                for (int i = 0; i < str.length() - ex.length() + 1; i++) {
                    String slice = str.substring(i, i + ex.length());
                    if (slice.equals(ex)) {
                        return true;
                    }
                }
                return false;
            }
        }
    }
}

/*
banana ana
 */

/*
banana wxyz
 */