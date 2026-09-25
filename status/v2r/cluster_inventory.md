# V2R cluster inventory

2026-09-25T20:13:31.934212+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318710931456 available bytes; 82.22% used; 112476342 free inodes.

server1 `/home`: 318710931456 available bytes; 82.22% used; 112476342 free inodes.

server1 `/tmp`: 318710931456 available bytes; 82.22% used; 112476342 free inodes.

server1 `/var/tmp`: 318710931456 available bytes; 82.22% used; 112476342 free inodes.

server1 `/mnt/raid5`: 370711887872 available bytes; 98.30% used; 337540587 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23086899200 available bytes; 98.71% used; 110407932 free inodes.

server2 `/home`: 23086899200 available bytes; 98.71% used; 110407932 free inodes.

server2 `/tmp`: 23086899200 available bytes; 98.71% used; 110407932 free inodes.

server2 `/var/tmp`: 23086899200 available bytes; 98.71% used; 110407932 free inodes.

server2 `/mnt/raid5`: 310886723584 available bytes; 97.85% used; 445063387 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84381540352 available bytes; 95.29% used; 114152620 free inodes.

server3 `/home`: 84381540352 available bytes; 95.29% used; 114152620 free inodes.

server3 `/data`: 127192047616 available bytes; 98.24% used; 225808320 free inodes.

server3 `/tmp`: 84381540352 available bytes; 95.29% used; 114152620 free inodes.

server3 `/var/tmp`: 84381540352 available bytes; 95.29% used; 114152620 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105673400320 available bytes; 94.10% used; 114349570 free inodes.

server4 `/home`: 105673400320 available bytes; 94.10% used; 114349570 free inodes.

server4 `/data`: 229426229248 available bytes; 96.83% used; 224929389 free inodes.

server4 `/tmp`: 105673400320 available bytes; 94.10% used; 114349570 free inodes.

server4 `/var/tmp`: 105673400320 available bytes; 94.10% used; 114349570 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
