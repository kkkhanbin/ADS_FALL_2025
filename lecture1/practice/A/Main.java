
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int a = Integer.parseInt(scanner.next());

        for (int i = 0; i < a; i++) {
            int n = Integer.parseInt(scanner.next());
            cards(n);
        }
    }

    private static long gcd(long a, long b) {
        if (a % b == 0) { return b; } return gcd(b, a % b);
    }

    private static void cards(int n) {
        Queue<Integer> cards = new LinkedList<>();

        for (int i = n; i > 0; i--) {
            cards.add(i);

            for (int j = i; j > 0; j--) {
                cards.add(cards.remove());
            }
        }

        String output = "";
        while (!cards.isEmpty()) {
            output = String.valueOf(cards.remove()) + " " + output;
        }

        System.out.println(output);
    }
}
