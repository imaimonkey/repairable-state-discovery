# V2R cluster inventory

2026-09-24T10:09:39.037503+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324419784704 available bytes; 81.90% used; 112489453 free inodes.

server1 `/home`: 324419784704 available bytes; 81.90% used; 112489453 free inodes.

server1 `/tmp`: 324419784704 available bytes; 81.90% used; 112489453 free inodes.

server1 `/var/tmp`: 324419784704 available bytes; 81.90% used; 112489453 free inodes.

server1 `/mnt/raid5`: 500668420096 available bytes; 97.70% used; 337700241 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57745342464 available bytes; 96.78% used; 110430713 free inodes.

server2 `/home`: 57745342464 available bytes; 96.78% used; 110430713 free inodes.

server2 `/tmp`: 57745342464 available bytes; 96.78% used; 110430713 free inodes.

server2 `/var/tmp`: 57745342464 available bytes; 96.78% used; 110430713 free inodes.

server2 `/mnt/raid5`: 513365766144 available bytes; 96.45% used; 445176206 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85378355200 available bytes; 95.24% used; 114173476 free inodes.

server3 `/home`: 85378355200 available bytes; 95.24% used; 114173476 free inodes.

server3 `/data`: 164451840000 available bytes; 97.73% used; 225819096 free inodes.

server3 `/tmp`: 85378355200 available bytes; 95.24% used; 114173476 free inodes.

server3 `/var/tmp`: 85378355200 available bytes; 95.24% used; 114173476 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105747521536 available bytes; 94.10% used; 114349001 free inodes.

server4 `/home`: 105747521536 available bytes; 94.10% used; 114349001 free inodes.

server4 `/data`: 153505923072 available bytes; 97.88% used; 225258639 free inodes.

server4 `/tmp`: 105747521536 available bytes; 94.10% used; 114349001 free inodes.

server4 `/var/tmp`: 105747521536 available bytes; 94.10% used; 114349001 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
