# V2R cluster inventory

2026-09-23T15:44:57.761514+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41425850368 available bytes; 97.69% used; 110435185 free inodes.

server2 `/home`: 41425850368 available bytes; 97.69% used; 110435185 free inodes.

server2 `/tmp`: 41425850368 available bytes; 97.69% used; 110435185 free inodes.

server2 `/var/tmp`: 41425850368 available bytes; 97.69% used; 110435185 free inodes.

server2 `/mnt/raid5`: 550349074432 available bytes; 96.20% used; 445223491 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 377321095168 available bytes; 78.94% used; 114302950 free inodes.

server3 `/home`: 377321095168 available bytes; 78.94% used; 114302950 free inodes.

server3 `/data`: 125357060096 available bytes; 98.27% used; 225855300 free inodes.

server3 `/tmp`: 377321095168 available bytes; 78.94% used; 114302950 free inodes.

server3 `/var/tmp`: 377321095168 available bytes; 78.94% used; 114302950 free inodes.
| server4 | True | ['1', '2', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111499403264 available bytes; 93.78% used; 114375780 free inodes.

server4 `/home`: 111499403264 available bytes; 93.78% used; 114375780 free inodes.

server4 `/data`: 38739890176 available bytes; 99.46% used; 225494980 free inodes.

server4 `/tmp`: 111499403264 available bytes; 93.78% used; 114375780 free inodes.

server4 `/var/tmp`: 111499403264 available bytes; 93.78% used; 114375780 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
