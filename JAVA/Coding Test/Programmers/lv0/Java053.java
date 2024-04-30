import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Java053 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181885?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] todo_list = inputString.substring(2, inputString.length() - 2).split("\", \"");

        inputString = scanner.nextLine();
        boolean[] finished = solution.convert(inputString.substring(1, inputString.length() - 1).split(", "));

        System.out.println(solution.returnToString(solution.solution(todo_list, finished)));
    }

    private static class Solution {
        public String[] solution(String[] todo_list, boolean[] finished) {
            List<String> answer = new ArrayList<>();
            for (int i = 0; i < todo_list.length; i++) {
                if (!finished[i]) {
                    answer.add(todo_list[i]);
                }
            }
            return answer.stream().map(String::new).toArray(String[]::new);
        }

        public boolean[] convert(String[] input_arr) {
            boolean[] num_list = new boolean[input_arr.length];
            for (int i  = 0; i < input_arr.length; i++) {
                num_list[i] = Boolean.parseBoolean(input_arr[i]);
            }
            return num_list;
        }

        public String returnToString(String[] numbers) {
            String result = "[";
            if (numbers.length == 1) {
                result += numbers[0];
            } else {
                for (int i = 0; i < numbers.length - 1; i++) {
                    result += numbers[i] + ", ";
                }
                result += numbers[numbers.length - 1];
            }
            result += "]";
            return result;
        }
    }
}

/*
["problemsolving", "practiceguitar", "swim", "studygraph"]
[true, false, true, false]
 */
