class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> stack = new Stack<>();

        for (String op : operations) {
            if (!op.equals("C") && !op.equals("D") && !op.equals("+")) {
                stack.push(Integer.parseInt(op));
            } else if (op.equals("C")) {
                stack.pop();
            } else if (op.equals("D")) {
                int n = stack.peek() * 2;
                stack.push(n);
            } else if (op.equals("+")) {
                int n1 = stack.get(stack.size() - 1);
                int n2 = stack.get(stack.size() - 2);
                stack.push(n1 + n2);
            }
        }

        int sum = 0;
        for (int num : stack) {
            sum += num;
        }

        return sum;
    }
}
