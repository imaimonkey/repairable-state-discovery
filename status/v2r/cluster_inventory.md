# V2R cluster inventory

2026-09-23T20:44:10.518120+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325735649280 available bytes; 81.83% used; 112501749 free inodes.

server1 `/home`: 325735649280 available bytes; 81.83% used; 112501749 free inodes.

server1 `/tmp`: 325735649280 available bytes; 81.83% used; 112501749 free inodes.

server1 `/var/tmp`: 325735649280 available bytes; 81.83% used; 112501749 free inodes.

server1 `/mnt/raid5`: 1388251525120 available bytes; 93.63% used; 337740878 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41132732416 available bytes; 97.71% used; 110432775 free inodes.

server2 `/home`: 41132732416 available bytes; 97.71% used; 110432775 free inodes.

server2 `/tmp`: 41132732416 available bytes; 97.71% used; 110432775 free inodes.

server2 `/var/tmp`: 41132732416 available bytes; 97.71% used; 110432775 free inodes.

server2 `/mnt/raid5`: 539927506944 available bytes; 96.27% used; 445209931 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293129711616 available bytes; 83.64% used; 114216731 free inodes.

server3 `/home`: 293129711616 available bytes; 83.64% used; 114216731 free inodes.

server3 `/data`: 52575277056 available bytes; 99.27% used; 225843102 free inodes.

server3 `/tmp`: 293129711616 available bytes; 83.64% used; 114216731 free inodes.

server3 `/var/tmp`: 293129711616 available bytes; 83.64% used; 114216731 free inodes.
| server4 | True | ['1', '2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106514980864 available bytes; 94.06% used; 114356127 free inodes.

server4 `/home`: 106514980864 available bytes; 94.06% used; 114356127 free inodes.

server4 `/data`: 300660666368 available bytes; 95.84% used; 225460156 free inodes.

server4 `/tmp`: 106514980864 available bytes; 94.06% used; 114356127 free inodes.

server4 `/var/tmp`: 106514980864 available bytes; 94.06% used; 114356127 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
