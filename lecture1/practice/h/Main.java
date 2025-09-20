import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int a = Integer.parseInt(scanner.next());

        is_prime(a);
    }

    public static void is_prime(int n) {
        boolean[] sieve = new boolean[n + 1];

        int i = 2;
        while (i * i < n + 1) {
            for (int j = i; j < n + 1; j += i) {
                sieve[j] = true;
            }
            i++;
        }

        sieve[1] = true;
        sieve[0] = true;

        if (sieve[n]) {
            System.out.println("NO");
        } else if (!sieve[n]) {
            System.out.println("YES");
        }
    }
}
