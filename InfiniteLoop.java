public class InfiniteLoopExample {

    public static void main(String[] args) {
        // Infinite loop
        while (true) {
            System.out.println("This loop will run forever...");
            
            // Optional: Add a sleep to slow down the loop iteration
            try {
                Thread.sleep(1000); // Sleep for 1 second
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
