# V2R cluster inventory

2026-09-23T15:48:00.908177+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41425268736 available bytes; 97.69% used; 110435185 free inodes.

server2 `/home`: 41425268736 available bytes; 97.69% used; 110435185 free inodes.

server2 `/tmp`: 41425268736 available bytes; 97.69% used; 110435185 free inodes.

server2 `/var/tmp`: 41425268736 available bytes; 97.69% used; 110435185 free inodes.

server2 `/mnt/raid5`: 550258552832 available bytes; 96.20% used; 445223308 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 376859869184 available bytes; 78.97% used; 114285338 free inodes.

server3 `/home`: 376859869184 available bytes; 78.97% used; 114285338 free inodes.

server3 `/data`: 125340557312 available bytes; 98.27% used; 225854824 free inodes.

server3 `/tmp`: 376859869184 available bytes; 78.97% used; 114285338 free inodes.

server3 `/var/tmp`: 376859869184 available bytes; 78.97% used; 114285338 free inodes.
| server4 | True | ['1', '2', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111499345920 available bytes; 93.78% used; 114375780 free inodes.

server4 `/home`: 111499345920 available bytes; 93.78% used; 114375780 free inodes.

server4 `/data`: 38682193920 available bytes; 99.47% used; 225494956 free inodes.

server4 `/tmp`: 111499345920 available bytes; 93.78% used; 114375780 free inodes.

server4 `/var/tmp`: 111499345920 available bytes; 93.78% used; 114375780 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
