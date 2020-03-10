# KPI Berry Hometask

## Start application

To start app:
```
docker-compose up --build -d
```

To turn off app:
```
docker-compose down
```

## API endpoints

|Description|Method|Endpoint|Parametrs|Expected response|
|-----------|------|--------|---------|-----------------|
|List all readings|GET|/all-readings|none|id, timestamp, value of all readings
|Get statistics|GET|/statistics|from=YYYY-MM-DD&to=YYYY-MM-DD|count, mean, variance, normal_dist, confidence_interval_start, confidence_interval_end, stationary 
|Get reading by id|GET|/reading/<:id>|none|id, timestamp, value of reading
|Add reading|POST|/reading|value=float|id, timestamp, value of created reading
|Edit reading by id|PUT|/reading/<:id>|value=float|id, timestamp, value of edited reading
|Delete reading by id|DELETE|/reading/<:id>|none|empty string

## Database

Application will look for _app/test.db_. There is testing db already included.

If you want to make new db:

1. Go to _app_ directory
2. Remove _test.db_
3. Type python terminal
4. In new command promt type:
```
from app import db
db.create_all()
```
5. Exit command promt. Then you need to rebuild docker image:
```
docker-compose up --build -d
```