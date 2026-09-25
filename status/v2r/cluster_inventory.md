# V2R cluster inventory

2026-09-25T16:16:24.285131+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318671626240 available bytes; 82.22% used; 112476328 free inodes.

server1 `/home`: 318671626240 available bytes; 82.22% used; 112476328 free inodes.

server1 `/tmp`: 318671626240 available bytes; 82.22% used; 112476328 free inodes.

server1 `/var/tmp`: 318671626240 available bytes; 82.22% used; 112476328 free inodes.

server1 `/mnt/raid5`: 363900809216 available bytes; 98.33% used; 337544951 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23108808704 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23108808704 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23108808704 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23108808704 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 318756655104 available bytes; 97.80% used; 445070879 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84401938432 available bytes; 95.29% used; 114152674 free inodes.

server3 `/home`: 84401938432 available bytes; 95.29% used; 114152674 free inodes.

server3 `/data`: 134928474112 available bytes; 98.14% used; 225806161 free inodes.

server3 `/tmp`: 84401938432 available bytes; 95.29% used; 114152674 free inodes.

server3 `/var/tmp`: 84401938432 available bytes; 95.29% used; 114152674 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105636507648 available bytes; 94.11% used; 114349647 free inodes.

server4 `/home`: 105636507648 available bytes; 94.11% used; 114349647 free inodes.

server4 `/data`: 230238507008 available bytes; 96.82% used; 224934481 free inodes.

server4 `/tmp`: 105636507648 available bytes; 94.11% used; 114349647 free inodes.

server4 `/var/tmp`: 105636507648 available bytes; 94.11% used; 114349647 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
