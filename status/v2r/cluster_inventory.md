# V2R cluster inventory

2026-09-23T18:52:48.841241+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['6', '7'] | [] | reference_compatible=False |

server2 `/`: 41344917504 available bytes; 97.69% used; 110435448 free inodes.

server2 `/home`: 41344917504 available bytes; 97.69% used; 110435448 free inodes.

server2 `/tmp`: 41344917504 available bytes; 97.69% used; 110435448 free inodes.

server2 `/var/tmp`: 41344917504 available bytes; 97.69% used; 110435448 free inodes.

server2 `/mnt/raid5`: 543721058304 available bytes; 96.24% used; 445213235 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 294128779264 available bytes; 83.59% used; 114261481 free inodes.

server3 `/home`: 294128779264 available bytes; 83.59% used; 114261481 free inodes.

server3 `/data`: 52820729856 available bytes; 99.27% used; 225846678 free inodes.

server3 `/tmp`: 294128779264 available bytes; 83.59% used; 114261481 free inodes.

server3 `/var/tmp`: 294128779264 available bytes; 83.59% used; 114261481 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111411888128 available bytes; 93.78% used; 114373047 free inodes.

server4 `/home`: 111411888128 available bytes; 93.78% used; 114373047 free inodes.

server4 `/data`: 17412096 available bytes; 100.00% used; 225458133 free inodes.

server4 `/tmp`: 111411888128 available bytes; 93.78% used; 114373047 free inodes.

server4 `/var/tmp`: 111411888128 available bytes; 93.78% used; 114373047 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
