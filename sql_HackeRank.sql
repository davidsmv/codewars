-- Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than 137.2345. Round your answer to  decimal places.
-- https://www.hackerrank.com/challenges/weather-observation-station-15/problem?isFullScreen=true&h_r=next-challenge&h_v=zen


select round(LONG_W,4)
from station
where LAT_N = (select max(LAT_N) from station where  LAT_N < 137.2345)