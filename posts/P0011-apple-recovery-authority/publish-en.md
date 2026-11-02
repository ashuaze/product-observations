### 1/6

1/6 Account recovery is a security feature—and a backdoor if designed badly.

Under standard iCloud protection, Apple stores keys for many data categories so it can help with recovery. Advanced Data Protection moves that authority away from the provider.

### 2/6

2/6 With Advanced Data Protection, trusted devices hold keys for most iCloud data; Apple says it cannot help recover it. Users must first set a Recovery Contact or Recovery Key.

Stronger privacy changes the recovery contract—not just encryption.

https://support.apple.com/en-us/102651

### 3/6

3/6 A Recovery Contact can generate a six-digit code, but cannot access your account or data. That separates assistance from access.

Failure condition: the person—and a compatible Apple device—must be available when you need them.

https://support.apple.com/en-us/102641

### 4/6

4/6 A 28-character Recovery Key disables Apple’s standard account recovery. Lose the key after losing account access, and Apple says you can be locked out permanently.

Self-custody removes a provider backstop; it does not remove recovery risk.

https://support.apple.com/en-us/109345

### 5/6

5/6 A 2024 USENIX study surveyed 281 users of an E2EE email service and analyzed 197 support requests. Users valued recovery-code security, but faced lost or non-working codes and misconceptions about what support could restore.

https://www.usenix.org/conference/usenixsecurity24/presentation/h%C3%B6ltervennhoff

### 6/6

6/6 Design recovery authority by threat model, not convenience alone.

Provider recovery: more help, more trust.
Trusted contact: distributed help, human dependency.
Recovery key: maximum control, maximum responsibility.

Show the failure state before opt-in.
