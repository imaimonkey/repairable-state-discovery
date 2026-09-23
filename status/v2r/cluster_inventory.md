# V2R cluster inventory

2026-09-23T17:42:37.648632+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41373097984 available bytes; 97.69% used; 110435438 free inodes.

server2 `/home`: 41373097984 available bytes; 97.69% used; 110435438 free inodes.

server2 `/tmp`: 41373097984 available bytes; 97.69% used; 110435438 free inodes.

server2 `/var/tmp`: 41373097984 available bytes; 97.69% used; 110435438 free inodes.

server2 `/mnt/raid5`: 546006290432 available bytes; 96.23% used; 445215543 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 294335959040 available bytes; 83.57% used; 114271702 free inodes.

server3 `/home`: 294335959040 available bytes; 83.57% used; 114271702 free inodes.

server3 `/data`: 53040381952 available bytes; 99.27% used; 225851798 free inodes.

server3 `/tmp`: 294335959040 available bytes; 83.57% used; 114271702 free inodes.

server3 `/var/tmp`: 294335959040 available bytes; 83.57% used; 114271702 free inodes.
| server4 | True | ['1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111488626688 available bytes; 93.78% used; 114375784 free inodes.

server4 `/home`: 111488626688 available bytes; 93.78% used; 114375784 free inodes.

server4 `/data`: 6344646656 available bytes; 99.91% used; 225468853 free inodes.

server4 `/tmp`: 111488626688 available bytes; 93.78% used; 114375784 free inodes.

server4 `/var/tmp`: 111488626688 available bytes; 93.78% used; 114375784 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
