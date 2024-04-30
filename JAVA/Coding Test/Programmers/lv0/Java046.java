import java.util.Scanner;

public class Java046 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181875?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] strArr = inputString.substring(2, inputString.length() - 2).split("\",\"");

        System.out.println(solution.returnToString(solution.solution(strArr)));
    }

    private static class Solution {
        public String[] solution(String[] strArr) {
            for (int i = 0; i < strArr.length; i++) {
                if (i%2 == 0) {
                    strArr[i] = strArr[i].toLowerCase();
                } else {
                    strArr[i] = strArr[i].toUpperCase();
                }
            }
            return strArr;
        }

        public String returnToString(String[] numbers) {
            String result = "[";
            if (numbers.length == 1) {
                result += numbers[0];
            } else {
                for (int i = 0; i < numbers.length - 1; i++) {
                    result += numbers[i] + ",";
                }
                result += numbers[numbers.length - 1];
            }
            result += "]";
            return result;
        }
    }
}

// ["AAA","BBB","CCC","DDD"]
// ["aBc","AbC"]