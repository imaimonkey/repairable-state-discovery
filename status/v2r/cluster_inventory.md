# V2R cluster inventory

2026-09-23T18:45:11.247696+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41344655360 available bytes; 97.69% used; 110435440 free inodes.

server2 `/home`: 41344655360 available bytes; 97.69% used; 110435440 free inodes.

server2 `/tmp`: 41344655360 available bytes; 97.69% used; 110435440 free inodes.

server2 `/var/tmp`: 41344655360 available bytes; 97.69% used; 110435440 free inodes.

server2 `/mnt/raid5`: 544492277760 available bytes; 96.24% used; 445213712 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 294168408064 available bytes; 83.58% used; 114266461 free inodes.

server3 `/home`: 294168408064 available bytes; 83.58% used; 114266461 free inodes.

server3 `/data`: 52840263680 available bytes; 99.27% used; 225847186 free inodes.

server3 `/tmp`: 294168408064 available bytes; 83.58% used; 114266461 free inodes.

server3 `/var/tmp`: 294168408064 available bytes; 83.58% used; 114266461 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111411060736 available bytes; 93.78% used; 114373058 free inodes.

server4 `/home`: 111411060736 available bytes; 93.78% used; 114373058 free inodes.

server4 `/data`: 16281600 available bytes; 100.00% used; 225458132 free inodes.

server4 `/tmp`: 111411060736 available bytes; 93.78% used; 114373058 free inodes.

server4 `/var/tmp`: 111411060736 available bytes; 93.78% used; 114373058 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
