# V2R cluster inventory

2026-09-25T20:57:51.990015+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318698434560 available bytes; 82.22% used; 112476306 free inodes.

server1 `/home`: 318698434560 available bytes; 82.22% used; 112476306 free inodes.

server1 `/tmp`: 318698434560 available bytes; 82.22% used; 112476306 free inodes.

server1 `/var/tmp`: 318698434560 available bytes; 82.22% used; 112476306 free inodes.

server1 `/mnt/raid5`: 368620445696 available bytes; 98.31% used; 337539531 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] |

server2 `/`: 22894084096 available bytes; 98.72% used; 110405680 free inodes.

server2 `/home`: 22894084096 available bytes; 98.72% used; 110405680 free inodes.

server2 `/tmp`: 22894084096 available bytes; 98.72% used; 110405680 free inodes.

server2 `/var/tmp`: 22894084096 available bytes; 98.72% used; 110405680 free inodes.

server2 `/mnt/raid5`: 302493220864 available bytes; 97.91% used; 445056378 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84362084352 available bytes; 95.29% used; 114152622 free inodes.

server3 `/home`: 84362084352 available bytes; 95.29% used; 114152622 free inodes.

server3 `/data`: 127097450496 available bytes; 98.24% used; 225807576 free inodes.

server3 `/tmp`: 84362084352 available bytes; 95.29% used; 114152622 free inodes.

server3 `/var/tmp`: 84362084352 available bytes; 95.29% used; 114152622 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105655144448 available bytes; 94.10% used; 114349519 free inodes.

server4 `/home`: 105655144448 available bytes; 94.10% used; 114349519 free inodes.

server4 `/data`: 227412611072 available bytes; 96.86% used; 224926431 free inodes.

server4 `/tmp`: 105655144448 available bytes; 94.10% used; 114349519 free inodes.

server4 `/var/tmp`: 105655144448 available bytes; 94.10% used; 114349519 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
