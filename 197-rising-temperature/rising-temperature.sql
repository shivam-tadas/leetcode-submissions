select w1.id from weather w1, weather w2
where subdate(w1.recordDate, 1) = w2.recordDate
and w2.temperature < w1.temperature;