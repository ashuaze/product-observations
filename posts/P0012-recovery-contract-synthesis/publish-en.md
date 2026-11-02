### 1/6

1/6 Before extending an undo window, ask two questions:
Can the recovery path survive the original failure?
Does it restore the outcome the user needs?

A longer deadline cannot fix an inaccessible key, erased history or missing permissions.

### 2/6

2/6 Apple warns against storing your Recovery Key in Apple Passwords, iCloud Photos, Notes or iCloud Drive: losing account access can lock you out of the key too.

A fallback that depends on the failed system may fail with it.

https://support.apple.com/en-us/109345

### 3/6

3/6 S3 Versioning keeps history after a normal delete. But a caller allowed to delete specific versions can erase that history.

For accidental deletion, versions may suffice. For compromised credentials, check who can destroy the fallback.

https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjectVersions.html

### 4/6

4/6 GitHub can restore eligible deleted repositories within 90 days, but not their team permissions.

"The repository is back" and "the team can work again" are different acceptance criteria. Test both.

https://docs.github.com/en/repositories/creating-and-managing-repositories/restoring-a-deleted-repository

### 5/6

5/6 Complete rollback is not always the goal. A Stripe refund can return money after a payment succeeds, but it can be pending or fail.

That is recovery through compensation. Track money returned, not just "refund requested."

https://docs.stripe.com/refunds

### 6/6

6/6 In a recovery test, make the scenario's lost device, credential or admin access unavailable.

Measure task completion, not clicks on Restore. Then account for retained data, extra access paths and manual repair.

Fix the failed link, not just the timer.
