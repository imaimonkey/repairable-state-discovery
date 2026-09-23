# V2R cluster inventory

2026-09-23T15:43:26.297882+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41426362368 available bytes; 97.69% used; 110435185 free inodes.

server2 `/home`: 41426362368 available bytes; 97.69% used; 110435185 free inodes.

server2 `/tmp`: 41426362368 available bytes; 97.69% used; 110435185 free inodes.

server2 `/var/tmp`: 41426362368 available bytes; 97.69% used; 110435185 free inodes.

server2 `/mnt/raid5`: 550389575680 available bytes; 96.20% used; 445223621 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 377320185856 available bytes; 78.94% used; 114302964 free inodes.

server3 `/home`: 377320185856 available bytes; 78.94% used; 114302964 free inodes.

server3 `/data`: 125358489600 available bytes; 98.27% used; 225855343 free inodes.

server3 `/tmp`: 377320185856 available bytes; 78.94% used; 114302964 free inodes.

server3 `/var/tmp`: 377320185856 available bytes; 78.94% used; 114302964 free inodes.
| server4 | True | ['1', '2', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111499423744 available bytes; 93.78% used; 114375780 free inodes.

server4 `/home`: 111499423744 available bytes; 93.78% used; 114375780 free inodes.

server4 `/data`: 38742654976 available bytes; 99.46% used; 225494996 free inodes.

server4 `/tmp`: 111499423744 available bytes; 93.78% used; 114375780 free inodes.

server4 `/var/tmp`: 111499423744 available bytes; 93.78% used; 114375780 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
