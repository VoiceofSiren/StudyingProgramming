import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Java066 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181920?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        int start_num = scanner.nextInt();
        int end_num = scanner.nextInt();

        System.out.println(solution.returnToString(solution.solution(start_num, end_num)));
    }

    private static class Solution {
        public Integer[] solution(int start_num, int end_num) {
            List<Integer> answer = new ArrayList<>();
            for (int i = start_num; i <= end_num; i++) {
                answer.add(i);
            }
            return answer.toArray(Integer[]::new);
        }

        public String returnToString(Integer[] numbers) {
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
3
10
 */