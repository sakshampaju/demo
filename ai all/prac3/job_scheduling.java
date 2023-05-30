import java.util.PriorityQueue;

class Job implements Comparable<Job> {
    private String name;
    private int priority;

    public Job(String name, int priority) {
        this.name = name;
        this.priority = priority;
    }

    public String getName() {
        return name;
    }

    public int getPriority() {
        return priority;
    }

    @Override
    public int compareTo(Job other) {
        return Integer.compare(this.priority, other.priority);
    }
}

public class JobScheduler {
    public static void main(String[] args) {
        PriorityQueue<Job> jobQueue = new PriorityQueue<>();

        // Adding jobs to the queue
        jobQueue.add(new Job("Job 1", 3));
        jobQueue.add(new Job("Job 2", 1));
        jobQueue.add(new Job("Job 3", 2));

        // Processing jobs
        while (!jobQueue.isEmpty()) {
            Job job = jobQueue.poll();
            System.out.println("Processing job: " + job.getName());
            // Perform job processing here
        }
    }
}
/*
The code you provided is correct and will work as a job scheduling implementation using a `PriorityQueue`. It imports the `PriorityQueue` class from the `java.util` package and uses it to manage the job queue based on their priorities.

The `Job` class represents a job with a name and priority, implementing the `Comparable` interface to compare jobs based on their priorities.

The `JobScheduler` class demonstrates the usage of the `PriorityQueue` to schedule and process jobs. Jobs are added to the queue using the `add` method, and then processed in the order of their priorities using the `poll` method.

This code will compile and run as expected, providing a simple job scheduling mechanism.

*/
