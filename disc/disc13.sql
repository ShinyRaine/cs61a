-- 2.1
-- Write a query that outputs the names of employees that Oliver Warbucks directly
-- supervises.
SELECT name FROM records WHERE supervisor = 'Oliver Warbucks';

-- 2.2
-- Write a query that outputs all information about employees that supervise themselves.
SELECT name FROM records WHERE supervisor = name;

-- 2.3
-- Write a query that outputs the names of all employees with salary greater than
-- 50,000 in alphabetical order.
SELECT name FROM records WHERE salary > 50000 ORDER BY name;

-- 3.1 Write a query that outputs the meeting days and times of all employees directly
-- supervised by Oliver Warbucks.
SELECT day, time FROM records, meetings 
WHERE records.division = meetings.division AND supervisor = 'Oliver Warbucks';

-- 3.2 Write a query that outputs the names of employees whose supervisor is in a different
-- division.
SELECT r1.name FROM records AS r1, records AS r2
WHERE r1.division != r2.division AND r1.supervisor = r2.name;

-- 3.3 Write a query that outputs the names of all pairs of employees that have a meeting
-- at the same time. Make sure that if A|B appears in your output, B|A does not
-- appear as well (A|A and B|B should additionally not appear).
SELECT r1.name, r2.name FROM records AS r1, records AS r2, meetings AS m1, meetings AS m2
WHERE r1.division = m1.division AND r2.division = m2.division
AND m1.day = m2.day AND m1.time = m2.time
AND r1.name < r2.name;

-- 4.1 Write a query that outputs each supervisor and the sum of salaries of all the employees they supervise.
SELECT supervisor, SUM(salary) FROM records GROUP BY supervisor;

-- 4.2 Write a query that outputs the days of the week for which fewer than 5 employees
-- have a meeting. You may assume no department has more than one meeting on a
-- given day.

SELECT day FROM meetings, records
WHERE meetings.division = records.division 
GROUP BY day
HAVING COUNT(*) < 5;

-- 4.3 Write a query that outputs all divisions for which there is more than one employee,
-- and all pairs of employees within that division that have a combined salary less
-- than 100,000.
SELECT r1.division, r1.name, r2.name FROM records AS r1, records AS r2
WHERE r1.division = r2.division AND r1.name < r2.name
AND (r1.salary + r2.salary) < 100000;

-- 5.1 Create a table called num_taught that contains three columns: professor, the
-- course they taught, and the number of times they taught each course.
CREATE TABLE num_taught AS
SELECT professor, course, COUNT(*) AS times FROM courses
GROUP BY professor, course;

-- 5.2 Write a query that outputs two professors and a course if they have taught that
-- course the same number of times. You may use the num taught table you created
-- in the previous question.
SELECT a.professor, b.professor, a.course FROM num_taught as a, num_taught as B
WHERE a.course = b.course AND a.professor < b.professor AND a.times = b.times;

-- 5.3 Write a query that outputs two professors if they co-taught (taught the same course
-- at the same time) the same course more than once.
SELECT a.professor, b.professor FROM courses AS a, courses AS b
WHERE a.course = b.course AND a.professor < b.professor AND a.semester = b.semester
GROUP BY a.professor, b.professor
HAVING COUNT(*) > 1;
