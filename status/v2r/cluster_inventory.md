# V2R cluster inventory

2026-09-24T10:51:34.106895+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324384518144 available bytes; 81.90% used; 112489099 free inodes.

server1 `/home`: 324384518144 available bytes; 81.90% used; 112489099 free inodes.

server1 `/tmp`: 324384518144 available bytes; 81.90% used; 112489099 free inodes.

server1 `/var/tmp`: 324384518144 available bytes; 81.90% used; 112489099 free inodes.

server1 `/mnt/raid5`: 499752103936 available bytes; 97.71% used; 337695263 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 57710333952 available bytes; 96.78% used; 110430389 free inodes.

server2 `/home`: 57710333952 available bytes; 96.78% used; 110430389 free inodes.

server2 `/tmp`: 57710333952 available bytes; 96.78% used; 110430389 free inodes.

server2 `/var/tmp`: 57710333952 available bytes; 96.78% used; 110430389 free inodes.

server2 `/mnt/raid5`: 511591174144 available bytes; 96.47% used; 445174507 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85776699392 available bytes; 95.21% used; 114196343 free inodes.

server3 `/home`: 85776699392 available bytes; 95.21% used; 114196343 free inodes.

server3 `/data`: 164085760000 available bytes; 97.73% used; 225817805 free inodes.

server3 `/tmp`: 85776699392 available bytes; 95.21% used; 114196343 free inodes.

server3 `/var/tmp`: 85776699392 available bytes; 95.21% used; 114196343 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105735225344 available bytes; 94.10% used; 114348943 free inodes.

server4 `/home`: 105735225344 available bytes; 94.10% used; 114348943 free inodes.

server4 `/data`: 132790116352 available bytes; 98.16% used; 225258305 free inodes.

server4 `/tmp`: 105735225344 available bytes; 94.10% used; 114348943 free inodes.

server4 `/var/tmp`: 105735225344 available bytes; 94.10% used; 114348943 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
