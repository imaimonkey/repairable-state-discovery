# V2R cluster inventory

2026-09-23T17:56:21.310092+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41369370624 available bytes; 97.69% used; 110435428 free inodes.

server2 `/home`: 41369370624 available bytes; 97.69% used; 110435428 free inodes.

server2 `/tmp`: 41369370624 available bytes; 97.69% used; 110435428 free inodes.

server2 `/var/tmp`: 41369370624 available bytes; 97.69% used; 110435428 free inodes.

server2 `/mnt/raid5`: 546144231424 available bytes; 96.23% used; 445215179 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 294320132096 available bytes; 83.58% used; 114268863 free inodes.

server3 `/home`: 294320132096 available bytes; 83.58% used; 114268863 free inodes.

server3 `/data`: 52996423680 available bytes; 99.27% used; 225851541 free inodes.

server3 `/tmp`: 294320132096 available bytes; 83.58% used; 114268863 free inodes.

server3 `/var/tmp`: 294320132096 available bytes; 83.58% used; 114268863 free inodes.
| server4 | True | ['1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111488364544 available bytes; 93.78% used; 114375771 free inodes.

server4 `/home`: 111488364544 available bytes; 93.78% used; 114375771 free inodes.

server4 `/data`: 2677297152 available bytes; 99.96% used; 225466228 free inodes.

server4 `/tmp`: 111488364544 available bytes; 93.78% used; 114375771 free inodes.

server4 `/var/tmp`: 111488364544 available bytes; 93.78% used; 114375771 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
