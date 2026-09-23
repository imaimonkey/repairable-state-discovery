# V2R cluster inventory

2026-09-23T17:45:40.708077+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41373773824 available bytes; 97.69% used; 110435440 free inodes.

server2 `/home`: 41373773824 available bytes; 97.69% used; 110435440 free inodes.

server2 `/tmp`: 41373773824 available bytes; 97.69% used; 110435440 free inodes.

server2 `/var/tmp`: 41373773824 available bytes; 97.69% used; 110435440 free inodes.

server2 `/mnt/raid5`: 546457534464 available bytes; 96.22% used; 445215447 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 294334373888 available bytes; 83.58% used; 114271290 free inodes.

server3 `/home`: 294334373888 available bytes; 83.58% used; 114271290 free inodes.

server3 `/data`: 52995928064 available bytes; 99.27% used; 225851738 free inodes.

server3 `/tmp`: 294334373888 available bytes; 83.58% used; 114271290 free inodes.

server3 `/var/tmp`: 294334373888 available bytes; 83.58% used; 114271290 free inodes.
| server4 | True | ['1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111488581632 available bytes; 93.78% used; 114375784 free inodes.

server4 `/home`: 111488581632 available bytes; 93.78% used; 114375784 free inodes.

server4 `/data`: 5550678016 available bytes; 99.92% used; 225468812 free inodes.

server4 `/tmp`: 111488581632 available bytes; 93.78% used; 114375784 free inodes.

server4 `/var/tmp`: 111488581632 available bytes; 93.78% used; 114375784 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
