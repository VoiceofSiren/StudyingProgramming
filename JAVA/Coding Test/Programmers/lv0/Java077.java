import java.util.Scanner;

public class Java077 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181940?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] input_arr = inputString.split(" ");
        String my_string = input_arr[0];
        my_string = my_string.substring(1, my_string.length() - 1);
        int k = Integer.parseInt(input_arr[1]);

        System.out.println(solution.solution(my_string, k));
    }

    private static class Solution {
        public String solution(String my_string, int k) {
            String answer = "";
            for (int i = 0; i < k; i++) {
                answer += my_string;
            }
            return answer;
        }
    }
}

/*
"string" 3
 */

/*
"love" 10
 */