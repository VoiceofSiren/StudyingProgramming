import java.util.Scanner;

public class Java080 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181841?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] str_list = inputString.substring(2, inputString.length() - 2).split("\", \"");
        String ex = scanner.nextLine();

        System.out.println(solution.solution(str_list, ex));
    }

    private static class Solution {
        public String solution(String[] str_list, String ex) {
            String answer = "";
            for (String str: str_list) {
                if (!contains(str, ex)) {
                    answer += str;
                }
            }
            return answer;
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
["abc", "def", "ghi"]
ef
 */

/*
["abc", "bbc", "cbc"]
c
 */