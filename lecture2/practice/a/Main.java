import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int a = Integer.parseInt(scanner.next());
        Queue<Integer> q = new LinkedList<>();

        for (int i = 0; i < a; i++) {
            int n = Integer.parseInt(scanner.next());

            q.add(n);
        }

        int n = Integer.parseInt(scanner.next());

        int min_i = 0;
        int min_diff = Math.abs((int) q.remove() - n);
        for (int i = 1; i < a; i++) {
            Integer cur = q.remove();

            if (Math.abs((int) cur - n) < min_diff) {
                min_i = i;
                min_diff = Math.abs((int) cur - n);
            }


        }

        System.out.println(min_i);
    }

}
