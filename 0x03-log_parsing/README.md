# ALX Africa Project: Log Metrics

This project is part of the curriculum of ALX Africa. It focuses on writing a script that reads stdin line by line and computes metrics.

## Project Description

The script reads the standard input line by line. Each line follows this format:

```
<IP Address> - [<date>] “GET /projects/260 HTTP/1.1” <status code> <file size>
```


If the line format is different, the line is skipped.

After every 10 lines and/or a keyboard interruption (CTRL + C), the script prints the following statistics from the beginning:

- Total file size: `File size: <total size>`, where `<total size>` is the sum of all previous `<file size>`.

- Number of lines by status code. The possible status codes are 200, 301, 400, 401, 403, 404, 405, and 500. If a status code doesn’t appear or is not an integer, it is not printed. The format is `<status code>: <number>`. Status codes are printed in ascending order.
