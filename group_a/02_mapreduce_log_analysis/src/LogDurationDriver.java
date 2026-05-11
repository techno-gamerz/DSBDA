import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class LogDurationDriver extends Configured implements Tool {

  public static class DurationMapper extends Mapper<LongWritable, Text, Text, LongWritable> {
    private final SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
    private final Text outKey = new Text();
    private final LongWritable outValue = new LongWritable();

    @Override
    protected void map(LongWritable key, Text value, Context context)
        throws IOException, InterruptedException {
      String line = value.toString().trim();
      if (line.isEmpty() || line.startsWith("user,")) {
        return;
      }

      String[] parts = line.split(",", -1);
      if (parts.length < 3) {
        return;
      }

      String user = parts[0].trim();
      if (user.isEmpty()) {
        return;
      }

      try {
        Date start = format.parse(parts[1].trim());
        Date end = format.parse(parts[2].trim());
        long durationSeconds = (end.getTime() - start.getTime()) / 1000L;
        if (durationSeconds <= 0) {
          return;
        }
        outKey.set(user);
        outValue.set(durationSeconds);
        context.write(outKey, outValue);
      } catch (ParseException e) {
        // Skip bad rows
      }
    }
  }

  public static class DurationReducer extends Reducer<Text, LongWritable, Text, LongWritable> {
    @Override
    protected void reduce(Text key, Iterable<LongWritable> values, Context context)
        throws IOException, InterruptedException {
      long sum = 0L;
      for (LongWritable v : values) {
        sum += v.get();
      }
      context.write(key, new LongWritable(sum));
    }
  }

  public static class MaxMapper extends Mapper<LongWritable, Text, Text, Text> {
    private final Text outKey = new Text("max");
    private final Text outValue = new Text();

    @Override
    protected void map(LongWritable key, Text value, Context context)
        throws IOException, InterruptedException {
      String line = value.toString().trim();
      if (line.isEmpty()) {
        return;
      }
      String[] parts = line.split("\t", -1);
      if (parts.length < 2) {
        return;
      }
      String user = parts[0].trim();
      String total = parts[1].trim();
      if (user.isEmpty() || total.isEmpty()) {
        return;
      }
      outValue.set(user + "," + total);
      context.write(outKey, outValue);
    }
  }

  public static class MaxReducer extends Reducer<Text, Text, Text, LongWritable> {
    @Override
    protected void reduce(Text key, Iterable<Text> values, Context context)
        throws IOException, InterruptedException {
      long max = Long.MIN_VALUE;
      List<String> users = new ArrayList<String>();

      for (Text v : values) {
        String[] parts = v.toString().split(",", -1);
        if (parts.length < 2) {
          continue;
        }
        String user = parts[0].trim();
        String totalStr = parts[1].trim();
        if (user.isEmpty() || totalStr.isEmpty()) {
          continue;
        }
        long total = Long.parseLong(totalStr);
        if (total > max) {
          max = total;
          users.clear();
          users.add(user);
        } else if (total == max) {
          users.add(user);
        }
      }

      for (String user : users) {
        context.write(new Text(user), new LongWritable(max));
      }
    }
  }

  @Override
  public int run(String[] args) throws Exception {
    if (args.length != 3) {
      System.err.println("Usage: LogDurationDriver <input> <totalsOutput> <maxOutput>");
      return 1;
    }

    Configuration conf = getConf();

    Job job1 = Job.getInstance(conf, "log-duration-totals");
    job1.setJarByClass(LogDurationDriver.class);
    job1.setMapperClass(DurationMapper.class);
    job1.setReducerClass(DurationReducer.class);
    job1.setOutputKeyClass(Text.class);
    job1.setOutputValueClass(LongWritable.class);
    FileInputFormat.addInputPath(job1, new Path(args[0]));
    FileOutputFormat.setOutputPath(job1, new Path(args[1]));

    if (!job1.waitForCompletion(true)) {
      return 1;
    }

    Job job2 = Job.getInstance(conf, "log-duration-max");
    job2.setJarByClass(LogDurationDriver.class);
    job2.setMapperClass(MaxMapper.class);
    job2.setReducerClass(MaxReducer.class);
    job2.setOutputKeyClass(Text.class);
    job2.setOutputValueClass(Text.class);
    job2.setMapOutputKeyClass(Text.class);
    job2.setMapOutputValueClass(Text.class);
    job2.setNumReduceTasks(1);

    FileInputFormat.addInputPath(job2, new Path(args[1]));
    FileOutputFormat.setOutputPath(job2, new Path(args[2]));

    return job2.waitForCompletion(true) ? 0 : 1;
  }

  public static void main(String[] args) throws Exception {
    int exitCode = ToolRunner.run(new LogDurationDriver(), args);
    System.exit(exitCode);
  }
}
