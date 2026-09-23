# V2R cluster inventory

2026-09-23T16:49:10.853618+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41400115200 available bytes; 97.69% used; 110435441 free inodes.

server2 `/home`: 41400115200 available bytes; 97.69% used; 110435441 free inodes.

server2 `/tmp`: 41400115200 available bytes; 97.69% used; 110435441 free inodes.

server2 `/var/tmp`: 41400115200 available bytes; 97.69% used; 110435441 free inodes.

server2 `/mnt/raid5`: 548268494848 available bytes; 96.21% used; 445217472 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 299940511744 available bytes; 83.26% used; 114285898 free inodes.

server3 `/home`: 299940511744 available bytes; 83.26% used; 114285898 free inodes.

server3 `/data`: 95329546240 available bytes; 98.68% used; 225853291 free inodes.

server3 `/tmp`: 299940511744 available bytes; 83.26% used; 114285898 free inodes.

server3 `/var/tmp`: 299940511744 available bytes; 83.26% used; 114285898 free inodes.
| server4 | True | ['1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111498248192 available bytes; 93.78% used; 114375793 free inodes.

server4 `/home`: 111498248192 available bytes; 93.78% used; 114375793 free inodes.

server4 `/data`: 35302572032 available bytes; 99.51% used; 225477932 free inodes.

server4 `/tmp`: 111498248192 available bytes; 93.78% used; 114375793 free inodes.

server4 `/var/tmp`: 111498248192 available bytes; 93.78% used; 114375793 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
