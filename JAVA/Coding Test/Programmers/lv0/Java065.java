import java.util.Scanner;

public class Java065 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181915?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String my_string = inputString.substring(1, inputString.length() - 1);

        inputString = scanner.nextLine();
        String[] input_arr = inputString.substring(1, inputString.length() - 1).split(", ");
        int[] index_list = solution.convert(input_arr);

        System.out.println(solution.solution(my_string, index_list));
    }

    private static class Solution {
        public String solution(String my_string, int[] index_list) {
            String answer = "";
            for (int index: index_list) {
                answer += my_string.charAt(index);
            }
            return answer;
        }

        public int[] convert(String[] input_arr) {
            int[] num_list = new int[input_arr.length];
            for (int i  = 0; i < input_arr.length; i++) {
                num_list[i] = Integer.parseInt(input_arr[i]);
            }
            return num_list;
        }
    }
}

/*
"cvsgiorszzzmrpaqpe"
[16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]
 */

/*
"zpiaz"
[1, 2, 0, 0, 3]
 */