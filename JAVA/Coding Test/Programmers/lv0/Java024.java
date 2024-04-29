import java.util.Scanner;

public class Java024 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120839
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String rsp = inputString.substring(1, inputString.length() - 1);

        System.out.println(solution.solution(rsp));
    }

    private static class Solution {
        public String solution(String rsp) {
            String answer = "";

            for (int i = 0;  i< rsp.length(); i++) {
                if (rsp.charAt(i) == '2') {
                    answer += "0";
                } else if (rsp.charAt(i) == '0') {
                    answer += "5";
                } else {
                    answer += "2";
                }
            }
            return answer;
        }
    }
}

// "2"
// "205"