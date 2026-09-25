# V2R cluster inventory

2026-09-25T19:07:48.109062+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318733398016 available bytes; 82.22% used; 112476328 free inodes.

server1 `/home`: 318733398016 available bytes; 82.22% used; 112476328 free inodes.

server1 `/tmp`: 318733398016 available bytes; 82.22% used; 112476328 free inodes.

server1 `/var/tmp`: 318733398016 available bytes; 82.22% used; 112476328 free inodes.

server1 `/mnt/raid5`: 371005140992 available bytes; 98.30% used; 337540922 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23103438848 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23103438848 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23103438848 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23103438848 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 312705056768 available bytes; 97.84% used; 445065090 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84383805440 available bytes; 95.29% used; 114152623 free inodes.

server3 `/home`: 84383805440 available bytes; 95.29% used; 114152623 free inodes.

server3 `/data`: 131362492416 available bytes; 98.18% used; 225808980 free inodes.

server3 `/tmp`: 84383805440 available bytes; 95.29% used; 114152623 free inodes.

server3 `/var/tmp`: 84383805440 available bytes; 95.29% used; 114152623 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105606344704 available bytes; 94.11% used; 114349593 free inodes.

server4 `/home`: 105606344704 available bytes; 94.11% used; 114349593 free inodes.

server4 `/data`: 229669163008 available bytes; 96.83% used; 224931175 free inodes.

server4 `/tmp`: 105606344704 available bytes; 94.11% used; 114349593 free inodes.

server4 `/var/tmp`: 105606344704 available bytes; 94.11% used; 114349593 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
