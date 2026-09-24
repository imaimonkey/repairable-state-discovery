# V2R cluster inventory

2026-09-24T00:13:56.405736+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325570105344 available bytes; 81.84% used; 112500765 free inodes.

server1 `/home`: 325570105344 available bytes; 81.84% used; 112500765 free inodes.

server1 `/tmp`: 325570105344 available bytes; 81.84% used; 112500765 free inodes.

server1 `/var/tmp`: 325570105344 available bytes; 81.84% used; 112500765 free inodes.

server1 `/mnt/raid5`: 1209623687168 available bytes; 94.45% used; 337735324 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41008816128 available bytes; 97.71% used; 110432402 free inodes.

server2 `/home`: 41008816128 available bytes; 97.71% used; 110432402 free inodes.

server2 `/tmp`: 41008816128 available bytes; 97.71% used; 110432402 free inodes.

server2 `/var/tmp`: 41008816128 available bytes; 97.71% used; 110432402 free inodes.

server2 `/mnt/raid5`: 533298302976 available bytes; 96.32% used; 445204190 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292557516800 available bytes; 83.67% used; 114208757 free inodes.

server3 `/home`: 292557516800 available bytes; 83.67% used; 114208757 free inodes.

server3 `/data`: 82253864960 available bytes; 98.86% used; 225844507 free inodes.

server3 `/tmp`: 292557516800 available bytes; 83.67% used; 114208757 free inodes.

server3 `/var/tmp`: 292557516800 available bytes; 83.67% used; 114208757 free inodes.
| server4 | True | ['3', '4', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106108096512 available bytes; 94.08% used; 114350791 free inodes.

server4 `/home`: 106108096512 available bytes; 94.08% used; 114350791 free inodes.

server4 `/data`: 292910137344 available bytes; 95.95% used; 225414568 free inodes.

server4 `/tmp`: 106108096512 available bytes; 94.08% used; 114350791 free inodes.

server4 `/var/tmp`: 106108096512 available bytes; 94.08% used; 114350791 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
