import java.util.Scanner;

public class Java015 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120811
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] inputArr = inputString.substring(1, inputString.length() - 1).split(", ");

        int[] numbers = new int[inputArr.length];

        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = Integer.parseInt(inputArr[i]);
        }

        System.out.println(solution.solution(numbers));
    }

    private static class Solution {
        public int solution(int[] array) {
            array = sort(array);
            return array[array.length/2];
        }

        public int[] sort(int[] array) {
            for (int i = 0; i < array.length - 1; i++) {
                for (int j = i + 1; j < array.length; j++) {
                    if (array[i] > array[j]) {
                        int temp = array[i];
                        array[i] = array[j];
                        array[j] = temp;
                    }
                }
            }
            return array;
        }
    }
}

// [1, 2, 7, 10, 11]
// [9, -1, 0]