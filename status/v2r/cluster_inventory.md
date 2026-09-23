# V2R cluster inventory

2026-09-23T17:57:52.786359+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41369092096 available bytes; 97.69% used; 110435428 free inodes.

server2 `/home`: 41369092096 available bytes; 97.69% used; 110435428 free inodes.

server2 `/tmp`: 41369092096 available bytes; 97.69% used; 110435428 free inodes.

server2 `/var/tmp`: 41369092096 available bytes; 97.69% used; 110435428 free inodes.

server2 `/mnt/raid5`: 546120429568 available bytes; 96.23% used; 445215356 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 294319386624 available bytes; 83.58% used; 114270139 free inodes.

server3 `/home`: 294319386624 available bytes; 83.58% used; 114270139 free inodes.

server3 `/data`: 52992192512 available bytes; 99.27% used; 225851521 free inodes.

server3 `/tmp`: 294319386624 available bytes; 83.58% used; 114270139 free inodes.

server3 `/var/tmp`: 294319386624 available bytes; 83.58% used; 114270139 free inodes.
| server4 | True | ['1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111488344064 available bytes; 93.78% used; 114375771 free inodes.

server4 `/home`: 111488344064 available bytes; 93.78% used; 114375771 free inodes.

server4 `/data`: 1256566784 available bytes; 99.98% used; 225457908 free inodes.

server4 `/tmp`: 111488344064 available bytes; 93.78% used; 114375771 free inodes.

server4 `/var/tmp`: 111488344064 available bytes; 93.78% used; 114375771 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
