public class test {
	
	public int fib(n) {
		int fib0 = 0;
		int fib1 = 1;
		if (n == 0) {
			return fib0;
		}
		if (n == 1) {
			return fib1;
		}
		for (int i = 0, i < n - 1; i++) {
			int temp = fib0 + fib1;
			fib0 = fib1;
			fib1 = temp;
		}
		return fib1;
	}
}
