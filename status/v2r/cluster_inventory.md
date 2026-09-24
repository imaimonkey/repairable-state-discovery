# V2R cluster inventory

2026-09-24T21:19:01.362046+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323961749504 available bytes; 81.93% used; 112481400 free inodes.

server1 `/home`: 323961749504 available bytes; 81.93% used; 112481400 free inodes.

server1 `/tmp`: 323961749504 available bytes; 81.93% used; 112481400 free inodes.

server1 `/var/tmp`: 323961749504 available bytes; 81.93% used; 112481400 free inodes.

server1 `/mnt/raid5`: 415525740544 available bytes; 98.09% used; 337628760 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 30137241600 available bytes; 98.32% used; 110411360 free inodes.

server2 `/home`: 30137241600 available bytes; 98.32% used; 110411360 free inodes.

server2 `/tmp`: 30137241600 available bytes; 98.32% used; 110411360 free inodes.

server2 `/var/tmp`: 30137241600 available bytes; 98.32% used; 110411360 free inodes.

server2 `/mnt/raid5`: 490761678848 available bytes; 96.61% used; 445155476 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84383092736 available bytes; 95.29% used; 114156095 free inodes.

server3 `/home`: 84383092736 available bytes; 95.29% used; 114156095 free inodes.

server3 `/data`: 150489194496 available bytes; 97.92% used; 225803387 free inodes.

server3 `/tmp`: 84383092736 available bytes; 95.29% used; 114156095 free inodes.

server3 `/var/tmp`: 84383092736 available bytes; 95.29% used; 114156095 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105632452608 available bytes; 94.11% used; 114348350 free inodes.

server4 `/home`: 105632452608 available bytes; 94.11% used; 114348350 free inodes.

server4 `/data`: 64571383808 available bytes; 99.11% used; 225253361 free inodes.

server4 `/tmp`: 105632452608 available bytes; 94.11% used; 114348350 free inodes.

server4 `/var/tmp`: 105632452608 available bytes; 94.11% used; 114348350 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
