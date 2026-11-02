### 1/5

1/5 Amazon S3 has a delete action that often adds data instead of removing it.

With Versioning enabled, a normal DELETE adds a delete marker. The object returns 404, but older versions remain. Remove the marker and the latest prior version becomes current.

### 2/5

2/5 The catch: S3 Versioning is off by default. Protection must exist before the mistake.

And every retained version is a full object, not a diff. Recovery capacity is a decision made at setup—and it carries an ongoing storage cost.

https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html

### 3/5

3/5 Versioning is not immutability. An authorized caller can permanently delete a version by ID, and lifecycle rules can expire noncurrent versions.

History survives only while permissions and retention rules preserve it.

https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjectVersions.html

### 4/5

4/5 S3 Object Lock can protect versions for a retention period or legal hold.

It requires Versioning, but still permits new versions and delete markers. Its promise is “cannot erase this version,” not “nothing can change.”

https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html

### 5/5

5/5 Product lesson: recovery is mostly decided before the error.

Define when history begins, who can destroy it, how long it lasts, what it costs, and whether “delete” hides, expires or erases. An undo shown afterward cannot recover state the system never kept.
