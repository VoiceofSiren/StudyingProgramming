import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Java067 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181926?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        int n = Integer.parseInt(scanner.nextLine());

        String inputString = scanner.nextLine();
        String control = inputString.substring(1, inputString.length() - 1);

        System.out.println(solution.solution(n, control));
    }

    private static class Solution {
        public int solution(int n, String control) {
            HashMap<String, Integer> hashMap = new HashMap<>();
            hashMap.putAll(Map.of("w", 1, "s", -1, "d", 10, "a", -10));

            for (int i = 0; i < control.length(); i++) {
                n += hashMap.get("" + control.charAt(i));
            }
            return n;
        }
    }
}

/*
0
"wsdawsdassw"
 */