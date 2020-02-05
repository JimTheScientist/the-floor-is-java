

```
import math #important because you need to do math

self.angle =  NetworkTables.getTable("limelight").getNumber('ty') #should get the angle from the limelight
self.angleTwo = self.angle + 45 #plus 45 because that is what it will be mounted at I believe
self.distance = 96.19/(math.tan(math.radians(self.angleTwo))) #the math to calculate distance in python, also the 96.19 is from the real target height and about where the limelight is mounted on the CAD file.

self.dash.putString ("The distance away from the target is:", self.distance,) #writes to dashboard what the distance is
```