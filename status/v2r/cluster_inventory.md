# V2R cluster inventory

2026-09-23T17:19:43.289175+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41384677376 available bytes; 97.69% used; 110435440 free inodes.

server2 `/home`: 41384677376 available bytes; 97.69% used; 110435440 free inodes.

server2 `/tmp`: 41384677376 available bytes; 97.69% used; 110435440 free inodes.

server2 `/var/tmp`: 41384677376 available bytes; 97.69% used; 110435440 free inodes.

server2 `/mnt/raid5`: 547156865024 available bytes; 96.22% used; 445216448 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 294398402560 available bytes; 83.57% used; 114275081 free inodes.

server3 `/home`: 294398402560 available bytes; 83.57% used; 114275081 free inodes.

server3 `/data`: 53094821888 available bytes; 99.27% used; 225852286 free inodes.

server3 `/tmp`: 294398402560 available bytes; 83.57% used; 114275081 free inodes.

server3 `/var/tmp`: 294398402560 available bytes; 83.57% used; 114275081 free inodes.
| server4 | True | ['1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111489318912 available bytes; 93.78% used; 114375792 free inodes.

server4 `/home`: 111489318912 available bytes; 93.78% used; 114375792 free inodes.

server4 `/data`: 26377932800 available bytes; 99.64% used; 225469168 free inodes.

server4 `/tmp`: 111489318912 available bytes; 93.78% used; 114375792 free inodes.

server4 `/var/tmp`: 111489318912 available bytes; 93.78% used; 114375792 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
