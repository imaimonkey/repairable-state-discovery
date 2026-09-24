# V2R cluster inventory

2026-09-24T00:49:29.717400+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 325533999104 available bytes; 81.84% used; 112500387 free inodes.

server1 `/home`: 325533999104 available bytes; 81.84% used; 112500387 free inodes.

server1 `/tmp`: 325533999104 available bytes; 81.84% used; 112500387 free inodes.

server1 `/var/tmp`: 325533999104 available bytes; 81.84% used; 112500387 free inodes.

server1 `/mnt/raid5`: 1063282601984 available bytes; 95.12% used; 337734888 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40982052864 available bytes; 97.71% used; 110432265 free inodes.

server2 `/home`: 40982052864 available bytes; 97.71% used; 110432265 free inodes.

server2 `/tmp`: 40982052864 available bytes; 97.71% used; 110432265 free inodes.

server2 `/var/tmp`: 40982052864 available bytes; 97.71% used; 110432265 free inodes.

server2 `/mnt/raid5`: 532182892544 available bytes; 96.32% used; 445202837 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292341338112 available bytes; 83.69% used; 114188814 free inodes.

server3 `/home`: 292341338112 available bytes; 83.69% used; 114188814 free inodes.

server3 `/data`: 82172256256 available bytes; 98.86% used; 225843497 free inodes.

server3 `/tmp`: 292341338112 available bytes; 83.69% used; 114188814 free inodes.

server3 `/var/tmp`: 292341338112 available bytes; 83.69% used; 114188814 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106047025152 available bytes; 94.08% used; 114349829 free inodes.

server4 `/home`: 106047025152 available bytes; 94.08% used; 114349829 free inodes.

server4 `/data`: 292883345408 available bytes; 95.95% used; 225414549 free inodes.

server4 `/tmp`: 106047025152 available bytes; 94.08% used; 114349829 free inodes.

server4 `/var/tmp`: 106047025152 available bytes; 94.08% used; 114349829 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
