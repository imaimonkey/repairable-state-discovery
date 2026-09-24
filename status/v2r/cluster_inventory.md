# V2R cluster inventory

2026-09-24T00:46:24.277392+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 325537062912 available bytes; 81.84% used; 112500424 free inodes.

server1 `/home`: 325537062912 available bytes; 81.84% used; 112500424 free inodes.

server1 `/tmp`: 325537062912 available bytes; 81.84% used; 112500424 free inodes.

server1 `/var/tmp`: 325537062912 available bytes; 81.84% used; 112500424 free inodes.

server1 `/mnt/raid5`: 1075981946880 available bytes; 95.06% used; 337734982 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40981389312 available bytes; 97.71% used; 110432276 free inodes.

server2 `/home`: 40981389312 available bytes; 97.71% used; 110432276 free inodes.

server2 `/tmp`: 40981389312 available bytes; 97.71% used; 110432276 free inodes.

server2 `/var/tmp`: 40981389312 available bytes; 97.71% used; 110432276 free inodes.

server2 `/mnt/raid5`: 531740852224 available bytes; 96.33% used; 445202953 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292342153216 available bytes; 83.69% used; 114188827 free inodes.

server3 `/home`: 292342153216 available bytes; 83.69% used; 114188827 free inodes.

server3 `/data`: 82217246720 available bytes; 98.86% used; 225843580 free inodes.

server3 `/tmp`: 292342153216 available bytes; 83.69% used; 114188827 free inodes.

server3 `/var/tmp`: 292342153216 available bytes; 83.69% used; 114188827 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106052157440 available bytes; 94.08% used; 114349914 free inodes.

server4 `/home`: 106052157440 available bytes; 94.08% used; 114349914 free inodes.

server4 `/data`: 292918947840 available bytes; 95.95% used; 225414576 free inodes.

server4 `/tmp`: 106052157440 available bytes; 94.08% used; 114349914 free inodes.

server4 `/var/tmp`: 106052157440 available bytes; 94.08% used; 114349914 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
