# V2R cluster inventory

2026-09-25T17:17:40.906247+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318680211456 available bytes; 82.22% used; 112476346 free inodes.

server1 `/home`: 318680211456 available bytes; 82.22% used; 112476346 free inodes.

server1 `/tmp`: 318680211456 available bytes; 82.22% used; 112476346 free inodes.

server1 `/var/tmp`: 318680211456 available bytes; 82.22% used; 112476346 free inodes.

server1 `/mnt/raid5`: 363858989056 available bytes; 98.33% used; 337543429 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23098183680 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23098183680 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23098183680 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23098183680 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 316412645376 available bytes; 97.81% used; 445068857 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84392808448 available bytes; 95.29% used; 114152614 free inodes.

server3 `/home`: 84392808448 available bytes; 95.29% used; 114152614 free inodes.

server3 `/data`: 132793614336 available bytes; 98.16% used; 225811575 free inodes.

server3 `/tmp`: 84392808448 available bytes; 95.29% used; 114152614 free inodes.

server3 `/var/tmp`: 84392808448 available bytes; 95.29% used; 114152614 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105626447872 available bytes; 94.11% used; 114349644 free inodes.

server4 `/home`: 105626447872 available bytes; 94.11% used; 114349644 free inodes.

server4 `/data`: 229876281344 available bytes; 96.82% used; 224933058 free inodes.

server4 `/tmp`: 105626447872 available bytes; 94.11% used; 114349644 free inodes.

server4 `/var/tmp`: 105626447872 available bytes; 94.11% used; 114349644 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
